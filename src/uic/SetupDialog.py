# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SetupDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetupDialog(object):
    def setupUi(self, SetupDialog):
        SetupDialog.setObjectName("SetupDialog")
        SetupDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SetupDialog.resize(330, 149)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SetupDialog.sizePolicy().hasHeightForWidth())
        SetupDialog.setSizePolicy(sizePolicy)
        SetupDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        SetupDialog.setWindowTitle("Setup")
        SetupDialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(SetupDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.MachineLineEdit = QtWidgets.QLineEdit(SetupDialog)
        self.MachineLineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.MachineLineEdit.setObjectName("MachineLineEdit")
        self.gridLayout.addWidget(self.MachineLineEdit, 3, 2, 1, 1)
        self.roasterSizeDoubleSpinBox = QtWidgets.QDoubleSpinBox(SetupDialog)
        self.roasterSizeDoubleSpinBox.setToolTip("The maximum nominal batch size of the machine in kg")
        self.roasterSizeDoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roasterSizeDoubleSpinBox.setPrefix("")
        self.roasterSizeDoubleSpinBox.setSuffix("kg")
        self.roasterSizeDoubleSpinBox.setDecimals(1)
        self.roasterSizeDoubleSpinBox.setMaximum(9999.9)
        self.roasterSizeDoubleSpinBox.setObjectName("roasterSizeDoubleSpinBox")
        self.gridLayout.addWidget(self.roasterSizeDoubleSpinBox, 3, 3, 1, 1)
        self.labelMachine = QtWidgets.QLabel(SetupDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelMachine.setFont(font)
        self.labelMachine.setText("Machine")
        self.labelMachine.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelMachine.setObjectName("labelMachine")
        self.gridLayout.addWidget(self.labelMachine, 3, 0, 1, 1)
        self.labelOrganization = QtWidgets.QLabel(SetupDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelOrganization.setFont(font)
        self.labelOrganization.setText("Organization")
        self.labelOrganization.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelOrganization.setObjectName("labelOrganization")
        self.gridLayout.addWidget(self.labelOrganization, 1, 0, 1, 1)
        self.labelOperator = QtWidgets.QLabel(SetupDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelOperator.setFont(font)
        self.labelOperator.setText("Operator")
        self.labelOperator.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelOperator.setObjectName("labelOperator")
        self.gridLayout.addWidget(self.labelOperator, 2, 0, 1, 1)
        self.OrganizationLineEdit = QtWidgets.QLineEdit(SetupDialog)
        self.OrganizationLineEdit.setObjectName("OrganizationLineEdit")
        self.gridLayout.addWidget(self.OrganizationLineEdit, 1, 2, 1, 2)
        self.OperatorLineEdit = QtWidgets.QLineEdit(SetupDialog)
        self.OperatorLineEdit.setObjectName("OperatorLineEdit")
        self.gridLayout.addWidget(self.OperatorLineEdit, 2, 2, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SetupDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(SetupDialog)
        QtCore.QMetaObject.connectSlotsByName(SetupDialog)
        SetupDialog.setTabOrder(self.OrganizationLineEdit, self.OperatorLineEdit)
        SetupDialog.setTabOrder(self.OperatorLineEdit, self.MachineLineEdit)
        SetupDialog.setTabOrder(self.MachineLineEdit, self.roasterSizeDoubleSpinBox)

    def retranslateUi(self, SetupDialog):
        pass
