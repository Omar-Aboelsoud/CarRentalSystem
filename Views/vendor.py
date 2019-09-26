# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vendor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Vendor(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 240)
        self.VendorNameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.VendorNameLineEdit.setGeometry(QtCore.QRect(100, 20, 121, 20))
        self.VendorNameLineEdit.setObjectName("VendorNameLineEdit")
        self.PhoneLineEdit = QtWidgets.QLineEdit(Dialog)
        self.PhoneLineEdit.setGeometry(QtCore.QRect(100, 50, 121, 20))
        self.PhoneLineEdit.setObjectName("PhoneLineEdit")
        self.ContactPersonLineEdit = QtWidgets.QLineEdit(Dialog)
        self.ContactPersonLineEdit.setGeometry(QtCore.QRect(100, 80, 121, 20))
        self.ContactPersonLineEdit.setObjectName("ContactPersonLineEdit")
        self.VendorNameLabel = QtWidgets.QLabel(Dialog)
        self.VendorNameLabel.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.VendorNameLabel.setObjectName("VendorNameLabel")
        self.PhoneLabel = QtWidgets.QLabel(Dialog)
        self.PhoneLabel.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.PhoneLabel.setObjectName("PhoneLabel")
        self.ContactPerson = QtWidgets.QLabel(Dialog)
        self.ContactPerson.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.ContactPerson.setObjectName("ContactPerson")
        self.TypeofVendorcomboBox = QtWidgets.QComboBox(Dialog)
        self.TypeofVendorcomboBox.setGeometry(QtCore.QRect(100, 120, 121, 22))
        self.TypeofVendorcomboBox.setEditable(True)
        self.TypeofVendorcomboBox.setObjectName("TypeofVendorcomboBox")
        self.TypeofVendorcomboBox.addItem("")
        self.TypeofVendorcomboBox.addItem("")
        self.TypeofVendorcomboBox.addItem("")
        self.TypeofVendorcomboBox.addItem("")
        self.TypeofVendorcomboBox.addItem("")
        self.TypeofVendorcomboBox.addItem("")
        self.TypeOfVendorLabel = QtWidgets.QLabel(Dialog)
        self.TypeOfVendorLabel.setGeometry(QtCore.QRect(10, 120, 81, 16))
        self.TypeOfVendorLabel.setObjectName("TypeOfVendorLabel")
        self.EditData_button = QtWidgets.QPushButton(Dialog)
        self.EditData_button.setEnabled(False)
        self.EditData_button.setGeometry(QtCore.QRect(50, 200, 61, 23))
        self.EditData_button.setObjectName("EditData_button")
        self.GenerateReport_PushButton = QtWidgets.QPushButton(Dialog)
        self.GenerateReport_PushButton.setGeometry(QtCore.QRect(130, 170, 91, 23))
        self.GenerateReport_PushButton.setObjectName("GenerateReport_PushButton")
        self.ArchiveData_button = QtWidgets.QPushButton(Dialog)
        self.ArchiveData_button.setEnabled(False)
        self.ArchiveData_button.setGeometry(QtCore.QRect(130, 200, 91, 23))
        self.ArchiveData_button.setObjectName("ArchiveData_button")
        self.Save_button = QtWidgets.QPushButton(Dialog)
        self.Save_button.setGeometry(QtCore.QRect(50, 170, 61, 23))
        self.Save_button.setObjectName("Save_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Vendor"))
        self.VendorNameLineEdit.setPlaceholderText(_translate("Dialog", "Ex.Naser Center"))
        self.PhoneLineEdit.setPlaceholderText(_translate("Dialog", "Ex.01234564514"))
        self.ContactPersonLineEdit.setPlaceholderText(_translate("Dialog", "Ex.Mohamed Ahmed"))
        self.VendorNameLabel.setText(_translate("Dialog", "Vendor Name"))
        self.PhoneLabel.setText(_translate("Dialog", "Phone"))
        self.ContactPerson.setText(_translate("Dialog", "Contact Person"))
        self.TypeofVendorcomboBox.setItemText(0, _translate("Dialog", "Driver"))
        self.TypeofVendorcomboBox.setItemText(1, _translate("Dialog", "Goverment"))
        self.TypeofVendorcomboBox.setItemText(2, _translate("Dialog", "Maintaince Center"))
        self.TypeofVendorcomboBox.setItemText(3, _translate("Dialog", "Spare Parts"))
        self.TypeofVendorcomboBox.setItemText(4, _translate("Dialog", "3rd party car owner"))
        self.TypeofVendorcomboBox.setItemText(5, _translate("Dialog", "Insurance"))
        self.TypeOfVendorLabel.setText(_translate("Dialog", "Type Of Vendor"))
        self.EditData_button.setText(_translate("Dialog", "Edit Data"))
        self.GenerateReport_PushButton.setText(_translate("Dialog", "Generate Report"))
        self.ArchiveData_button.setText(_translate("Dialog", "Archive Data"))
        self.Save_button.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    def run():
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Vendor()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()
    run()

