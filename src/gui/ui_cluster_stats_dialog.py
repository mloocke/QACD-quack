# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui_cluster_stats_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClusterStatsDialog(object):
    def setupUi(self, ClusterStatsDialog):
        ClusterStatsDialog.setObjectName("ClusterStatsDialog")
        ClusterStatsDialog.resize(977, 693)
        self.verticalLayout = QtWidgets.QVBoxLayout(ClusterStatsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ClusterStatsDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(ClusterStatsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tableTab = QtWidgets.QWidget()
        self.tableTab.setObjectName("tableTab")
        self.tableLayout = QtWidgets.QVBoxLayout(self.tableTab)
        self.tableLayout.setContentsMargins(9, 9, 9, 9)
        self.tableLayout.setObjectName("tableLayout")
        self.label1 = QtWidgets.QLabel(self.tableTab)
        self.label1.setObjectName("label1")
        self.tableLayout.addWidget(self.label1)
        self.table = QtWidgets.QTableWidget(self.tableTab)
        self.table.setStyleSheet("")
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.verticalHeader().setVisible(False)
        self.tableLayout.addWidget(self.table)
        self.tabWidget.addTab(self.tableTab, "")
        self.plotTab = QtWidgets.QWidget()
        self.plotTab.setObjectName("plotTab")
        self.plotLayout = QtWidgets.QHBoxLayout(self.plotTab)
        self.plotLayout.setContentsMargins(9, 9, 9, 9)
        self.plotLayout.setObjectName("plotLayout")
        self.left = QtWidgets.QVBoxLayout()
        self.left.setObjectName("left")
        self.showClusterTableWidget = QtWidgets.QTableWidget(self.plotTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showClusterTableWidget.sizePolicy().hasHeightForWidth())
        self.showClusterTableWidget.setSizePolicy(sizePolicy)
        self.showClusterTableWidget.setMaximumSize(QtCore.QSize(160, 16777215))
        self.showClusterTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.showClusterTableWidget.setColumnCount(3)
        self.showClusterTableWidget.setObjectName("showClusterTableWidget")
        self.showClusterTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.showClusterTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.showClusterTableWidget.setHorizontalHeaderItem(1, item)
        self.showClusterTableWidget.horizontalHeader().setStretchLastSection(True)
        self.showClusterTableWidget.verticalHeader().setVisible(False)
        self.left.addWidget(self.showClusterTableWidget)
        self.showAllButton = QtWidgets.QPushButton(self.plotTab)
        self.showAllButton.setObjectName("showAllButton")
        self.left.addWidget(self.showAllButton)
        self.hideAllButton = QtWidgets.QPushButton(self.plotTab)
        self.hideAllButton.setObjectName("hideAllButton")
        self.left.addWidget(self.hideAllButton)
        self.showXAxisLabelsCheckBox = QtWidgets.QCheckBox(self.plotTab)
        self.showXAxisLabelsCheckBox.setChecked(True)
        self.showXAxisLabelsCheckBox.setObjectName("showXAxisLabelsCheckBox")
        self.left.addWidget(self.showXAxisLabelsCheckBox)
        self.plotLayout.addLayout(self.left)
        self.clusterStatsWidget = ClusterStatsWidget(self.plotTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.clusterStatsWidget.sizePolicy().hasHeightForWidth())
        self.clusterStatsWidget.setSizePolicy(sizePolicy)
        self.clusterStatsWidget.setObjectName("clusterStatsWidget")
        self.plotLayout.addWidget(self.clusterStatsWidget)
        self.plotLayout.setStretch(1, 1)
        self.tabWidget.addTab(self.plotTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.h = QtWidgets.QHBoxLayout()
        self.h.setObjectName("h")
        self.statusLabel = QtWidgets.QLabel(ClusterStatsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy)
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.h.addWidget(self.statusLabel)
        self.buttonBox = QtWidgets.QDialogButtonBox(ClusterStatsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.h.addWidget(self.buttonBox)
        self.h.setStretch(0, 1)
        self.verticalLayout.addLayout(self.h)

        self.retranslateUi(ClusterStatsDialog)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(ClusterStatsDialog.accept)
        self.buttonBox.rejected.connect(ClusterStatsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ClusterStatsDialog)

    def retranslateUi(self, ClusterStatsDialog):
        _translate = QtCore.QCoreApplication.translate
        ClusterStatsDialog.setWindowTitle(_translate("ClusterStatsDialog", "Cluster Stats Dialog"))
        self.label.setText(_translate("ClusterStatsDialog", "Filtered element values of centroids of each cluster."))
        self.label1.setText(_translate("ClusterStatsDialog", "Click on a column heading to sort on that column"))
        self.table.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tableTab), _translate("ClusterStatsDialog", "Table"))
        item = self.showClusterTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ClusterStatsDialog", "Show"))
        item = self.showClusterTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ClusterStatsDialog", "Cluster"))
        self.showAllButton.setToolTip(_translate("ClusterStatsDialog", "Show all clusters"))
        self.showAllButton.setText(_translate("ClusterStatsDialog", "Show all"))
        self.hideAllButton.setToolTip(_translate("ClusterStatsDialog", "Hide all clusters"))
        self.hideAllButton.setText(_translate("ClusterStatsDialog", "Hide all"))
        self.showXAxisLabelsCheckBox.setText(_translate("ClusterStatsDialog", "Show x-axis labels"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plotTab), _translate("ClusterStatsDialog", "Plot"))

from .cluster_stats_widget import ClusterStatsWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClusterStatsDialog = QtWidgets.QDialog()
    ui = Ui_ClusterStatsDialog()
    ui.setupUi(ClusterStatsDialog)
    ClusterStatsDialog.show()
    sys.exit(app.exec_())

