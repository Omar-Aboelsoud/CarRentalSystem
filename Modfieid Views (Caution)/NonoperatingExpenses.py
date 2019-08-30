# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NonoperatingExpenses.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 269)
        self.TypeOfExpenseLabel = QtWidgets.QLabel(Dialog)
        self.TypeOfExpenseLabel.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.TypeOfExpenseLabel.setObjectName("TypeOfExpenseLabel")
        self.TypeOfExpenseComboBox = QtWidgets.QComboBox(Dialog)
        self.TypeOfExpenseComboBox.setGeometry(QtCore.QRect(120, 20, 131, 22))
        self.TypeOfExpenseComboBox.setEditable(True)
        self.TypeOfExpenseComboBox.setObjectName("TypeOfExpenseComboBox")
        self.TypeOfExpenseComboBox.addItem("")
        self.TypeOfExpenseComboBox.addItem("")
        self.TypeOfExpenseComboBox.addItem("")
        self.TypeOfExpenseComboBox.addItem("")
        self.NameOfVendorLabel = QtWidgets.QLabel(Dialog)
        self.NameOfVendorLabel.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.NameOfVendorLabel.setObjectName("NameOfVendorLabel")
        self.NameOfVendorComboBox = QtWidgets.QComboBox(Dialog)
        self.NameOfVendorComboBox.setGeometry(QtCore.QRect(120, 60, 131, 22))
        self.NameOfVendorComboBox.setEditable(True)
        self.NameOfVendorComboBox.setObjectName("NameOfVendorComboBox")
        self.ExpenesesDescription = QtWidgets.QLabel(Dialog)
        self.ExpenesesDescription.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.ExpenesesDescription.setObjectName("ExpenesesDescription")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(120, 140, 141, 71))
        self.textEdit.setObjectName("textEdit")
        self.Save_PushButton = QtWidgets.QPushButton(Dialog)
        self.Save_PushButton.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.Save_PushButton.setObjectName("Save_PushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 100, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.GenerateReport_PushButton = QtWidgets.QPushButton(Dialog)
        self.GenerateReport_PushButton.setGeometry(QtCore.QRect(200, 230, 91, 23))
        self.GenerateReport_PushButton.setObjectName("GenerateReport_PushButton")
        self.UploadDocument_PushButton = QtWidgets.QPushButton(Dialog)
        self.UploadDocument_PushButton.setGeometry(QtCore.QRect(280, 100, 101, 23))
        self.UploadDocument_PushButton.setObjectName("UploadDocument_PushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.TypeOfExpenseLabel.setText(_translate("Dialog", "Type of Expenses"))
        self.TypeOfExpenseComboBox.setItemText(0, _translate("Dialog", "3d Party Car Owner"))
        self.TypeOfExpenseComboBox.setItemText(1, _translate("Dialog", "Insurance"))
        self.TypeOfExpenseComboBox.setItemText(2, _translate("Dialog", "Maintaince Center"))
        self.TypeOfExpenseComboBox.setItemText(3, _translate("Dialog", "Govermental"))
        self.NameOfVendorLabel.setText(_translate("Dialog", "Name of Vendor"))
        self.ExpenesesDescription.setText(_translate("Dialog", "Expense Description"))
        self.Save_PushButton.setText(_translate("Dialog", "Save"))
        self.label_4.setText(_translate("Dialog", "Paid Expense"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "50 L.E"))
        self.GenerateReport_PushButton.setText(_translate("Dialog", "Generate Report"))
        self.UploadDocument_PushButton.setText(_translate("Dialog", "Upload Document"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

