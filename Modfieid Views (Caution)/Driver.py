# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Driver.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(556, 422)
        self.DriverName_label = QtWidgets.QLabel(Dialog)
        self.DriverName_label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.DriverName_label.setObjectName("DriverName_label")
        self.IDnumber_label = QtWidgets.QLabel(Dialog)
        self.IDnumber_label.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.IDnumber_label.setObjectName("IDnumber_label")
        self.IdExpiryDateLabel = QtWidgets.QLabel(Dialog)
        self.IdExpiryDateLabel.setGeometry(QtCore.QRect(230, 60, 61, 16))
        self.IdExpiryDateLabel.setObjectName("IdExpiryDateLabel")
        self.Certification_label = QtWidgets.QLabel(Dialog)
        self.Certification_label.setGeometry(QtCore.QRect(20, 140, 61, 16))
        self.Certification_label.setObjectName("Certification_label")
        self.PhoneLabel = QtWidgets.QLabel(Dialog)
        self.PhoneLabel.setGeometry(QtCore.QRect(20, 180, 47, 13))
        self.PhoneLabel.setObjectName("PhoneLabel")
        self.LisenceNumberLabel = QtWidgets.QLabel(Dialog)
        self.LisenceNumberLabel.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.LisenceNumberLabel.setObjectName("LisenceNumberLabel")
        self.LisenceExpiryDateLabel = QtWidgets.QLabel(Dialog)
        self.LisenceExpiryDateLabel.setGeometry(QtCore.QRect(230, 100, 61, 16))
        self.LisenceExpiryDateLabel.setObjectName("LisenceExpiryDateLabel")
        self.AgreementType_label = QtWidgets.QLabel(Dialog)
        self.AgreementType_label.setGeometry(QtCore.QRect(20, 220, 81, 16))
        self.AgreementType_label.setObjectName("AgreementType_label")
        self.Email_label = QtWidgets.QLabel(Dialog)
        self.Email_label.setGeometry(QtCore.QRect(190, 180, 31, 16))
        self.Email_label.setObjectName("Email_label")
        self.DataStartService_label = QtWidgets.QLabel(Dialog)
        self.DataStartService_label.setGeometry(QtCore.QRect(20, 290, 91, 16))
        self.DataStartService_label.setObjectName("DataStartService_label")
        self.Fees_label = QtWidgets.QLabel(Dialog)
        self.Fees_label.setGeometry(QtCore.QRect(20, 260, 61, 16))
        self.Fees_label.setObjectName("Fees_label")
        self.EditData_button = QtWidgets.QPushButton(Dialog)
        self.EditData_button.setEnabled(False)
        self.EditData_button.setGeometry(QtCore.QRect(170, 390, 91, 23))
        self.EditData_button.setObjectName("EditData_button")
        self.ArchiveData_button = QtWidgets.QPushButton(Dialog)
        self.ArchiveData_button.setEnabled(False)
        self.ArchiveData_button.setGeometry(QtCore.QRect(320, 390, 91, 23))
        self.ArchiveData_button.setObjectName("ArchiveData_button")
        self.UploadLisence_PushButton = QtWidgets.QPushButton(Dialog)
        self.UploadLisence_PushButton.setGeometry(QtCore.QRect(420, 100, 101, 23))
        self.UploadLisence_PushButton.setObjectName("UploadLisence_PushButton")
        self.UploadDocumentId_PushButton = QtWidgets.QPushButton(Dialog)
        self.UploadDocumentId_PushButton.setGeometry(QtCore.QRect(420, 60, 101, 23))
        self.UploadDocumentId_PushButton.setObjectName("UploadDocumentId_PushButton")
        self.UploadCertification_PushButton = QtWidgets.QPushButton(Dialog)
        self.UploadCertification_PushButton.setGeometry(QtCore.QRect(100, 140, 111, 23))
        self.UploadCertification_PushButton.setObjectName("UploadCertification_PushButton")
        self.AgreementType_combobox = QtWidgets.QComboBox(Dialog)
        self.AgreementType_combobox.setGeometry(QtCore.QRect(118, 220, 91, 22))
        self.AgreementType_combobox.setEditable(True)
        self.AgreementType_combobox.setObjectName("AgreementType_combobox")
        self.AgreementType_combobox.addItem("")
        self.AgreementType_combobox.addItem("")
        self.AgreementType_combobox.addItem("")
        self.AgreementType_combobox.addItem("")
        self.UploadAgreementType_PushButton = QtWidgets.QPushButton(Dialog)
        self.UploadAgreementType_PushButton.setGeometry(QtCore.QRect(230, 220, 121, 23))
        self.UploadAgreementType_PushButton.setObjectName("UploadAgreementType_PushButton")
        self.DriverName_text = QtWidgets.QLineEdit(Dialog)
        self.DriverName_text.setGeometry(QtCore.QRect(100, 20, 121, 20))
        self.DriverName_text.setObjectName("DriverName_text")
        self.IDnumber_text = QtWidgets.QLineEdit(Dialog)
        self.IDnumber_text.setGeometry(QtCore.QRect(100, 60, 121, 20))
        self.IDnumber_text.setInputMethodHints(QtCore.Qt.ImhNone)
        self.IDnumber_text.setObjectName("IDnumber_text")
        self.LisenceNumberText = QtWidgets.QLineEdit(Dialog)
        self.LisenceNumberText.setGeometry(QtCore.QRect(100, 100, 121, 20))
        self.LisenceNumberText.setMaxLength(14)
        self.LisenceNumberText.setObjectName("LisenceNumberText")
        self.PhoneText = QtWidgets.QLineEdit(Dialog)
        self.PhoneText.setGeometry(QtCore.QRect(70, 180, 101, 20))
        self.PhoneText.setObjectName("PhoneText")
        self.Emai_text = QtWidgets.QLineEdit(Dialog)
        self.Emai_text.setGeometry(QtCore.QRect(230, 180, 121, 20))
        self.Emai_text.setObjectName("Emai_text")
        self.Fees_text = QtWidgets.QLineEdit(Dialog)
        self.Fees_text.setGeometry(QtCore.QRect(120, 260, 91, 20))
        self.Fees_text.setObjectName("Fees_text")
        self.Save_button = QtWidgets.QPushButton(Dialog)
        self.Save_button.setGeometry(QtCore.QRect(170, 350, 91, 23))
        self.Save_button.setObjectName("Save_button")
        self.DriverIDExpiryDateEdit = QtWidgets.QDateEdit(Dialog)
        self.DriverIDExpiryDateEdit.setGeometry(QtCore.QRect(300, 60, 110, 22))
        self.DriverIDExpiryDateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DriverIDExpiryDateEdit.setCalendarPopup(True)
        self.DriverIDExpiryDateEdit.setObjectName("DriverIDExpiryDateEdit")
        self.LisenceNumberDateEdit = QtWidgets.QDateEdit(Dialog)
        self.LisenceNumberDateEdit.setGeometry(QtCore.QRect(300, 100, 110, 22))
        self.LisenceNumberDateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.LisenceNumberDateEdit.setCalendarPopup(True)
        self.LisenceNumberDateEdit.setObjectName("LisenceNumberDateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(120, 290, 91, 22))
        self.dateEdit_2.setMinimumDate(QtCore.QDate(2019, 9, 14))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.ViewAgreementDocument_PushButton = QtWidgets.QPushButton(Dialog)
        self.ViewAgreementDocument_PushButton.setGeometry(QtCore.QRect(230, 220, 121, 23))
        self.ViewAgreementDocument_PushButton.setObjectName("ViewAgreementDocument_PushButton")
        self.ViewCertification_PushButton = QtWidgets.QPushButton(Dialog)
        self.ViewCertification_PushButton.setGeometry(QtCore.QRect(100, 140, 111, 23))
        self.ViewCertification_PushButton.setObjectName("ViewCertification_PushButton")
        self.ViewLisence_PushButton = QtWidgets.QPushButton(Dialog)
        self.ViewLisence_PushButton.setGeometry(QtCore.QRect(420, 100, 101, 23))
        self.ViewLisence_PushButton.setObjectName("ViewLisence_PushButton")
        self.ViewIDDocument_PushButton = QtWidgets.QPushButton(Dialog)
        self.ViewIDDocument_PushButton.setGeometry(QtCore.QRect(420, 60, 101, 23))
        self.ViewIDDocument_PushButton.setObjectName("ViewIDDocument_PushButton")
        self.GenerateReport_PushButton = QtWidgets.QPushButton(Dialog)
        self.GenerateReport_PushButton.setGeometry(QtCore.QRect(320, 350, 91, 23))
        self.GenerateReport_PushButton.setObjectName("GenerateReport_PushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.DriverName_label.setText(_translate("Dialog", "Driver Name"))
        self.IDnumber_label.setText(_translate("Dialog", "ID number"))
        self.IdExpiryDateLabel.setText(_translate("Dialog", "Expiry Date"))
        self.Certification_label.setText(_translate("Dialog", "Certification"))
        self.PhoneLabel.setText(_translate("Dialog", "Phone"))
        self.LisenceNumberLabel.setText(_translate("Dialog", "Lisence Number"))
        self.LisenceExpiryDateLabel.setText(_translate("Dialog", "Expiry Date"))
        self.AgreementType_label.setText(_translate("Dialog", "Agreement Type"))
        self.Email_label.setText(_translate("Dialog", "Email"))
        self.DataStartService_label.setText(_translate("Dialog", "Data Start Service"))
        self.Fees_label.setText(_translate("Dialog", "Fees"))
        self.EditData_button.setText(_translate("Dialog", "Edit Data"))
        self.ArchiveData_button.setText(_translate("Dialog", "Archive Data"))
        self.UploadLisence_PushButton.setText(_translate("Dialog", "Attach Document "))
        self.UploadDocumentId_PushButton.setText(_translate("Dialog", "Attach Document "))
        self.UploadCertification_PushButton.setText(_translate("Dialog", "Attach Document "))
        self.AgreementType_combobox.setItemText(0, _translate("Dialog", "Daily"))
        self.AgreementType_combobox.setItemText(1, _translate("Dialog", "Monthly"))
        self.AgreementType_combobox.setItemText(2, _translate("Dialog", "Per Shift"))
        self.AgreementType_combobox.setItemText(3, _translate("Dialog", "Revenue Sharing"))
        self.UploadAgreementType_PushButton.setText(_translate("Dialog", "Attach Document "))
        self.DriverName_text.setPlaceholderText(_translate("Dialog", "ex.Ahmed Younes"))
        self.IDnumber_text.setPlaceholderText(_translate("Dialog", " 14 Digtial of ID number"))
        self.LisenceNumberText.setPlaceholderText(_translate("Dialog", " 14 Digtial of Lisence"))
        self.PhoneText.setPlaceholderText(_translate("Dialog", "01123456514"))
        self.Emai_text.setPlaceholderText(_translate("Dialog", "Example@gmail.com"))
        self.Fees_text.setPlaceholderText(_translate("Dialog", "5000 L.E"))
        self.Save_button.setText(_translate("Dialog", "Save"))
        self.ViewAgreementDocument_PushButton.setText(_translate("Dialog", "View Document "))
        self.ViewCertification_PushButton.setText(_translate("Dialog", "View Document "))
        self.ViewLisence_PushButton.setText(_translate("Dialog", "View Document "))
        self.ViewIDDocument_PushButton.setText(_translate("Dialog", "View Document "))
        self.GenerateReport_PushButton.setText(_translate("Dialog", "Generate Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

