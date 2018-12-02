# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui_display_options_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DisplayOptionsDialog(object):
    def setupUi(self, DisplayOptionsDialog):
        DisplayOptionsDialog.setObjectName("DisplayOptionsDialog")
        DisplayOptionsDialog.resize(429, 537)
        self.verticalLayout = QtWidgets.QVBoxLayout(DisplayOptionsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(DisplayOptionsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.colourmapTab = QtWidgets.QWidget()
        self.colourmapTab.setObjectName("colourmapTab")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.colourmapTab)
        self.verticalLayout1.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.colourmapListWidget = QtWidgets.QListWidget(self.colourmapTab)
        self.colourmapListWidget.setObjectName("colourmapListWidget")
        self.verticalLayout1.addWidget(self.colourmapListWidget)
        self.reverseCheckBox = QtWidgets.QCheckBox(self.colourmapTab)
        self.reverseCheckBox.setObjectName("reverseCheckBox")
        self.verticalLayout1.addWidget(self.reverseCheckBox)
        self.tabWidget.addTab(self.colourmapTab, "")
        self.labelsAndScaleTab = QtWidgets.QWidget()
        self.labelsAndScaleTab.setObjectName("labelsAndScaleTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.labelsAndScaleTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.showTicksAndLabelsCheckBox = QtWidgets.QCheckBox(self.labelsAndScaleTab)
        self.showTicksAndLabelsCheckBox.setObjectName("showTicksAndLabelsCheckBox")
        self.verticalLayout_2.addWidget(self.showTicksAndLabelsCheckBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.labelsAndScaleTab)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.overallTitleLineEdit = QtWidgets.QLineEdit(self.labelsAndScaleTab)
        self.overallTitleLineEdit.setObjectName("overallTitleLineEdit")
        self.horizontalLayout_2.addWidget(self.overallTitleLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.showProjectFilenameCheckBox = QtWidgets.QCheckBox(self.labelsAndScaleTab)
        self.showProjectFilenameCheckBox.setObjectName("showProjectFilenameCheckBox")
        self.verticalLayout_2.addWidget(self.showProjectFilenameCheckBox)
        self.showDateCheckBox = QtWidgets.QCheckBox(self.labelsAndScaleTab)
        self.showDateCheckBox.setObjectName("showDateCheckBox")
        self.verticalLayout_2.addWidget(self.showDateCheckBox)
        self.line = QtWidgets.QFrame(self.labelsAndScaleTab)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.useScaleCheckBox = QtWidgets.QCheckBox(self.labelsAndScaleTab)
        self.useScaleCheckBox.setObjectName("useScaleCheckBox")
        self.verticalLayout_2.addWidget(self.useScaleCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pixelSizeLabel = QtWidgets.QLabel(self.labelsAndScaleTab)
        self.pixelSizeLabel.setObjectName("pixelSizeLabel")
        self.horizontalLayout.addWidget(self.pixelSizeLabel)
        self.pixelSizeLineEdit = QtWidgets.QLineEdit(self.labelsAndScaleTab)
        self.pixelSizeLineEdit.setObjectName("pixelSizeLineEdit")
        self.horizontalLayout.addWidget(self.pixelSizeLineEdit)
        self.unitsComboBox = QtWidgets.QComboBox(self.labelsAndScaleTab)
        self.unitsComboBox.setObjectName("unitsComboBox")
        self.horizontalLayout.addWidget(self.unitsComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.showScaleBarCheckBox = QtWidgets.QCheckBox(self.labelsAndScaleTab)
        self.showScaleBarCheckBox.setObjectName("showScaleBarCheckBox")
        self.verticalLayout_2.addWidget(self.showScaleBarCheckBox)
        self.scaleBarLocationGroupBox = QtWidgets.QGroupBox(self.labelsAndScaleTab)
        self.scaleBarLocationGroupBox.setObjectName("scaleBarLocationGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.scaleBarLocationGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.upperLeftRadioButton = QtWidgets.QRadioButton(self.scaleBarLocationGroupBox)
        self.upperLeftRadioButton.setObjectName("upperLeftRadioButton")
        self.gridLayout.addWidget(self.upperLeftRadioButton, 0, 0, 1, 1)
        self.upperRightRadioButton = QtWidgets.QRadioButton(self.scaleBarLocationGroupBox)
        self.upperRightRadioButton.setObjectName("upperRightRadioButton")
        self.gridLayout.addWidget(self.upperRightRadioButton, 0, 1, 1, 1)
        self.lowerLeftRadioButton = QtWidgets.QRadioButton(self.scaleBarLocationGroupBox)
        self.lowerLeftRadioButton.setObjectName("lowerLeftRadioButton")
        self.gridLayout.addWidget(self.lowerLeftRadioButton, 1, 0, 1, 1)
        self.lowerRightRadioButton = QtWidgets.QRadioButton(self.scaleBarLocationGroupBox)
        self.lowerRightRadioButton.setObjectName("lowerRightRadioButton")
        self.gridLayout.addWidget(self.lowerRightRadioButton, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.scaleBarLocationGroupBox)
        self.scaleBarColourGroupBox = QtWidgets.QGroupBox(self.labelsAndScaleTab)
        self.scaleBarColourGroupBox.setObjectName("scaleBarColourGroupBox")
        self.scaleBarColourLayout = QtWidgets.QVBoxLayout(self.scaleBarColourGroupBox)
        self.scaleBarColourLayout.setObjectName("scaleBarColourLayout")
        self.blackRadioButton = QtWidgets.QRadioButton(self.scaleBarColourGroupBox)
        self.blackRadioButton.setObjectName("blackRadioButton")
        self.scaleBarColourLayout.addWidget(self.blackRadioButton)
        self.whiteRadioButton = QtWidgets.QRadioButton(self.scaleBarColourGroupBox)
        self.whiteRadioButton.setObjectName("whiteRadioButton")
        self.scaleBarColourLayout.addWidget(self.whiteRadioButton)
        self.verticalLayout_2.addWidget(self.scaleBarColourGroupBox)
        self.dummyLabel = QtWidgets.QLabel(self.labelsAndScaleTab)
        self.dummyLabel.setText("")
        self.dummyLabel.setObjectName("dummyLabel")
        self.verticalLayout_2.addWidget(self.dummyLabel)
        self.tabWidget.addTab(self.labelsAndScaleTab, "")
        self.histogramTab = QtWidgets.QWidget()
        self.histogramTab.setObjectName("histogramTab")
        self.v = QtWidgets.QVBoxLayout(self.histogramTab)
        self.v.setObjectName("v")
        self.fixedBinCountGroupBox = QtWidgets.QGroupBox(self.histogramTab)
        self.fixedBinCountGroupBox.setCheckable(True)
        self.fixedBinCountGroupBox.setObjectName("fixedBinCountGroupBox")
        self.h = QtWidgets.QHBoxLayout(self.fixedBinCountGroupBox)
        self.h.setObjectName("h")
        self.label_2 = QtWidgets.QLabel(self.fixedBinCountGroupBox)
        self.label_2.setObjectName("label_2")
        self.h.addWidget(self.label_2)
        self.histogramBinCountComboBox = QtWidgets.QComboBox(self.fixedBinCountGroupBox)
        self.histogramBinCountComboBox.setObjectName("histogramBinCountComboBox")
        self.h.addWidget(self.histogramBinCountComboBox)
        self.v.addWidget(self.fixedBinCountGroupBox)
        self.fixedBinWidthGroupBox = QtWidgets.QGroupBox(self.histogramTab)
        self.fixedBinWidthGroupBox.setCheckable(True)
        self.fixedBinWidthGroupBox.setChecked(False)
        self.fixedBinWidthGroupBox.setObjectName("fixedBinWidthGroupBox")
        self.g = QtWidgets.QGridLayout(self.fixedBinWidthGroupBox)
        self.g.setObjectName("g")
        self.label_2a = QtWidgets.QLabel(self.fixedBinWidthGroupBox)
        self.label_2a.setObjectName("label_2a")
        self.g.addWidget(self.label_2a, 0, 0, 1, 1)
        self.histogramBinWidthLineEdit = QtWidgets.QLineEdit(self.fixedBinWidthGroupBox)
        self.histogramBinWidthLineEdit.setObjectName("histogramBinWidthLineEdit")
        self.g.addWidget(self.histogramBinWidthLineEdit, 0, 1, 1, 1)
        self.label_2b = QtWidgets.QLabel(self.fixedBinWidthGroupBox)
        self.label_2b.setObjectName("label_2b")
        self.g.addWidget(self.label_2b, 1, 0, 1, 1)
        self.maxBinCountLineEdit = QtWidgets.QLineEdit(self.fixedBinWidthGroupBox)
        self.maxBinCountLineEdit.setObjectName("maxBinCountLineEdit")
        self.g.addWidget(self.maxBinCountLineEdit, 1, 1, 1, 1)
        self.v.addWidget(self.fixedBinWidthGroupBox)
        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.v.addItem(spacerItem)
        self.line2 = QtWidgets.QFrame(self.histogramTab)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setLineWidth(1)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setObjectName("line2")
        self.v.addWidget(self.line2)
        self.showMeanMedianStdCheckBox = QtWidgets.QCheckBox(self.histogramTab)
        self.showMeanMedianStdCheckBox.setObjectName("showMeanMedianStdCheckBox")
        self.v.addWidget(self.showMeanMedianStdCheckBox)
        self.dummy = QtWidgets.QLabel(self.histogramTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.dummy.sizePolicy().hasHeightForWidth())
        self.dummy.setSizePolicy(sizePolicy)
        self.dummy.setObjectName("dummy")
        self.v.addWidget(self.dummy)
        self.tabWidget.addTab(self.histogramTab, "")
        self.zoomTab = QtWidgets.QWidget()
        self.zoomTab.setObjectName("zoomTab")
        self.v3 = QtWidgets.QVBoxLayout(self.zoomTab)
        self.v3.setObjectName("v3")
        self.autoZoomRegionCheckBox = QtWidgets.QCheckBox(self.zoomTab)
        self.autoZoomRegionCheckBox.setObjectName("autoZoomRegionCheckBox")
        self.v3.addWidget(self.autoZoomRegionCheckBox)
        self.dummy2 = QtWidgets.QLabel(self.zoomTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.dummy2.sizePolicy().hasHeightForWidth())
        self.dummy2.setSizePolicy(sizePolicy)
        self.dummy2.setObjectName("dummy2")
        self.v3.addWidget(self.dummy2)
        self.tabWidget.addTab(self.zoomTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(DisplayOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DisplayOptionsDialog)
        self.tabWidget.setCurrentIndex(2)
        self.buttonBox.accepted.connect(DisplayOptionsDialog.accept)
        self.buttonBox.rejected.connect(DisplayOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DisplayOptionsDialog)

    def retranslateUi(self, DisplayOptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        DisplayOptionsDialog.setWindowTitle(_translate("DisplayOptionsDialog", "Display Options"))
        self.reverseCheckBox.setText(_translate("DisplayOptionsDialog", "Reverse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.colourmapTab), _translate("DisplayOptionsDialog", "Colourmap"))
        self.showTicksAndLabelsCheckBox.setText(_translate("DisplayOptionsDialog", "Show axes ticks and labels"))
        self.label.setText(_translate("DisplayOptionsDialog", "Title"))
        self.showProjectFilenameCheckBox.setText(_translate("DisplayOptionsDialog", "Show project filename (bottom left)"))
        self.showDateCheckBox.setText(_translate("DisplayOptionsDialog", "Show date (bottom right)"))
        self.useScaleCheckBox.setText(_translate("DisplayOptionsDialog", "Use physical scale"))
        self.pixelSizeLabel.setText(_translate("DisplayOptionsDialog", "Pixel size"))
        self.showScaleBarCheckBox.setText(_translate("DisplayOptionsDialog", "Show scale bar"))
        self.scaleBarLocationGroupBox.setTitle(_translate("DisplayOptionsDialog", "Scale bar location"))
        self.upperLeftRadioButton.setText(_translate("DisplayOptionsDialog", "Upper left"))
        self.upperRightRadioButton.setText(_translate("DisplayOptionsDialog", "Upper right"))
        self.lowerLeftRadioButton.setText(_translate("DisplayOptionsDialog", "Lower left"))
        self.lowerRightRadioButton.setText(_translate("DisplayOptionsDialog", "Lower right"))
        self.scaleBarColourGroupBox.setTitle(_translate("DisplayOptionsDialog", "Scale bar colour"))
        self.blackRadioButton.setText(_translate("DisplayOptionsDialog", "Black"))
        self.whiteRadioButton.setText(_translate("DisplayOptionsDialog", "White"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.labelsAndScaleTab), _translate("DisplayOptionsDialog", "Labels and scale"))
        self.fixedBinCountGroupBox.setTitle(_translate("DisplayOptionsDialog", "Fixed bin count"))
        self.label_2.setText(_translate("DisplayOptionsDialog", "Number of bins"))
        self.fixedBinWidthGroupBox.setTitle(_translate("DisplayOptionsDialog", "Fixed bin width"))
        self.label_2a.setText(_translate("DisplayOptionsDialog", "Bin width"))
        self.label_2b.setText(_translate("DisplayOptionsDialog", "Maximum number of bins"))
        self.showMeanMedianStdCheckBox.setText(_translate("DisplayOptionsDialog", "Show mean, median and standard deviation lines"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.histogramTab), _translate("DisplayOptionsDialog", "Histogram"))
        self.autoZoomRegionCheckBox.setText(_translate("DisplayOptionsDialog", "Auto zoom to selected region"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zoomTab), _translate("DisplayOptionsDialog", "Zoom"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DisplayOptionsDialog = QtWidgets.QDialog()
    ui = Ui_DisplayOptionsDialog()
    ui.setupUi(DisplayOptionsDialog)
    DisplayOptionsDialog.show()
    sys.exit(app.exec_())

