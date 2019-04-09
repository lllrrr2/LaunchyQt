# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcy.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CalcyOption(object):
    def setupUi(self, CalcyOption):
        CalcyOption.setObjectName("CalcyOption")
        CalcyOption.resize(516, 262)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(CalcyOption)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(CalcyOption)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tabOutput = QtWidgets.QWidget()
        self.tabOutput.setObjectName("tabOutput")
        self.formLayout = QtWidgets.QFormLayout(self.tabOutput)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabOutput)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radioButtonDecSepSystem = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonDecSepSystem.setChecked(True)
        self.radioButtonDecSepSystem.setObjectName("radioButtonDecSepSystem")
        self.verticalLayout_6.addWidget(self.radioButtonDecSepSystem)
        self.radioButtonDecSepComa = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonDecSepComa.setObjectName("radioButtonDecSepComa")
        self.verticalLayout_6.addWidget(self.radioButtonDecSepComa)
        self.radioButtonDecSepDot = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButtonDecSepDot.setObjectName("radioButtonDecSepDot")
        self.verticalLayout_6.addWidget(self.radioButtonDecSepDot)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.tabOutput)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.spinBoxOutputPrecision = QtWidgets.QSpinBox(self.tabOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxOutputPrecision.sizePolicy().hasHeightForWidth())
        self.spinBoxOutputPrecision.setSizePolicy(sizePolicy)
        self.spinBoxOutputPrecision.setMinimumSize(QtCore.QSize(55, 0))
        self.spinBoxOutputPrecision.setMaximumSize(QtCore.QSize(60, 30))
        self.spinBoxOutputPrecision.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxOutputPrecision.setMinimum(1)
        self.spinBoxOutputPrecision.setMaximum(10)
        self.spinBoxOutputPrecision.setProperty("value", 3)
        self.spinBoxOutputPrecision.setObjectName("spinBoxOutputPrecision")
        self.horizontalLayout_3.addWidget(self.spinBoxOutputPrecision)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.checkBoxShowGrpSep = QtWidgets.QCheckBox(self.tabOutput)
        self.checkBoxShowGrpSep.setChecked(False)
        self.checkBoxShowGrpSep.setObjectName("checkBoxShowGrpSep")
        self.verticalLayout_4.addWidget(self.checkBoxShowGrpSep)
        self.checkBoxCopyToClipboard = QtWidgets.QCheckBox(self.tabOutput)
        self.checkBoxCopyToClipboard.setChecked(True)
        self.checkBoxCopyToClipboard.setObjectName("checkBoxCopyToClipboard")
        self.verticalLayout_4.addWidget(self.checkBoxCopyToClipboard)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_5)
        self.tabWidget.addTab(self.tabOutput, "")
        self.tabRadix = QtWidgets.QWidget()
        self.tabRadix.setObjectName("tabRadix")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tabRadix)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabRadix)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBoxBinOut = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxBinOut.setChecked(True)
        self.checkBoxBinOut.setObjectName("checkBoxBinOut")
        self.horizontalLayout.addWidget(self.checkBoxBinOut)
        self.checkBoxOctOut = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxOctOut.setChecked(True)
        self.checkBoxOctOut.setObjectName("checkBoxOctOut")
        self.horizontalLayout.addWidget(self.checkBoxOctOut)
        self.checkBoxHexOut = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxHexOut.setChecked(True)
        self.checkBoxHexOut.setObjectName("checkBoxHexOut")
        self.horizontalLayout.addWidget(self.checkBoxHexOut)
        self.checkBoxSizeOut = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxSizeOut.setChecked(True)
        self.checkBoxSizeOut.setObjectName("checkBoxSizeOut")
        self.horizontalLayout.addWidget(self.checkBoxSizeOut)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxShowBasePrefix = QtWidgets.QCheckBox(self.tabRadix)
        self.checkBoxShowBasePrefix.setChecked(True)
        self.checkBoxShowBasePrefix.setObjectName("checkBoxShowBasePrefix")
        self.verticalLayout.addWidget(self.checkBoxShowBasePrefix)
        self.checkBoxShowLeadingZerosBin = QtWidgets.QCheckBox(self.tabRadix)
        self.checkBoxShowLeadingZerosBin.setChecked(True)
        self.checkBoxShowLeadingZerosBin.setObjectName("checkBoxShowLeadingZerosBin")
        self.verticalLayout.addWidget(self.checkBoxShowLeadingZerosBin)
        self.checkBoxShowLeadingZerosOct = QtWidgets.QCheckBox(self.tabRadix)
        self.checkBoxShowLeadingZerosOct.setChecked(True)
        self.checkBoxShowLeadingZerosOct.setObjectName("checkBoxShowLeadingZerosOct")
        self.verticalLayout.addWidget(self.checkBoxShowLeadingZerosOct)
        self.checkBoxShowLeadingZerosHex = QtWidgets.QCheckBox(self.tabRadix)
        self.checkBoxShowLeadingZerosHex.setChecked(True)
        self.checkBoxShowLeadingZerosHex.setObjectName("checkBoxShowLeadingZerosHex")
        self.verticalLayout.addWidget(self.checkBoxShowLeadingZerosHex)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBoxBW = QtWidgets.QGroupBox(self.tabRadix)
        self.groupBoxBW.setObjectName("groupBoxBW")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBoxBW)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButtonBW64 = QtWidgets.QRadioButton(self.groupBoxBW)
        self.radioButtonBW64.setObjectName("radioButtonBW64")
        self.horizontalLayout_5.addWidget(self.radioButtonBW64)
        self.radioButtonBW32 = QtWidgets.QRadioButton(self.groupBoxBW)
        self.radioButtonBW32.setObjectName("radioButtonBW32")
        self.horizontalLayout_5.addWidget(self.radioButtonBW32)
        self.radioButtonBW16 = QtWidgets.QRadioButton(self.groupBoxBW)
        self.radioButtonBW16.setChecked(True)
        self.radioButtonBW16.setObjectName("radioButtonBW16")
        self.horizontalLayout_5.addWidget(self.radioButtonBW16)
        self.radioButtonBW8 = QtWidgets.QRadioButton(self.groupBoxBW)
        self.radioButtonBW8.setObjectName("radioButtonBW8")
        self.horizontalLayout_5.addWidget(self.radioButtonBW8)
        self.verticalLayout_2.addWidget(self.groupBoxBW)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tabRadix, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(CalcyOption)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CalcyOption)

    def retranslateUi(self, CalcyOption):
        _translate = QtCore.QCoreApplication.translate
        CalcyOption.setWindowTitle(_translate("CalcyOption", "CalcyPy - Simple calculator"))
        self.groupBox_2.setTitle(_translate("CalcyOption", "Decimal point and group separator"))
        self.radioButtonDecSepSystem.setToolTip(_translate("CalcyOption", "Use system locale settings"))
        self.radioButtonDecSepSystem.setText(_translate("CalcyOption", "System default"))
        self.radioButtonDecSepComa.setText(_translate("CalcyOption", "Coma as decimal point and dot as group separator"))
        self.radioButtonDecSepDot.setText(_translate("CalcyOption", "Dot as decimal point and coma as group separator"))
        self.label.setText(_translate("CalcyOption", "Decimal output Precision"))
        self.spinBoxOutputPrecision.setToolTip(_translate("CalcyOption", "<html><head/><body><p>Sets the maximal number of digits</p></body></html>"))
        self.checkBoxShowGrpSep.setText(_translate("CalcyOption", "Show group separator in result"))
        self.checkBoxCopyToClipboard.setToolTip(_translate("CalcyOption", "If this option is enabled, pressing enter key will copy calculation result to clipboard."))
        self.checkBoxCopyToClipboard.setText(_translate("CalcyOption", "Use Enter key to Copy result to Clipboard"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOutput), _translate("CalcyOption", "General"))
        self.groupBox_3.setTitle(_translate("CalcyOption", "Show result as"))
        self.checkBoxBinOut.setText(_translate("CalcyOption", "Bin"))
        self.checkBoxOctOut.setText(_translate("CalcyOption", "Oct"))
        self.checkBoxHexOut.setText(_translate("CalcyOption", "Hex"))
        self.checkBoxSizeOut.setText(_translate("CalcyOption", "Size"))
        self.checkBoxShowBasePrefix.setToolTip(_translate("CalcyOption", "Show prefix for given number base in results (i.e. \"0x\" for hexadecimal numbers)"))
        self.checkBoxShowBasePrefix.setText(_translate("CalcyOption", "Show base prefix in result"))
        self.checkBoxShowLeadingZerosBin.setText(_translate("CalcyOption", "Show leading zeros in bin output"))
        self.checkBoxShowLeadingZerosOct.setText(_translate("CalcyOption", "Show leading zeros in oct output"))
        self.checkBoxShowLeadingZerosHex.setText(_translate("CalcyOption", "Show leading zeros in hex output"))
        self.groupBoxBW.setTitle(_translate("CalcyOption", "Calculation bit width"))
        self.radioButtonBW64.setText(_translate("CalcyOption", "64"))
        self.radioButtonBW32.setText(_translate("CalcyOption", "32"))
        self.radioButtonBW16.setText(_translate("CalcyOption", "16"))
        self.radioButtonBW8.setText(_translate("CalcyOption", "8"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRadix), _translate("CalcyOption", "Radix"))

