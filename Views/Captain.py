# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Captian.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from RentalCarCommen import RentalCarCommonUi
from RentalCarCaptainDatabase import RentalCarCaptaindb
class Ui_Captian(object):
    def __init__(self):
        self._RentalCarCommonUi=RentalCarCommonUi()
        self.RentalCarCaptaindb=RentalCarCaptaindb()
        self.AgreementTypeImagePath=None
        self.DocumentIdImagePath=None
        self.CertificationImagePath=[]
        self.LisenceImagePath=None
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(556, 422)
        self.CaptianName_label = QtWidgets.QLabel(Dialog)
        self.CaptianName_label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.CaptianName_label.setObjectName("CaptianName_label")
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
        self.AgreementType_combobox.addItem("")
        self.UploadAgreementType_PushButton = QtWidgets.QPushButton(Dialog)
        self.UploadAgreementType_PushButton.setGeometry(QtCore.QRect(230, 220, 121, 23))
        self.UploadAgreementType_PushButton.setObjectName("UploadAgreementType_PushButton")
        self.CaptianName_text = QtWidgets.QLineEdit(Dialog)
        self.CaptianName_text.setGeometry(QtCore.QRect(100, 20, 121, 20))
        self.CaptianName_text.setObjectName("CaptianName_text")
        self.IDnumber_text = QtWidgets.QLineEdit(Dialog)
        self.IDnumber_text.setGeometry(QtCore.QRect(100, 60, 121, 20))
        self.IDnumber_text.setMaxLength(14)
        self.IDnumber_text.setObjectName("IDnumber_text")
        self.LisenceNumberText = QtWidgets.QLineEdit(Dialog)
        self.LisenceNumberText.setGeometry(QtCore.QRect(100, 100, 121, 20))
        self.LisenceNumberText.setMaxLength(14)
        self.LisenceNumberText.setObjectName("LisenceNumberText")
        self.PhoneText = QtWidgets.QLineEdit(Dialog)
        self.PhoneText.setGeometry(QtCore.QRect(70, 180, 101, 20))
        self.PhoneText.setObjectName("PhoneText")
        self.PhoneText.setMaxLength(11)
        self.Email_text = QtWidgets.QLineEdit(Dialog)
        self.Email_text.setGeometry(QtCore.QRect(230, 180, 121, 20))
        self.Email_text.setObjectName("Email_text")
        self.Fees_text = QtWidgets.QLineEdit(Dialog)
        self.Fees_text.setGeometry(QtCore.QRect(120, 260, 91, 20))
        self.Fees_text.setObjectName("Fees_text")
        self.Save_button = QtWidgets.QPushButton(Dialog)
        self.Save_button.setGeometry(QtCore.QRect(170, 350, 91, 23))
        self.Save_button.setObjectName("Save_button")
        self.CaptianIDExpiryDateEdit = QtWidgets.QDateEdit(Dialog)
        self.CaptianIDExpiryDateEdit.setGeometry(QtCore.QRect(300, 60, 110, 22))
        self.CaptianIDExpiryDateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.CaptianIDExpiryDateEdit.setCalendarPopup(True)
        self.CaptianIDExpiryDateEdit.setObjectName("CaptianIDExpiryDateEdit")
        self.LisenceNumberDateEdit = QtWidgets.QDateEdit(Dialog)
        self.LisenceNumberDateEdit.setGeometry(QtCore.QRect(300, 100, 110, 22))
        self.LisenceNumberDateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.LisenceNumberDateEdit.setCalendarPopup(True)
        self.LisenceNumberDateEdit.setObjectName("LisenceNumberDateEdit")
        self.DateStartService = QtWidgets.QDateEdit(Dialog)
        self.DateStartService.setGeometry(QtCore.QRect(120, 290, 91, 22))
        self.DateStartService.setMinimumDate(QtCore.QDate(2019, 9, 14))
        self.DateStartService.setCalendarPopup(True)
        self.DateStartService.setObjectName("DateStartService")
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
        Dialog.setWindowTitle(_translate("Dialog", "Captian"))
        self.CaptianName_label.setText(_translate("Dialog", "Captian Name"))
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
        self.AgreementType_combobox.setItemText(4, _translate("Dialog", "Percentage %"))
        self.UploadAgreementType_PushButton.setText(_translate("Dialog", "Attach Document "))
        self.CaptianName_text.setPlaceholderText(_translate("Dialog", "ex.Ahmed Younes"))
        self.IDnumber_text.setPlaceholderText(_translate("Dialog", " 14 digit of ID number"))
        self.LisenceNumberText.setPlaceholderText(_translate("Dialog", " 14 digit of Lisence"))
        self.PhoneText.setPlaceholderText(_translate("Dialog", "01123456514"))
        self.Email_text.setPlaceholderText(_translate("Dialog", "Example@gmail.com"))
        self.Fees_text.setPlaceholderText(_translate("Dialog", "5000 L.E"))
        self.Save_button.setText(_translate("Dialog", "Save"))
        self.ViewAgreementDocument_PushButton.setText(_translate("Dialog", "View Document "))
        self.ViewCertification_PushButton.setText(_translate("Dialog", "View Document "))
        self.ViewLisence_PushButton.setText(_translate("Dialog", "View Document "))
        self.ViewIDDocument_PushButton.setText(_translate("Dialog", "View Document "))
        self.GenerateReport_PushButton.setText(_translate("Dialog", "Generate Report"))
        
        
        
        #functionCalls
        self.setVisiblityOfButtons()
        self.UploadAgreementType_PushButton.clicked.connect(self.UploadAgreementType)
        self.UploadCertification_PushButton.clicked.connect(self.UploadCertification)       
        self.UploadDocumentId_PushButton.clicked.connect(self.UploadDocumentId)
        self.UploadLisence_PushButton.clicked.connect(self.UploadLisence)
        self.Save_button.clicked.connect(lambda:self.onSaveClick(Dialog))
        
        self.IDnumber_text.returnPressed.connect(lambda: self.IsRecoredExist(self.IDnumber_text.text() , Dialog))
        self.LisenceNumberText.returnPressed.connect(lambda: self.IsRecoredExist(self.LisenceNumberText.text()))
        
        
        self.CaptianName_text.textChanged[str].connect(lambda: self._RentalCarCommonUi.IsEmptyTextbox(self.CaptianName_text))
        self.CaptianName_text.setValidator(self._RentalCarCommonUi.StringRegexValidator)
        self.IDnumber_text.textChanged[str].connect(lambda: self._RentalCarCommonUi.IsLengthofStringVaild(self.IDnumber_text,self._RentalCarCommonUi.MaxLenghtofIDNumber))
        self.IDnumber_text.setValidator(self._RentalCarCommonUi.IntegerRegexValidator)
        self.LisenceNumberText.textChanged[str].connect(lambda: self._RentalCarCommonUi.IsLengthofStringVaild(self.LisenceNumberText,self._RentalCarCommonUi.MaxLenghtofIDNumber))
        self.LisenceNumberText.setValidator(self._RentalCarCommonUi.IntegerRegexValidator)
        self.PhoneText.textChanged[str].connect(lambda: self._RentalCarCommonUi.IsLengthofStringVaild(self.PhoneText,self._RentalCarCommonUi.MaxLengthofPhoneNumber))
        self.PhoneText.setValidator(self._RentalCarCommonUi.IntegerRegexValidator)
        self.Fees_text.textChanged[str].connect(lambda: self._RentalCarCommonUi.IsEmptyTextbox(self.Fees_text))
        self.Fees_text.setValidator(self._RentalCarCommonUi.IntegerRegexValidator)
        self.Email_text.textChanged[str].connect(lambda: self._RentalCarCommonUi.EmailAddressTextStatus(self.Email_text))
        self.Email_text.setValidator(self._RentalCarCommonUi.EmailRegexValidator)
        
        
        
    def ReteriveAndRepresentValues(self,fields):
        
        self.CaptianName_text.setText(fields[1])
        self.IDnumber_text.setText(fields[2])
        self.LisenceNumberText.setText(fields[3])
        self.CaptianIDExpiryDateEdit.setDate(self._RentalCarCommonUi.StringToDate(fields[4]))
        self.LisenceNumberDateEdit.setDate(self._RentalCarCommonUi.StringToDate(fields[5]))
        self.DocumentIdImagePath=fields[6]
        self.LisenceImagePath=fields[7]
#        self.CertificationImagePath=fields[8]
        self.PhoneText.setText(fields[8])
        self.Email_text.setText(fields[9])
        self.AgreementType_combobox.setCurrentText(fields[10])
        self.AgreementTypeImagePath=fields[11]
        self.Fees_text.setText(fields[12])
        self.DateStartService.setDate(self._RentalCarCommonUi.StringToDate(fields[13]))
        
        
    def IsRecoredExist(self,Text,Dialog):
        exist,fields=self.RentalCarCaptaindb.IsRecoredExistCaptain(Text)
        if(exist==True):
            RepersentiviefieldsName=[self.CaptianName_text,self.LisenceNumberDateEdit,self.LisenceNumberText,self.UploadAgreementType_PushButton,
                                     self.UploadCertification_PushButton,self.UploadDocumentId_PushButton,self.UploadLisence_PushButton,
                                     self.CaptianIDExpiryDateEdit,self.PhoneText,self.AgreementType_combobox,self.Fees_text,self.IDnumber_text,
                                     self.Email_text,self.DateStartService]
            self._RentalCarCommonUi.DisableFields(RepersentiviefieldsName)
            self.ReteriveAndRepresentValues(fields)
            self.ShowViewButtons()
        else:
            reply= QMessageBox.information(Dialog, "Messege", "This Captain infomration is not exist", QMessageBox.Ok)
        
    def InsertValuesInCaptainDB(self):
             CaptainName=self.CaptianName_text.text()
             IDNumber=self.IDnumber_text.text()
             LisenceNumber=self.LisenceNumberText.text()
             IDNumberExpiryDate=self.CaptianIDExpiryDateEdit.date().toString("yyyy-MM-dd")
             LisenceNumberExpiryDate=self.LisenceNumberDateEdit.date().toString("yyyy-MM-dd")
             IDnumberImage=self.DocumentIdImagePath
             LisenceNumberImage=self.LisenceImagePath
             CertificationImage=self.CertificationImagePath
             PhoneNumber=self.PhoneText.text()
             Email=self.Email_text.text()
             AgreementType=self.AgreementType_combobox.currentText()
             AgreementTypeImage=self.AgreementTypeImagePath
             Fees=self.Fees_text.text()
             DateofStartService=self.DateStartService.date().toString("yyyy-MM-dd")
             
             values=[CaptainName, IDNumber, LisenceNumber, IDNumberExpiryDate, LisenceNumberExpiryDate, IDnumberImage, LisenceNumberImage, CertificationImage, PhoneNumber, Email, AgreementType, AgreementTypeImage, Fees, DateofStartService]
             valueswithNoNone=self.RentalCarCaptaindb.convertNoneToEmptyString(values)
             self.RentalCarCaptaindb.insertIntoCaptainTable(valueswithNoNone)
#             for i in valueswithNoNone:
#                 print (i) 
             
    def ShowViewButtons(self):
        ViewbuttonsNames=[self.ViewAgreementDocument_PushButton,self.ViewCertification_PushButton,self.ViewIDDocument_PushButton,self.ViewLisence_PushButton]
        self._RentalCarCommonUi.ShowFields(ViewbuttonsNames)    
    def onSaveClick(self,Dialog):
        textBoxeswithCheckboxNames =[self.CaptianName_text,self.IDnumber_text,self.LisenceNumberText,self.PhoneText,self.Fees_text,
                                         self.Email_text]     
        pushButtons=[self.UploadDocumentId_PushButton,self.UploadLisence_PushButton,self.UploadCertification_PushButton,self.UploadAgreementType_PushButton]                        
        imagePaths=[self.DocumentIdImagePath,self.LisenceImagePath,self.CertificationImagePath,self.AgreementTypeImagePath]
        
        self._RentalCarCommonUi.OnClickSaveButton(textBoxeswithCheckboxNames)
        self._RentalCarCommonUi.isEmptyOrNoneImagePath(imagePaths,pushButtons)
            
        if (self._RentalCarCommonUi.bSaveButtonActive==False):
            QMessageBox().about(Dialog,"Error","Please Enter Required Fields")
        else:
            self.InsertValuesInCaptainDB()
            reply= QMessageBox.information(Dialog, "Messege", "Saved Successfully", QMessageBox.Ok)
        
        

   
        
    def setVisiblityOfButtons(self):
        self.ViewAgreementDocument_PushButton.hide()
        self.ViewCertification_PushButton.hide()
        self.ViewIDDocument_PushButton.hide()
        self.ViewLisence_PushButton.hide()
        
    def UploadAgreementType(self):  
        self.AgreementTypeImagePath=self._RentalCarCommonUi.openFileNameDialog()
    def UploadCertification(self):
        fileNames=self._RentalCarCommonUi.openFileNameDialog()
        self.CertificationImagePath.append(fileNames)
        self.CertificationImagePath=self._RentalCarCommonUi.single_list(self.CertificationImagePath)
        print(self.CertificationImagePath)
        
    def UploadDocumentId(self):
        self.DocumentIdImagePath=self._RentalCarCommonUi.openFileNameDialog()
    def UploadLisence(self):
        self.LisenceImagePath=self._RentalCarCommonUi.openFileNameDialog()

        
    

if __name__ == "__main__":
    import sys
    def run():
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Captian()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()
    run()

