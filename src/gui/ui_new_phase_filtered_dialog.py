# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui_new_phase_filtered_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewPhaseFilteredDialog(object):
    def setupUi(self, NewPhaseFilteredDialog):
        NewPhaseFilteredDialog.setObjectName("NewPhaseFilteredDialog")
        NewPhaseFilteredDialog.resize(1120, 869)
        self.vlayout = QtWidgets.QVBoxLayout(NewPhaseFilteredDialog)
        self.vlayout.setObjectName("vlayout")
        self.zoomLayout = QtWidgets.QHBoxLayout()
        self.zoomLayout.setObjectName("zoomLayout")
        self.dummy1 = QtWidgets.QLabel(NewPhaseFilteredDialog)
        self.dummy1.setText("")
        self.dummy1.setObjectName("dummy1")
        self.zoomLayout.addWidget(self.dummy1)
        self.zoomLabel = QtWidgets.QLabel(NewPhaseFilteredDialog)
        self.zoomLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.zoomLabel.setObjectName("zoomLabel")
        self.zoomLayout.addWidget(self.zoomLabel)
        self.undoButton = QtWidgets.QPushButton(NewPhaseFilteredDialog)
        self.undoButton.setObjectName("undoButton")
        self.zoomLayout.addWidget(self.undoButton)
        self.redoButton = QtWidgets.QPushButton(NewPhaseFilteredDialog)
        self.redoButton.setObjectName("redoButton")
        self.zoomLayout.addWidget(self.redoButton)
        self.dummy11 = QtWidgets.QLabel(NewPhaseFilteredDialog)
        self.dummy11.setText("")
        self.dummy11.setObjectName("dummy11")
        self.zoomLayout.addWidget(self.dummy11)
        self.zoomLayout.setStretch(0, 1)
        self.zoomLayout.setStretch(4, 1)
        self.vlayout.addLayout(self.zoomLayout)
        self.splitter = QtWidgets.QSplitter(NewPhaseFilteredDialog)
        self.splitter.setStyleSheet("QSplitter::handle {\n"
"        border-top: 1px solid #888;\n"
"        border-bottom: 1px solid #888;\n"
"        margin: 8px 0;}\n"
"      ")
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(3)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.layoutWidgetTop = QtWidgets.QWidget(self.splitter)
        self.layoutWidgetTop.setObjectName("layoutWidgetTop")
        self.hTopLayout = QtWidgets.QHBoxLayout(self.layoutWidgetTop)
        self.hTopLayout.setContentsMargins(0, 0, 0, 0)
        self.hTopLayout.setObjectName("hTopLayout")
        self.vTopLeftLayout = QtWidgets.QVBoxLayout()
        self.vTopLeftLayout.setObjectName("vTopLeftLayout")
        self.label = QtWidgets.QLabel(self.layoutWidgetTop)
        self.label.setObjectName("label")
        self.vTopLeftLayout.addWidget(self.label)
        self.elementTable = QtWidgets.QTableWidget(self.layoutWidgetTop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.elementTable.sizePolicy().hasHeightForWidth())
        self.elementTable.setSizePolicy(sizePolicy)
        self.elementTable.setMinimumSize(QtCore.QSize(0, 0))
        self.elementTable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.elementTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.elementTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.elementTable.setShowGrid(False)
        self.elementTable.setColumnCount(4)
        self.elementTable.setObjectName("elementTable")
        self.elementTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.elementTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.elementTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.elementTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.elementTable.setHorizontalHeaderItem(3, item)
        self.elementTable.horizontalHeader().setCascadingSectionResizes(False)
        self.elementTable.horizontalHeader().setDefaultSectionSize(60)
        self.elementTable.horizontalHeader().setHighlightSections(False)
        self.elementTable.horizontalHeader().setMinimumSectionSize(14)
        self.elementTable.horizontalHeader().setSortIndicatorShown(True)
        self.elementTable.horizontalHeader().setStretchLastSection(True)
        self.elementTable.verticalHeader().setVisible(False)
        self.vTopLeftLayout.addWidget(self.elementTable)
        self.hTopLayout.addLayout(self.vTopLeftLayout)
        self.elementMatplotlibWidget = MatplotlibWidget(self.layoutWidgetTop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.elementMatplotlibWidget.sizePolicy().hasHeightForWidth())
        self.elementMatplotlibWidget.setSizePolicy(sizePolicy)
        self.elementMatplotlibWidget.setMinimumSize(QtCore.QSize(100, 100))
        self.elementMatplotlibWidget.setObjectName("elementMatplotlibWidget")
        self.hTopLayout.addWidget(self.elementMatplotlibWidget)
        self.gridTopRightLayout = QtWidgets.QGridLayout()
        self.gridTopRightLayout.setObjectName("gridTopRightLayout")
        self.lowerSlider = QtWidgets.QSlider(self.layoutWidgetTop)
        self.lowerSlider.setSingleStep(10)
        self.lowerSlider.setPageStep(100)
        self.lowerSlider.setOrientation(QtCore.Qt.Vertical)
        self.lowerSlider.setObjectName("lowerSlider")
        self.gridTopRightLayout.addWidget(self.lowerSlider, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.upperSlider = QtWidgets.QSlider(self.layoutWidgetTop)
        self.upperSlider.setSingleStep(10)
        self.upperSlider.setPageStep(100)
        self.upperSlider.setOrientation(QtCore.Qt.Vertical)
        self.upperSlider.setObjectName("upperSlider")
        self.gridTopRightLayout.addWidget(self.upperSlider, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label1 = QtWidgets.QLabel(self.layoutWidgetTop)
        self.label1.setObjectName("label1")
        self.gridTopRightLayout.addWidget(self.label1, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.layoutWidgetTop)
        self.label_2.setObjectName("label_2")
        self.gridTopRightLayout.addWidget(self.label_2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.lowerLineEdit = QtWidgets.QLineEdit(self.layoutWidgetTop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowerLineEdit.sizePolicy().hasHeightForWidth())
        self.lowerLineEdit.setSizePolicy(sizePolicy)
        self.lowerLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lowerLineEdit.setReadOnly(True)
        self.lowerLineEdit.setObjectName("lowerLineEdit")
        self.gridTopRightLayout.addWidget(self.lowerLineEdit, 2, 0, 1, 1)
        self.updateThresholdsButton = QtWidgets.QPushButton(self.layoutWidgetTop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateThresholdsButton.sizePolicy().hasHeightForWidth())
        self.updateThresholdsButton.setSizePolicy(sizePolicy)
        self.updateThresholdsButton.setObjectName("updateThresholdsButton")
        self.gridTopRightLayout.addWidget(self.updateThresholdsButton, 3, 0, 1, 1)
        self.clearThresholdsButton = QtWidgets.QPushButton(self.layoutWidgetTop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearThresholdsButton.sizePolicy().hasHeightForWidth())
        self.clearThresholdsButton.setSizePolicy(sizePolicy)
        self.clearThresholdsButton.setObjectName("clearThresholdsButton")
        self.gridTopRightLayout.addWidget(self.clearThresholdsButton, 3, 1, 1, 1)
        self.upperLineEdit = QtWidgets.QLineEdit(self.layoutWidgetTop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upperLineEdit.sizePolicy().hasHeightForWidth())
        self.upperLineEdit.setSizePolicy(sizePolicy)
        self.upperLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.upperLineEdit.setReadOnly(True)
        self.upperLineEdit.setObjectName("upperLineEdit")
        self.gridTopRightLayout.addWidget(self.upperLineEdit, 2, 1, 1, 1)
        self.hTopLayout.addLayout(self.gridTopRightLayout)
        self.hTopLayout.setStretch(1, 1)
        self.gridLayoutWidgetBottom = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidgetBottom.setObjectName("gridLayoutWidgetBottom")
        self.gridLayoutBottom = QtWidgets.QGridLayout(self.gridLayoutWidgetBottom)
        self.gridLayoutBottom.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutBottom.setObjectName("gridLayoutBottom")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidgetBottom)
        self.label_5.setObjectName("label_5")
        self.gridLayoutBottom.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidgetBottom)
        self.label_4.setMaximumSize(QtCore.QSize(205, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayoutBottom.addWidget(self.label_4, 0, 1, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.gridLayoutWidgetBottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy)
        self.nameEdit.setMaximumSize(QtCore.QSize(205, 16777215))
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayoutBottom.addWidget(self.nameEdit, 1, 1, 1, 1, QtCore.Qt.AlignTop)
        self.phaseMatplotlibWidget = MatplotlibWidget(self.gridLayoutWidgetBottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.phaseMatplotlibWidget.sizePolicy().hasHeightForWidth())
        self.phaseMatplotlibWidget.setSizePolicy(sizePolicy)
        self.phaseMatplotlibWidget.setMinimumSize(QtCore.QSize(100, 100))
        self.phaseMatplotlibWidget.setObjectName("phaseMatplotlibWidget")
        self.gridLayoutBottom.addWidget(self.phaseMatplotlibWidget, 1, 0, 2, 1)
        self.statusbar = QtWidgets.QLabel(self.gridLayoutWidgetBottom)
        self.statusbar.setText("")
        self.statusbar.setObjectName("statusbar")
        self.gridLayoutBottom.addWidget(self.statusbar, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidgetBottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMaximumSize(QtCore.QSize(205, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutBottom.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.gridLayoutBottom.setColumnMinimumWidth(0, 1)
        self.gridLayoutBottom.setColumnStretch(1, 1)
        self.gridLayoutBottom.setRowStretch(1, 1)
        self.vlayout.addWidget(self.splitter)

        self.retranslateUi(NewPhaseFilteredDialog)
        self.buttonBox.accepted.connect(NewPhaseFilteredDialog.accept)
        self.buttonBox.rejected.connect(NewPhaseFilteredDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewPhaseFilteredDialog)

    def retranslateUi(self, NewPhaseFilteredDialog):
        _translate = QtCore.QCoreApplication.translate
        NewPhaseFilteredDialog.setWindowTitle(_translate("NewPhaseFilteredDialog", "Create new phase map by thresholding filtered element maps"))
        self.zoomLabel.setText(_translate("NewPhaseFilteredDialog", "Zoom"))
        self.undoButton.setText(_translate("NewPhaseFilteredDialog", "Undo"))
        self.redoButton.setText(_translate("NewPhaseFilteredDialog", "Redo"))
        self.label.setText(_translate("NewPhaseFilteredDialog", "Elements and thresholds"))
        self.elementTable.setSortingEnabled(True)
        item = self.elementTable.horizontalHeaderItem(0)
        item.setText(_translate("NewPhaseFilteredDialog", "Element"))
        item = self.elementTable.horizontalHeaderItem(1)
        item.setText(_translate("NewPhaseFilteredDialog", "Name"))
        item = self.elementTable.horizontalHeaderItem(2)
        item.setText(_translate("NewPhaseFilteredDialog", "Lower"))
        item = self.elementTable.horizontalHeaderItem(3)
        item.setText(_translate("NewPhaseFilteredDialog", "Upper"))
        self.label1.setText(_translate("NewPhaseFilteredDialog", "Lower"))
        self.label_2.setText(_translate("NewPhaseFilteredDialog", "Upper"))
        self.updateThresholdsButton.setText(_translate("NewPhaseFilteredDialog", "Update"))
        self.clearThresholdsButton.setText(_translate("NewPhaseFilteredDialog", "Clear"))
        self.label_5.setText(_translate("NewPhaseFilteredDialog", "Phase map"))
        self.label_4.setText(_translate("NewPhaseFilteredDialog", "Phase name"))

from .matplotlib_widget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewPhaseFilteredDialog = QtWidgets.QDialog()
    ui = Ui_NewPhaseFilteredDialog()
    ui.setupUi(NewPhaseFilteredDialog)
    NewPhaseFilteredDialog.show()
    sys.exit(app.exec_())

