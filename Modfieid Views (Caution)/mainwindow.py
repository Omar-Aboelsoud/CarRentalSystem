# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 299)
        self.Vehicle_button = QtWidgets.QPushButton(Dialog)
        self.Vehicle_button.setGeometry(QtCore.QRect(210, 80, 161, 51))
        self.Vehicle_button.setObjectName("Vehicle_button")
        self.Client_button = QtWidgets.QPushButton(Dialog)
        self.Client_button.setGeometry(QtCore.QRect(10, 80, 161, 51))
        self.Client_button.setObjectName("Client_button")
        self.Activity_button = QtWidgets.QPushButton(Dialog)
        self.Activity_button.setGeometry(QtCore.QRect(10, 10, 161, 51))
        self.Activity_button.setObjectName("Activity_button")
        self.Driver_button = QtWidgets.QPushButton(Dialog)
        self.Driver_button.setGeometry(QtCore.QRect(210, 10, 161, 51))
        self.Driver_button.setObjectName("Driver_button")
        self.Alerts_button = QtWidgets.QPushButton(Dialog)
        self.Alerts_button.setGeometry(QtCore.QRect(10, 160, 161, 51))
        self.Alerts_button.setObjectName("Alerts_button")
        self.GenerateReport_button = QtWidgets.QPushButton(Dialog)
        self.GenerateReport_button.setGeometry(QtCore.QRect(210, 160, 161, 51))
        self.GenerateReport_button.setObjectName("GenerateReport_button")
        self.LoadOldData_button = QtWidgets.QPushButton(Dialog)
        self.LoadOldData_button.setGeometry(QtCore.QRect(210, 230, 161, 51))
        self.LoadOldData_button.setObjectName("LoadOldData_button")
        self.VendorOldData_button = QtWidgets.QPushButton(Dialog)
        self.VendorOldData_button.setGeometry(QtCore.QRect(10, 230, 161, 51))
        self.VendorOldData_button.setObjectName("VendorOldData_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Vehicle_button.setText(_translate("Dialog", "Vehicle "))
        self.Client_button.setText(_translate("Dialog", "Client"))
        self.Activity_button.setText(_translate("Dialog", "Activity"))
        self.Driver_button.setText(_translate("Dialog", "Driver"))
        self.Alerts_button.setText(_translate("Dialog", "Alerts"))
        self.GenerateReport_button.setText(_translate("Dialog", "Generate Report"))
        self.LoadOldData_button.setText(_translate("Dialog", "Load Open Balance"))
        self.VendorOldData_button.setText(_translate("Dialog", "Vendor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

