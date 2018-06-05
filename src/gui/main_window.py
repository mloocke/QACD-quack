import numpy as np
import os
from PyQt5 import QtCore, QtWidgets, QtGui
import string
import time

from src.model.elements import element_properties
from src.model.qacd_project import QACDProject, State
from .clustering_dialog import ClusteringDialog
from .display_options_dialog import DisplayOptionsDialog
from .filter_dialog import FilterDialog
from .matplotlib_widget import DataType, PlotType
from .new_phase_filtered_dialog import NewPhaseFilteredDialog
from .new_ratio_dialog import NewRatioDialog
from .progress_dialog import ProgressDialog
from .ui_main_window import Ui_MainWindow
from .zoom_history import ZoomHistory


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Inner class for current data displayed.
    class Current:
        def __init__(self):
            self.clear()

        def clear(self):
            # Selected array read from project.
            self.selected_array = None
            self.selected_array_stats = None

            # Displayed array is selected array masked by phase and/or region.
            # May be same objects as selected above.
            self.displayed_array = None
            self.displayed_array_stats = None

            self.data_type = DataType.NONE
            self.name = None   # e.g. element name, or 'total', etc.
            self.phase = None


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.matplotlibWidget.initialise(owning_window=self)

        self.statusbar.messageChanged.connect(self.status_bar_change)

        # Menu items.
        self.actionProjectNew.triggered.connect(self.new_project)
        self.actionProjectOpen.triggered.connect(self.choose_open_project)
        self.actionProjectClose.triggered.connect(self.close_project)
        self.actionFilter.triggered.connect(self.filter)
        self.actionClustering.triggered.connect(self.clustering)
        self.actionDisplayOptions.triggered.connect(self.display_options)

        # Tab widget controls.
        self.newRatioButton.clicked.connect(self.new_ratio)
        self.deleteRatioButton.clicked.connect(self.delete_ratio)
        self.newPhaseFilteredButton.clicked.connect(self.new_phase_filtered)
        self.deletePhaseButton.clicked.connect(self.delete_phase)

        # Matplotlib toolbar controls.
        self.plotTypeComboBox.currentIndexChanged.connect(self.change_plot_type)
        self.phaseComboBox.currentIndexChanged.connect(self.change_phase)
        self.undoButton.clicked.connect(self.zoom_undo)
        self.redoButton.clicked.connect(self.zoom_redo)

        # Set initial width of tabWidget.  Needs improvement.
        #self.splitter.setSizes([50, 100])

        # Hide all but the first tab.
        for i in range(self.tabWidget.count()-1, 0, -1):
            self.tabWidget.removeTab(i)

        self._tabs_and_tables = (
            (DataType.RAW,        self.rawTab,        self.rawTable,        'Raw'),
            (DataType.FILTERED,   self.filteredTab,   self.filteredTable,   'Filtered'),
            (DataType.NORMALISED, self.normalisedTab, self.normalisedTable, 'Normalised'),
            (DataType.RATIO,      self.ratioTab,      self.ratioTable,      'Ratios'),
            (DataType.CLUSTER,    self.clusterTab,    self.clusterTable,    'Clusters'),
            (DataType.PHASE,      self.phaseTab,      self.phaseTable,      'Phases'),
        )

        # Correct table widget properties and connect signals and slots.
        for (_, _, table, _) in self._tabs_and_tables:
            horiz = table.horizontalHeader()
            horiz.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
            horiz.setDefaultAlignment(QtCore.Qt.AlignLeft)

            vert = table.verticalHeader()
            vert.setDefaultSectionSize(vert.minimumSectionSize())

            table.itemSelectionChanged.connect(self.change_table_item)

        # Read-only checkboxes.
        for checkbox in (self.pixelTotalsCheckBox, self.medianFilterCheckBox):
            checkbox.setFocusPolicy(QtCore.Qt.NoFocus)
            checkbox.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)

        # Member variables.
        self._project = None

        self._current = self.Current()  # Current data displayed.

        self._ignore_selection_change = False
        self._display_options_shown = False

        self._zoom_history = ZoomHistory()

        self.update_controls()
        self.update_title()

    def change_phase(self):
        text = self.phaseComboBox.currentText()
        if text == '':
            self._current.phase = None
        else:
            self._current.phase = ~self._project.get_phase(text, masked=False)

        if self._project is not None:
            self.update_matplotlib_widget()
            self.update_status_bar()

    def change_plot_type(self):
        self.update_matplotlib_widget()

    def change_table_item(self):
        if self._ignore_selection_change:
            return

        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.BusyCursor)

        if self._project is not None:
            current = self._current

            # Determine which table widget and which element selected.
            tab_index = self.tabWidget.currentIndex()
            current.data_type, _, table_widget, _ = self._tabs_and_tables[tab_index]
            row = table_widget.currentRow()
            item = table_widget.item(row, 0)
            if item is not None:
                current.name = item.text()
            else:
                current.name = None

            # Clear other table widgets.
            self._ignore_selection_change = True
            for index, (_, _, widget, _) in enumerate(self._tabs_and_tables):
                if index != tab_index:
                    widget.clearSelection()
                    widget.setCurrentItem(None)
            self._ignore_selection_change = False

            # Retrieve array and array stats from project.
            if current.name is None:
                current.data_type = DataType.NONE
                ret = (None, None)
            elif current.data_type == DataType.RAW:
                if current.name == 'Total':
                    ret = self._project.get_raw_total(want_stats=True)
                else:
                    ret = self._project.get_raw(current.name, want_stats=True)
            elif current.data_type == DataType.FILTERED:
                if current.name == 'Total':
                    ret = self._project.get_filtered_total(want_stats=True)
                else:
                    ret = self._project.get_filtered(current.name, want_stats=True)
            elif current.data_type == DataType.NORMALISED:
                if current.name in ('h', 'h-factor'):
                    ret = self._project.get_h_factor(want_stats=True)
                else:
                    ret = self._project.get_normalised(current.name, want_stats=True)
            elif current.data_type == DataType.RATIO:
                ret = self._project.get_ratio_by_name(current.name, want_stats=True)
            elif current.data_type == DataType.CLUSTER:
                current.name = int(current.name)
                ret = self._project.get_cluster_indices(current.name, want_stats=True)
            elif current.data_type == DataType.PHASE:
                ret = self._project.get_phase(current.name, want_stats=True)
            else:
                raise RuntimeError('Not implemented ' + type_)

            current.selected_array, current.selected_array_stats = ret

        self.update_controls()
        self.update_matplotlib_widget()
        self.update_status_bar()
        QtWidgets.QApplication.restoreOverrideCursor()

    def choose_open_project(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, _ = QtWidgets.QFileDialog.getOpenFileName( \
            self, 'Select project file to open', '',
            'Quack project files (*.quack)', options=options)
        if filename:
            self.open_project(filename)

    def close_project(self):
        if self._project is not None:
            self._project = None
            self._current.clear()

            # Clear table widgets.
            for i, (_, _, widget, _) in enumerate(self._tabs_and_tables):
                widget.setRowCount(0)

            # Hide all but the first tab.
            for i in range(self.tabWidget.count()-1, 0, -1):
                self.tabWidget.removeTab(i)

            self.update_matplotlib_widget()
            self.matplotlibWidget.clear_all()
            self.update_controls()
            self.update_phase_combo_box()
            self.update_status_bar()
            self.update_title()

    def clustering(self):
        dialog = ClusteringDialog(self._project, parent=self)
        if dialog.exec_():
            if self._project.has_cluster():
                button = QtWidgets.QMessageBox.question(self,
                    'k-means cluster maps already exist',
                    'Proceeding will delete the previous k-means cluster maps.<br>Do you want to continue?')
                if button == QtWidgets.QMessageBox.Yes:
                    self._project.delete_all_clusters()
                    self.fill_table_widget(4)
                else:
                    return

            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.BusyCursor)

            k_min, k_max, want_all_elements = dialog.get_values()

            def thread_func(project, k_min, k_max, progress_callback):
                self.short_wait()
                project.k_means_clustering(k_min, k_max, want_all_elements,
                    progress_callback=progress_callback)

            ProgressDialog.worker_thread( \
                self, 'k-means Clustering', thread_func,
                args=[self._project, k_min, k_max])

            self.fill_table_widget(4)
            self.tabWidget.setCurrentIndex(4)  # Bring tab to front.

            self.update_controls()
            QtWidgets.QApplication.restoreOverrideCursor()

    def delete_phase(self):
        table_widget = self.phaseTable

        row = table_widget.currentRow()
        name = table_widget.item(row, 0).text()
        button = QtWidgets.QMessageBox.question(self, 'Delete phase map',
            "Are you sure you want to delete phase map '{}'?".format(name))
        if button == QtWidgets.QMessageBox.Yes:
            table_widget.clearSelection()
            table_widget.removeRow(row)
            self._project.delete_phase_map(name)
            self.update_phase_combo_box()
            self.update_controls()
            if len(self._project.phases) == 0:
                # If other phases remain, one is automatically selected and so
                # mpl widget is automatically updated.  Need to clear selection
                # and update mpl widget manually if no other phases remain.
                self._current.clear()
                self.update_matplotlib_widget()

    def delete_ratio(self):
        table_widget = self.ratioTable

        row = table_widget.currentRow()
        name = table_widget.item(row, 0).text()
        button = QtWidgets.QMessageBox.question(self, 'Delete ratio map',
            "Are you sure you want to delete ratio map '{}'?".format(name))
        if button == QtWidgets.QMessageBox.Yes:
            table_widget.clearSelection()
            table_widget.removeRow(row)
            self._project.delete_ratio_map(name)
            self.update_controls()
            if len(self._project.ratios) == 0:
                # If other ratios remain, one is automatically selected and so
                # mpl widget is automatically updated.  Need to clear selection
                # and update mpl widget manually if no other ratios remain.
                self._current.clear()
                self.update_matplotlib_widget()

    def display_options(self):
        def finished():
            self._display_options_shown = False
            self.update_controls()

        colormap_name = self.matplotlibWidget.get_colormap_name()
        valid_colormap_names = self.matplotlibWidget.get_valid_colormap_names()

        dialog = DisplayOptionsDialog(colormap_name, valid_colormap_names,
                                      parent=self)
        dialog.finished.connect(finished)
        dialog.show()

        self._display_options_shown = True
        self.update_controls()

    def fill_table_widget(self, index):
        data_type, tab_widget, table_widget, tab_title = \
            self._tabs_and_tables[index]

        # Disable sorting whilst changing content.
        sorting = table_widget.isSortingEnabled()
        table_widget.setSortingEnabled(False)

        if self.tabWidget.widget(index) != tab_widget:
            self.tabWidget.insertTab(index, tab_widget, tab_title)

        rows = []
        if data_type in (DataType.RAW, DataType.FILTERED, DataType.NORMALISED):
            for i, element in enumerate(self._project.elements):
                name = element_properties[element][0]
                rows.append((element, name))
            if data_type in (DataType.RAW, DataType.FILTERED):
                rows.append(('Total', ''))
            if data_type == DataType.NORMALISED and self._project.state >= State.H_FACTOR:
                rows.append(('h-factor', ''))
        elif data_type == DataType.RATIO:
            for name, tuple_ in self._project.ratios.items():
                rows.append((name, tuple_[0], tuple_[1]))
        elif data_type == DataType.CLUSTER:
            cluster_k = self._project.get_cluster_k()
            if cluster_k is not None:
                k_min, k_max = cluster_k
                for k in range(k_min, k_max+1):
                    rows.append((str(k),))
        elif data_type == DataType.PHASE:
            for name in self._project.phases:
                source = self._project.get_phase_source(name)
                rows.append((name, source))

        nrows = len(rows)
        table_widget.setRowCount(nrows)
        for i, row in enumerate(rows):
            for j, text in enumerate(row):
                item = QtWidgets.QTableWidgetItem(text)
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                table_widget.setItem(i, j, item)
        table_widget.setSortingEnabled(sorting)

        # Reset column widths
        for column in range(table_widget.columnCount()):
            table_widget.resizeColumnToContents(column)

        if index == 1:
            filter_options = self._project.get_filter_options()
            self.pixelTotalsCheckBox.setChecked(filter_options[0])
            self.medianFilterCheckBox.setChecked(filter_options[1])
        elif index == 4:
            cluster_elements = self._project.get_cluster_elements()
            self.includedElementsLabel.setText( \
                'Included elements: {}'.format(cluster_elements))

    def filter(self):
        dialog = FilterDialog(parent=self)
        if dialog.exec_():
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.BusyCursor)

            pixel_totals = dialog.pixelTotalsCheckBox.isChecked()
            median_filter = dialog.medianFilterCheckBox.isChecked()

            def thread_func(project, pixel_totals, median_filter, progress_callback):
                self.short_wait()
                project.filter_normalise_and_h_factor( \
                    pixel_totals, median_filter, progress_callback=progress_callback)

            ProgressDialog.worker_thread( \
                self, 'Filter and Normalise', thread_func,
                args=[self._project, pixel_totals, median_filter])

            for index in range(1, 6):
                self.fill_table_widget(index)
            self.tabWidget.setCurrentIndex(2)  # Bring tab to front.

            self.update_controls()
            QtWidgets.QApplication.restoreOverrideCursor()

    def new_project(self):
        # Select file to save new project to.
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, _ = QtWidgets.QFileDialog.getSaveFileName( \
            self, 'Save new project as...', '',
            'Quack project files (*.quack)', options=options)
        if not filename:
            return

        if os.path.splitext(filename)[1] != '.quack':
            filename = os.path.splitext(filename)[0] + '.quack'
        # Danger of overwriting without prompting here?

        # Select CSV files to import.
        csv_files, _ = QtWidgets.QFileDialog.getOpenFileNames( \
            self, 'Select CSV files containing raw element maps to import',
            os.path.dirname(filename), 'CSV files (*.csv)', options=options)
        if len(csv_files) < 1:
            return

        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.BusyCursor)

        self.close_project()
        try:
            self._project = QACDProject()
            self._project.set_filename(filename)

            csv_directory = os.path.dirname(csv_files[0])
            csv_files = [os.path.basename(f) for f in csv_files]
        except:
            print('Need to display message box')

        def thread_func(project, csv_directory, csv_files, progress_callback):
            self.short_wait()
            project.import_raw_csv_files(csv_directory, csv_files,
                                         progress_callback=progress_callback)

        ProgressDialog.worker_thread( \
            self, 'New project ' + os.path.basename(filename), thread_func,
            args=[self._project, csv_directory, csv_files])

        self.fill_table_widget(0)
        self.tabWidget.setCurrentIndex(0)  # Bring tab to front.

        self.update_controls()
        self.update_matplotlib_widget()
        self.update_status_bar()
        self.update_title()
        QtWidgets.QApplication.restoreOverrideCursor()

    def new_phase_filtered(self):
        # Create new phase map from filtered element maps.
        dialog = NewPhaseFilteredDialog(self._project, parent=self)
        if dialog.exec_():
            name = dialog.get_name()

            self.fill_table_widget(5)

            # Find row matching name and select it.
            table_widget = self.phaseTable
            match = table_widget.findItems(name, QtCore.Qt.MatchExactly)
            row = match[0].row()
            table_widget.clearSelection()
            table_widget.selectRow(row)

            self.update_phase_combo_box()
            self.update_controls()

    def new_ratio(self):
        dialog = NewRatioDialog(self._project, parent=self)
        if dialog.exec_():
            name = dialog.get_name()

            self.fill_table_widget(3)  # Update user interface.

            # Find row matching name and select it.
            table_widget = self.ratioTable
            match = table_widget.findItems(name, QtCore.Qt.MatchExactly)
            row = match[0].row()
            table_widget.clearSelection()
            table_widget.selectRow(row)

            self.update_controls()

    def open_project(self, filename):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.BusyCursor)

        project = None
        try:
            project = QACDProject()
            project.load_file(filename)
        except Exception as e:
            print('Need to display message box: {}'.format(e))

        # Opened project is OK, so can close previous project.
        self.close_project()
        self._project = project

        if self._project.state >= State.RAW:
            self.fill_table_widget(0)  # Raw.
            self.tabWidget.setCurrentIndex(0)  # Bring tab to front.

        if self._project.state >= State.FILTERED:
            self.fill_table_widget(1)  # Filtered.
            self.tabWidget.setCurrentIndex(1)  # Bring tab to front.

        if self._project.state >= State.NORMALISED:
            self.fill_table_widget(2)  # Normalised (and h-factor if present).
            self.tabWidget.setCurrentIndex(2)  # Bring tab to front.

        if self._project.state >= State.H_FACTOR:
            self.fill_table_widget(3)  # Ratios.
            self.fill_table_widget(4)  # Clustering.
            self.fill_table_widget(5)  # Phases.

        self.update_controls()
        self.update_matplotlib_widget()
        self.update_phase_combo_box()
        self.update_status_bar()
        self.update_title()
        QtWidgets.QApplication.restoreOverrideCursor()

    def set_colormap_name(self, colormap_name):
        if self.matplotlibWidget is not None:
            self.matplotlibWidget.set_colormap_name(colormap_name)

    def short_wait(self):
        time.sleep(0.1)

    def status_bar_change(self):
        if (self.statusbar.currentMessage() == '' and \
            self._current.selected_array is not None):
            self.update_status_bar()

    def update_controls(self):
        valid_project = self._project is not None
        showing_phase = self._current.data_type == DataType.PHASE

        # Menu items.
        self.actionProjectClose.setEnabled(valid_project)
        self.actionFilter.setEnabled(valid_project and
                                     self._project.state == State.RAW)
        self.actionClustering.setEnabled(valid_project and
                                         self._project.state == State.H_FACTOR)
        self.actionDisplayOptions.setEnabled(not self._display_options_shown)

        # Tab widget controls.
        self.deleteRatioButton.setEnabled(self.ratioTable.currentItem() is not None)
        self.deletePhaseButton.setEnabled(self.phaseTable.currentItem() is not None)

        # Matplotlib toolbar controls.
        self.plotTypeComboBox.setEnabled(not showing_phase)
        self.plotTypeLabel.setEnabled(not showing_phase)
        self.phaseComboBox.setEnabled(not showing_phase)
        self.phaseLabel.setEnabled(not showing_phase)
        self.regionComboBox.setEnabled(not showing_phase)
        self.regionLabel.setEnabled(not showing_phase)
        self.undoButton.setEnabled(self._zoom_history.has_undo())
        self.redoButton.setEnabled(self._zoom_history.has_redo())

    def update_matplotlib_widget(self):
        current = self._current

        if current.data_type is DataType.NONE:
            self.matplotlibWidget.clear()
        else:
            plot_type = PlotType(self.plotTypeComboBox.currentIndex())
            cmap_int_max = None
            show_colorbar = True
            if current.name in ('h', 'h-factor'):
                title = 'h-factor'
            elif current.data_type == DataType.RATIO:
                title = current.name + ' ratio'
            elif current.data_type == DataType.CLUSTER:
                title = 'k={} cluster'.format(current.name)
                cmap_int_max = current.name
            elif current.data_type == DataType.PHASE:
                title = current.name + ' phase'
                cmap_int_max = 2
                plot_type = PlotType.MAP
                show_colorbar = False
            else:
                if current.name == 'Total':
                    name = 'total'
                else:
                    name = element_properties[current.name][0]
                type_string = string.capwords(current.data_type.name.lower())
                title = '{} {} element'.format(type_string, name)

            if current.data_type != DataType.PHASE and current.phase is not None:
                # May want to cache this instead of recalculating it each time.
                array = np.ma.masked_where(current.phase, current.selected_array)
                array_stats = {}
                if 'valid' in current.selected_array_stats:
                    number_invalid = np.ma.count_masked(array)
                    array_stats['invalid'] = number_invalid
                    array_stats['valid'] = array.size - number_invalid
                if 'min' in current.selected_array_stats:
                    array_stats['max'] = array.max()
                    array_stats['min'] = array.min()
                if 'mean' in current.selected_array_stats:
                    array_stats['mean'] = array.mean()
                if 'median' in current.selected_array_stats:
                    array_stats['median'] = np.ma.median(array)
                if 'std' in current.selected_array_stats:
                    array_stats['std'] = array.std()
                current.displayed_array = array
                current.displayed_array_stats = array_stats
                # Assuming update_status_bar will follow anyway.
            else:
                current.displayed_array = current.selected_array
                current.displayed_array_stats = current.selected_array_stats

            self.matplotlibWidget.update( \
                plot_type, current.displayed_array, current.displayed_array_stats,
                title, show_colorbar=show_colorbar, cmap_int_max=cmap_int_max)

    def update_phase_combo_box(self):
        combo_box = self.phaseComboBox
        combo_box.clear()
        combo_box.addItem('')
        if self._project is not None:
            for phase in self._project.phases:
                combo_box.addItem(phase)

    def update_status_bar(self):
        def stat_to_string(name, label=None):
            label = label or name
            value = self._current.displayed_array_stats.get(name)
            if value is None:
                return ''
            elif isinstance(value, np.float):
                if int(value) == value:
                    value = int(value)
                else:
                    value = float('{:.5g}'.format(value))
                return ', {}={}'.format(label, value)
            else:
                return ', {}={}'.format(label, value)

        if self._current.displayed_array is not None:
            ny, nx = self._current.displayed_array.shape
            msg = 'pixels={}x{}'.format(nx, ny)
            msg += stat_to_string('valid')
            msg += stat_to_string('invalid')
            msg += stat_to_string('min')
            msg += stat_to_string('max')
            msg += stat_to_string('mean')
            msg += stat_to_string('median')
            msg += stat_to_string('std')
            self.statusbar.showMessage(msg)
        else:
            self.statusbar.clearMessage()

    def update_title(self):
        title = 'QACD quack'
        if self._project is not None:
            title += ' - ' + self._project.filename
        self.setWindowTitle(title)

    def zoom_append(self, from_, to):
        # Append zoom rectangle to zoom history, and apply it.
        self._zoom_history.append(from_, to)
        self.matplotlibWidget.set_map_zoom(to[0], to[1])
        self.update_controls()

    def zoom_redo(self):
        zoom = self._zoom_history.redo()
        self.matplotlibWidget.set_map_zoom(zoom[1][0], zoom[1][1])
        self.update_controls()

    def zoom_undo(self):
        zoom = self._zoom_history.undo()
        self.matplotlibWidget.set_map_zoom(zoom[0][0], zoom[0][1])
        self.update_controls()
