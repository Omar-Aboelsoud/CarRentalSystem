# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Client.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from RentalCarCommen import RentalCarCommonUi
from PyQt5.QtWidgets import QMessageBox
from RentalCarClientDatabase import RentalCarClientdb
class Ui_Client(object):
    def __init__(self):
        self._RentalCarCommonUi=RentalCarCommonUi()
        self._RentalCarClientDatabase=RentalCarClientdb()
        self.ContractImagePath=None
        self.VehiclesApproved=[]
        self.CaptainsApproved=[]
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(545, 400)
        self.ClientName_label = QtWidgets.QLabel(Dialog)
        self.ClientName_label.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.ClientName_label.setObjectName("ClientName_label")
        self.ContactName_label = QtWidgets.QLabel(Dialog)
        self.ContactName_label.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.ContactName_label.setObjectName("ContactName_label")
        self.EmailLabel = QtWidgets.QLabel(Dialog)
        self.EmailLabel.setGeometry(QtCore.QRect(350, 70, 91, 16))
        self.EmailLabel.setObjectName("EmailLabel")
        self.Phone_label = QtWidgets.QLabel(Dialog)
        self.Phone_label.setGeometry(QtCore.QRect(210, 70, 91, 16))
        self.Phone_label.setObjectName("Phone_label")
        self.ContractStartDate_label = QtWidgets.QLabel(Dialog)
        self.ContractStartDate_label.setGeometry(QtCore.QRect(20, 160, 111, 16))
        self.ContractStartDate_label.setObjectName("ContractStartDate_label")
        self.ContractType_label = QtWidgets.QLabel(Dialog)
        self.ContractType_label.setGeometry(QtCore.QRect(30, 120, 91, 16))
        self.ContractType_label.setObjectName("ContractType_label")
        self.ContractExpiryDate_label = QtWidgets.QLabel(Dialog)
        self.ContractExpiryDate_label.setGeometry(QtCore.QRect(240, 160, 111, 16))
        self.ContractExpiryDate_label.setObjectName("ContractExpiryDate_label")
        self.ContractType_combobox = QtWidgets.QComboBox(Dialog)
        self.ContractType_combobox.setGeometry(QtCore.QRect(118, 120, 101, 22))
        self.ContractType_combobox.setEditable(True)
        self.ContractType_combobox.setObjectName("ContractType_combobox")
        self.ContractType_combobox.addItem("")
        self.ContractType_combobox.addItem("")
        self.ContractType_combobox.addItem("")
        self.ContractType_combobox.addItem("")
        self.ContractType_combobox.addItem("")
        self.ContractType_combobox.addItem("")
        self.UploadDocumentButton = QtWidgets.QPushButton(Dialog)
        self.UploadDocumentButton.setGeometry(QtCore.QRect(230, 120, 101, 23))
        self.UploadDocumentButton.setObjectName("UploadDocumentButton")
        self.ViewDocumentButton = QtWidgets.QPushButton(Dialog)
        self.ViewDocumentButton.setGeometry(QtCore.QRect(230, 120, 101, 23))
        self.ViewDocumentButton.setObjectName("ViewDocumentButton")
        self.Fees_label = QtWidgets.QLabel(Dialog)
        self.Fees_label.setGeometry(QtCore.QRect(30, 190, 41, 16))
        self.Fees_label.setObjectName("Fees_label")
        self.Fees_text = QtWidgets.QLineEdit(Dialog)
        self.Fees_text.setGeometry(QtCore.QRect(120, 190, 61, 20))
        self.Fees_text.setObjectName("Fees_text")
        self.VehiclesAssigned_label = QtWidgets.QLabel(Dialog)
        self.VehiclesAssigned_label.setGeometry(QtCore.QRect(30, 230, 91, 16))
        self.VehiclesAssigned_label.setObjectName("VehiclesAssigned_label")
        self.Phone_text = QtWidgets.QLineEdit(Dialog)
        self.Phone_text.setGeometry(QtCore.QRect(250, 70, 91, 20))
        self.Phone_text.setObjectName("Phone_text")
        self.Phone_text.setMaxLength(11)
        self.EmailText = QtWidgets.QLineEdit(Dialog)
        self.EmailText.setGeometry(QtCore.QRect(390, 70, 141, 20))
        self.EmailText.setObjectName("EmailText")
        self.CaptainsApproved_label = QtWidgets.QLabel(Dialog)
        self.CaptainsApproved_label.setGeometry(QtCore.QRect(30, 270, 95, 16))
        self.CaptainsApproved_label.setObjectName("CaptainsApproved_label")
        self.ClientName_text = QtWidgets.QLineEdit(Dialog)
        self.ClientName_text.setGeometry(QtCore.QRect(90, 30, 111, 20))
        self.ClientName_text.setObjectName("ClientName_text")
        self.ArchiveData_button = QtWidgets.QPushButton(Dialog)
        self.ArchiveData_button.setEnabled(False)
        self.ArchiveData_button.setGeometry(QtCore.QRect(290, 360, 91, 23))
        self.ArchiveData_button.setObjectName("ArchiveData_button")
        self.SaveButton = QtWidgets.QPushButton(Dialog)
        self.SaveButton.setGeometry(QtCore.QRect(130, 330, 91, 23))
        self.SaveButton.setObjectName("SaveButton")
        self.EditDataButton = QtWidgets.QPushButton(Dialog)
        self.EditDataButton.setEnabled(False)
        self.EditDataButton.setGeometry(QtCore.QRect(130, 360, 91, 23))
        self.EditDataButton.setObjectName("EditDataButton")
        self.ContactName_text = QtWidgets.QLineEdit(Dialog)
        self.ContactName_text.setGeometry(QtCore.QRect(90, 70, 111, 20))
        self.ContactName_text.setObjectName("ContactName_text")
        self.VehiclesAssignedComboBox = QtWidgets.QComboBox(Dialog)
        self.VehiclesAssignedComboBox.setGeometry(QtCore.QRect(130, 230, 110, 22))
        self.VehiclesAssignedComboBox.setEditable(True)
        self.VehiclesAssignedComboBox.setObjectName("VehiclesAssignedComboBox")
        self.StartContractDate_DateEdit = QtWidgets.QDateEdit(Dialog)
        self.StartContractDate_DateEdit.setGeometry(QtCore.QRect(120, 160, 110, 22))
        self.StartContractDate_DateEdit.setMinimumDate(QtCore.QDate(2019, 9, 14))
        self.StartContractDate_DateEdit.setCalendarPopup(True)
        self.StartContractDate_DateEdit.setObjectName("StartContractDate_DateEdit")
        self.CaptainsApprovedComboBox = QtWidgets.QComboBox(Dialog)
        self.CaptainsApprovedComboBox.setGeometry(QtCore.QRect(130, 270, 110, 22))
        self.CaptainsApprovedComboBox.setEditable(True)
        self.CaptainsApprovedComboBox.setObjectName("CaptainsApprovedComboBox")
        self.VehiclesAssigned_AddButton = QtWidgets.QPushButton(Dialog)
        self.VehiclesAssigned_AddButton.setGeometry(QtCore.QRect(260, 230, 75, 23))
        self.VehiclesAssigned_AddButton.setObjectName("VehiclesAssigned_AddButton")
        self.ContractExpiryDate_DateEdit = QtWidgets.QDateEdit(Dialog)
        self.ContractExpiryDate_DateEdit.setGeometry(QtCore.QRect(350, 160, 110, 22))
        self.ContractExpiryDate_DateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 9, 14), QtCore.QTime(0, 0, 0)))
        self.ContractExpiryDate_DateEdit.setCalendarPopup(True)
        self.ContractExpiryDate_DateEdit.setObjectName("ContractExpiryDate_DateEdit")
        self.CaptainAssign_AddButton = QtWidgets.QPushButton(Dialog)
        self.CaptainAssign_AddButton.setGeometry(QtCore.QRect(260, 270, 75, 23))
        self.CaptainAssign_AddButton.setObjectName("CaptainAssign_AddButton")
        self.VehiclesAssigned_RemoveButton = QtWidgets.QPushButton(Dialog)
        self.VehiclesAssigned_RemoveButton.setEnabled(False)
        self.VehiclesAssigned_RemoveButton.setGeometry(QtCore.QRect(360, 230, 75, 23))
        self.VehiclesAssigned_RemoveButton.setObjectName("VehiclesAssigned_RemoveButton")
        self.CaptainsAssigned_RemoveButton = QtWidgets.QPushButton(Dialog)
        self.CaptainsAssigned_RemoveButton.setEnabled(False)
        self.CaptainsAssigned_RemoveButton.setGeometry(QtCore.QRect(360, 270, 75, 23))
        self.CaptainsAssigned_RemoveButton.setObjectName("CaptainsAssigned_RemoveButton")
        self.GenerateReport_PushButton = QtWidgets.QPushButton(Dialog)
        self.GenerateReport_PushButton.setGeometry(QtCore.QRect(290, 330, 91, 23))
        self.GenerateReport_PushButton.setObjectName("GenerateReport_PushButton")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Client"))
        self.ClientName_label.setText(_translate("Dialog", "Client Name"))
        self.ContactName_label.setText(_translate("Dialog", "Contact Name"))
        self.EmailLabel.setText(_translate("Dialog", "Email"))
        self.Phone_label.setText(_translate("Dialog", "Phone"))
        self.ContractStartDate_label.setText(_translate("Dialog", "Contract Start Date"))
        self.ContractType_label.setText(_translate("Dialog", "Contract Type"))
        self.ContractExpiryDate_label.setText(_translate("Dialog", "Contract Expiry Date"))
        self.ContractType_combobox.setItemText(0, _translate("Dialog", "Daily"))
        self.ContractType_combobox.setItemText(1, _translate("Dialog", "Monthly"))
        self.ContractType_combobox.setItemText(2, _translate("Dialog", "Annual"))
        self.ContractType_combobox.setItemText(3, _translate("Dialog", "Per KM"))
        self.ContractType_combobox.setItemText(4, _translate("Dialog", "Application Based"))
        self.ContractType_combobox.setItemText(5, _translate("Dialog", "Other"))
        self.UploadDocumentButton.setText(_translate("Dialog", "Upload Document"))
        self.ViewDocumentButton.setText(_translate("Dialog", "View Document"))
        self.Fees_label.setText(_translate("Dialog", "Fees"))
        self.Fees_text.setPlaceholderText(_translate("Dialog", "Ex.1000"))
        self.VehiclesAssigned_label.setText(_translate("Dialog", "Vehicles Approved  "))
        self.Phone_text.setPlaceholderText(_translate("Dialog", "01152134554"))
        self.EmailText.setPlaceholderText(_translate("Dialog", "example@gmail.com"))
        self.CaptainsApproved_label.setText(_translate("Dialog", "Captains Approved"))
        self.ClientName_text.setPlaceholderText(_translate("Dialog", "Uber"))
        self.ArchiveData_button.setText(_translate("Dialog", "Archive Data"))
        self.SaveButton.setText(_translate("Dialog", "Save"))
        self.EditDataButton.setText(_translate("Dialog", "Edit Data"))
        self.ContactName_text.setPlaceholderText(_translate("Dialog", "Ahmed Younes"))
        self.VehiclesAssigned_AddButton.setText(_translate("Dialog", "Add"))
        self.CaptainAssign_AddButton.setText(_translate("Dialog", "Add"))
        self.VehiclesAssigned_RemoveButton.setText(_translate("Dialog", "Remove"))
        self.CaptainsAssigned_RemoveButton.setText(_translate("Dialog", "Remove"))
        self.GenerateReport_PushButton.setText(_translate("Dialog", "Generate Report"))
        
        
        
        
        
        self.UploadDocumentButton.clicked.connect(self.UploadDocument)
        self.SaveButton.clicked.connect(lambda: self.onSaveClick(Dialog))
        self.setButtonVisabilty()
        
        self.ContactName_text.textChanged[str].connect(lambda: self._RentalCarCommonUi.IsEmptyTextbox(self.ContactName_text))
        self.ContactName_text.setValidator(self._RentalCarCommonUi.StringRegexValidator)
        
        self.ClientName_text.textChanged[str].connect(lambda: self._RentalCarCommonUi.IsEmptyTextbox(self.ClientName_text))
        self.ClientName_text.setValidator(self._RentalCarCommonUi.StringRegexValidator)
        
        self.Phone_text.textChanged[str].connect(lambda: self._RentalCarCommonUi.IsLengthofStringVaild(self.Phone_text,self._RentalCarCommonUi.MaxLengthofPhoneNumber))
        self.Phone_text.setValidator(self._RentalCarCommonUi.IntegerRegexValidator)
        self.EmailText.textChanged[str].connect(lambda: self._RentalCarCommonUi.EmailAddressTextStatus(self.EmailText))
        self.EmailText.setValidator(self._RentalCarCommonUi.EmailRegexValidator)
        self.Fees_text.textChanged[str].connect(lambda: self._RentalCarCommonUi.IsEmptyTextbox(self.Fees_text))
        self.Fees_text.setValidator(self._RentalCarCommonUi.IntegerRegexValidator)
        self.VehiclesAssigned_AddButton.clicked.connect(lambda: self.AddVehilcesApproved(self.VehiclesAssignedComboBox.currentText()))
        self.CaptainAssign_AddButton.clicked.connect(lambda: self.AddCaptainsApproved(self.CaptainsApprovedComboBox.currentText()))
        
        self.loadCaptainNames()
        self.loadVehicleNames()
        
        
    def AddVehilcesApproved(self,VehicleName):
        self.VehiclesApproved.append(VehicleName)
        self._RentalCarCommonUi.removeitemfromComboBox(self.VehiclesAssignedComboBox,VehicleName)
      
    def AddCaptainsApproved(self,CaptainName):
        self.CaptainsApproved.append(CaptainName)
        self._RentalCarCommonUi.removeitemfromComboBox(self.CaptainsApprovedComboBox,CaptainName)
        
    def InsertValuesInVehicleDB(self):
            clientName=self.ClientName_text.text()
            ContantName=self.ContactName_text.text()
            phone=self.Phone_text.text()
            email=self.EmailText.text()
            contractType=self.ContractType_combobox.currentText()
            ContractImage=self.ContractImagePath
            contractStartDate=self.StartContractDate_DateEdit.date().toString("yyyy-MM-dd")
            contractExpiryDate=self.ContractExpiryDate_DateEdit.date().toString("yyyy-MM-dd")
            fees=self.Fees_text.text()
            vehiclesApproved=self.VehiclesApproved
            captainApproved=self.CaptainsApproved
            
            values=[clientName,ContantName,phone,email,contractType,ContractImage,contractStartDate,
                    contractExpiryDate,fees,vehiclesApproved,captainApproved]
            valueswithNoNone=self._RentalCarClientDatabase.convertNoneToEmptyString(values)
            self._RentalCarClientDatabase.insertIntoClientTable(valueswithNoNone)
        
        
    def onSaveClick(self,Dialog):
        textBoxeswithCheckboxNames =[self.ContactName_text,self.ClientName_text,self.Phone_text,self.EmailText,self.Fees_text]
        pushButtons=[self.UploadDocumentButton]
        ImagePaths=[self.ContractImagePath]
        ComboBoxes=[self.CaptainsApprovedComboBox,self.VehiclesAssignedComboBox]
        FieldsAssigned=[self.VehiclesApproved,self.CaptainsApproved]
        self._RentalCarCommonUi.OnClickSaveButton(textBoxeswithCheckboxNames)
        self._RentalCarCommonUi.isEmptyOrNoneImagePath(ImagePaths,pushButtons)
        self._RentalCarCommonUi.IsFeildisNotAssigned(FieldsAssigned,ComboBoxes)
            
        if (self._RentalCarCommonUi.bSaveButtonActive==False):
             QMessageBox().about(Dialog,"Error","Please Enter Required Fields")
        if (self._RentalCarCommonUi.bSaveButtonActive==True):
             self.InsertValuesInVehicleDB()
             reply= QMessageBox.information(Dialog, "Messege", "Saved Successfully", QMessageBox.Ok)
            
    def loadCaptainNames(self):
        captainNames=self._RentalCarClientDatabase.loadCaptainNames()

        self.CaptainsApprovedComboBox.addItems(captainNames)
    
    def loadVehicleNames(self):
       vehicleNames=self._RentalCarClientDatabase.loadVehiclesNames()
      
       self.VehiclesAssignedComboBox.addItems(vehicleNames)
    
    def UploadDocument(self):
        self.ContractImagePath=self._RentalCarCommonUi.openFileNameDialog()
     
        
    def setButtonVisabilty(self):
        self.ViewDocumentButton.hide()
        


if __name__ == "__main__":
    import sys
    def run():
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Client()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()
    run()
