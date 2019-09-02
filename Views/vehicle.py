# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vehicle.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from RentalCarCommen import RentalCarCommon
from PyQt5.QtCore import QRegExp , Qt
from PyQt5.QtWidgets import QMessageBox


from PyQt5.QtGui import QRegExpValidator
class Ui_Vehicle(object):
    def __init__(self):
     self._RentalCarCommon=RentalCarCommon()
     self.bSaveButtonActive= True
#     self._sender = self.sender()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(553, 542)
        self.VehicleTypeLabel = QtWidgets.QLabel(Dialog)
        self.VehicleTypeLabel.setGeometry(QtCore.QRect(20, 70, 61, 16))
        self.VehicleTypeLabel.setObjectName("VehicleTypeLabel")
        self.PeriodicalMaintainceLabel = QtWidgets.QLabel(Dialog)
        self.PeriodicalMaintainceLabel.setGeometry(QtCore.QRect(20, 110, 121, 16))
        self.PeriodicalMaintainceLabel.setObjectName("PeriodicalMaintainceLabel")
        self.LastPerodicMaintaince = QtWidgets.QLabel(Dialog)
        self.LastPerodicMaintaince.setGeometry(QtCore.QRect(20, 150, 101, 16))
        self.LastPerodicMaintaince.setObjectName("LastPerodicMaintaince")
        self.VehicleTypeText = QtWidgets.QLineEdit(Dialog)
        self.VehicleTypeText.setGeometry(QtCore.QRect(100, 70, 115, 20))
        self.VehicleTypeText.setObjectName("lineEdit")
        self.OwnerNameLabel = QtWidgets.QLabel(Dialog)
        self.OwnerNameLabel.setGeometry(QtCore.QRect(170, 150, 81, 16))
        self.OwnerNameLabel.setObjectName("OwnerNameLabel")
        self.OwnerNameText = QtWidgets.QLineEdit(Dialog)
        self.OwnerNameText.setEnabled(False)
        self.OwnerNameText.setGeometry(QtCore.QRect(240, 150, 101, 21))
        self.OwnerNameText.setObjectName("OwnerNameText")
        self.PhoneNumberText = QtWidgets.QLineEdit(Dialog)
        self.PhoneNumberText.setGeometry(QtCore.QRect(60, 230, 101, 20))
        self.PhoneNumberText.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.PhoneNumberText.setObjectName("PhoneNumberText")
        self.PhoneNumberText.setMaxLength(11)
        self.EmailAddressText = QtWidgets.QLineEdit(Dialog)
        self.EmailAddressText.setGeometry(QtCore.QRect(230, 230, 150, 20))
        self.EmailAddressText.setObjectName("EmailAddressText")
        self.EmailAddressLabel = QtWidgets.QLabel(Dialog)
        self.EmailAddressLabel.setGeometry(QtCore.QRect(190, 230, 41, 16))
        self.EmailAddressLabel.setObjectName("EmailAddressLabel")
        self.PhoneNumberTextLabel = QtWidgets.QLabel(Dialog)
        self.PhoneNumberTextLabel.setGeometry(QtCore.QRect(20, 230, 81, 16))
        self.PhoneNumberTextLabel.setObjectName("PhoneNumberTextLabel")
        self.ContractTypeLabel = QtWidgets.QLabel(Dialog)
        self.ContractTypeLabel.setGeometry(QtCore.QRect(20, 270, 81, 16))
        self.ContractTypeLabel.setObjectName("ContractTypeLabel")
        self.ContractTypeCheckBox = QtWidgets.QComboBox(Dialog)
        self.ContractTypeCheckBox.setGeometry(QtCore.QRect(100, 270, 69, 21))
        self.ContractTypeCheckBox.setObjectName("ContractTypeCheckBox")
        self.ContractTypeCheckBox.addItem("")
        self.ContractTypeCheckBox.addItem("")
        self.ContractTypeCheckBox.addItem("")
        self.ContractTypeCheckBox.addItem("")
        self.ContractTypeCheckBox.addItem("")
        self.ContractStartDateLabel = QtWidgets.QLabel(Dialog)
        self.ContractStartDateLabel.setGeometry(QtCore.QRect(20, 310, 101, 16))
        self.ContractStartDateLabel.setObjectName("ContractStartDateLabel")
        self.ContactExpiryDate = QtWidgets.QLabel(Dialog)
        self.ContactExpiryDate.setGeometry(QtCore.QRect(220, 310, 101, 16))
        self.ContactExpiryDate.setObjectName("ContactExpiryDate")
        self.DateOfServiceStart = QtWidgets.QLabel(Dialog)
        self.DateOfServiceStart.setGeometry(QtCore.QRect(20, 350, 101, 16))
        self.DateOfServiceStart.setObjectName("DateOfServiceStart")
        self.KMAtServiceStart = QtWidgets.QLabel(Dialog)
        self.KMAtServiceStart.setGeometry(QtCore.QRect(220, 350, 101, 16))
        self.KMAtServiceStart.setObjectName("KMAtServiceStart")
        self.LastPeriodicalMaintainceatLabel = QtWidgets.QLabel(Dialog)
        self.LastPeriodicalMaintainceatLabel.setGeometry(QtCore.QRect(280, 110, 141, 20))
        self.LastPeriodicalMaintainceatLabel.setObjectName("LastPeriodicalMaintainceatLabel")
        self.LastPeriodicMaintainceText = QtWidgets.QLineEdit(Dialog)
        self.LastPeriodicMaintainceText.setGeometry(QtCore.QRect(430, 110, 61, 20))
        self.LastPeriodicMaintainceText.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.LastPeriodicMaintainceText.setText("")
        self.LastPeriodicMaintainceText.setObjectName("LastPeriodicMaintainceText")
        self.InsruancePolicyLabel = QtWidgets.QLabel(Dialog)
        self.InsruancePolicyLabel.setGeometry(QtCore.QRect(20, 400, 101, 16))
        self.InsruancePolicyLabel.setObjectName("InsruancePolicyLabel")
        self.InsurancePolicyDateLabel = QtWidgets.QLabel(Dialog)
        self.InsurancePolicyDateLabel.setGeometry(QtCore.QRect(230, 400, 141, 16))
        self.InsurancePolicyDateLabel.setObjectName("InsurancePolicyDateLabel")
        self.UploadInsurancePolicy_PushButton = QtWidgets.QPushButton(Dialog)
        self.UploadInsurancePolicy_PushButton.setGeometry(QtCore.QRect(120, 400, 101, 23))
        self.UploadInsurancePolicy_PushButton.setObjectName("UploadInsurancePolicy_PushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 500, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 500, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.Save_PushButton = QtWidgets.QPushButton(Dialog)
        self.Save_PushButton.setGeometry(QtCore.QRect(120, 460, 91, 23))
        self.Save_PushButton.setObjectName("Save_PushButton")
        self.LicenseNumberExpiryDateLabel = QtWidgets.QLabel(Dialog)
        self.LicenseNumberExpiryDateLabel.setGeometry(QtCore.QRect(210, 30, 61, 16))
        self.LicenseNumberExpiryDateLabel.setObjectName("LicenseNumberExpiryDateLabel")
        self.LicenseNumberTextBox = QtWidgets.QLineEdit(Dialog)
        self.LicenseNumberTextBox.setGeometry(QtCore.QRect(100, 30, 101, 20))
        self.LicenseNumberTextBox.setMaxLength(14)
        self.LicenseNumberTextBox.setObjectName("LicenseNumberTextBox")
        self.LicenseNumberLabel = QtWidgets.QLabel(Dialog)
        self.LicenseNumberLabel.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.LicenseNumberLabel.setObjectName("LicenseNumberLabel")
        self.UploadCarPhoto_PushButton = QtWidgets.QPushButton(Dialog)
        self.UploadCarPhoto_PushButton.setGeometry(QtCore.QRect(235, 70, 101, 23))
        self.UploadCarPhoto_PushButton.setObjectName("UploadCarPhoto_PushButton")
        self.UploadLicensePhoto_PushButton = QtWidgets.QPushButton(Dialog)
        self.UploadLicensePhoto_PushButton.setGeometry(QtCore.QRect(370, 30, 111, 23))
        self.UploadLicensePhoto_PushButton.setObjectName("UploadLicensePhoto_PushButton")
        self.UploadContractType_PushButton = QtWidgets.QPushButton(Dialog)
        self.UploadContractType_PushButton.setGeometry(QtCore.QRect(260, 270, 101, 23))
        self.UploadContractType_PushButton.setObjectName("UploadContractType_PushButton")
        self.UploadOwnerID_PushButton = QtWidgets.QPushButton(Dialog)
        self.UploadOwnerID_PushButton.setEnabled(False)
        self.UploadOwnerID_PushButton.setGeometry(QtCore.QRect(380, 150, 101, 21))
        self.UploadOwnerID_PushButton.setObjectName("UploadOwnerID_PushButton")
        self.PeriodicalMaintainceComboBox = QtWidgets.QComboBox(Dialog)
        self.PeriodicalMaintainceComboBox.setGeometry(QtCore.QRect(190, 110, 71, 21))
        self.PeriodicalMaintainceComboBox.setObjectName("PeriodicalMaintainceComboBox")
        self.PeriodicalMaintainceComboBox.addItem("")
        self.PeriodicalMaintainceComboBox.addItem("")
        self.OwnedByThirdPartyCheckBox = QtWidgets.QCheckBox(Dialog)
        self.OwnedByThirdPartyCheckBox.setGeometry(QtCore.QRect(30, 150, 120, 17))
        self.OwnedByThirdPartyCheckBox.setObjectName("OwnedByThirdPartyCheckBox")
        self.ExpiryDateEdit = QtWidgets.QDateEdit(Dialog)
        self.ExpiryDateEdit.setGeometry(QtCore.QRect(280, 30, 71, 22))
        self.ExpiryDateEdit.setCalendarPopup(True)
        self.ExpiryDateEdit.setObjectName("ExpiryDateEdit")
        self.ContractStartDateEdit = QtWidgets.QDateEdit(Dialog)
        self.ContractStartDateEdit.setGeometry(QtCore.QRect(130, 310, 81, 21))
        self.ContractStartDateEdit.setCalendarPopup(True)
        self.ContractStartDateEdit.setObjectName("ContractStartDateEdit")
        self.DateOfServiceStartDateEdit = QtWidgets.QDateEdit(Dialog)
        self.DateOfServiceStartDateEdit.setGeometry(QtCore.QRect(130, 350, 81, 21))
        self.DateOfServiceStartDateEdit.setCalendarPopup(True)
        self.DateOfServiceStartDateEdit.setObjectName("DateOfServiceStartDateEdit")
        self.ContractExpiryDateEdit = QtWidgets.QDateEdit(Dialog)
        self.ContractExpiryDateEdit.setGeometry(QtCore.QRect(330, 310, 81, 21))
        self.ContractExpiryDateEdit.setCalendarPopup(True)
        self.ContractExpiryDateEdit.setObjectName("ContractExpiryDateEdit")
        self.KMatServiceStartText = QtWidgets.QLineEdit(Dialog)
        self.KMatServiceStartText.setGeometry(QtCore.QRect(330, 350, 81, 21))
        self.KMatServiceStartText.setObjectName("KMatServiceStartText")
        self.InsuranceExpiryDate = QtWidgets.QDateEdit(Dialog)
        self.InsuranceExpiryDate.setGeometry(QtCore.QRect(330, 400, 81, 21))
        self.InsuranceExpiryDate.setCalendarPopup(True)
        self.InsuranceExpiryDate.setObjectName("InsuranceExpiryDate")
        self.ViewLicensePhoto_PushButton = QtWidgets.QPushButton(Dialog)
        self.ViewLicensePhoto_PushButton.setEnabled(True)
        self.ViewLicensePhoto_PushButton.setGeometry(QtCore.QRect(370, 30, 111, 23))
        self.ViewLicensePhoto_PushButton.setObjectName("ViewLicensePhoto_PushButton")
        self.ViewCarPhoto_PushButton = QtWidgets.QPushButton(Dialog)
        self.ViewCarPhoto_PushButton.setEnabled(True)
        self.ViewCarPhoto_PushButton.setGeometry(QtCore.QRect(190, 70, 101, 23))
        self.ViewCarPhoto_PushButton.setObjectName("ViewCarPhoto_PushButton")
        self.ViewOwnerID_Pusbutton = QtWidgets.QPushButton(Dialog)
        self.ViewOwnerID_Pusbutton.setEnabled(True)
        self.ViewOwnerID_Pusbutton.setGeometry(QtCore.QRect(380, 150, 101, 21))
        self.ViewOwnerID_Pusbutton.setObjectName("ViewOwnerID_Pusbutton")
        self.ViewContractType_PushButton = QtWidgets.QPushButton(Dialog)
        self.ViewContractType_PushButton.setGeometry(QtCore.QRect(260, 270, 101, 23))
        self.ViewContractType_PushButton.setObjectName("ViewContractType_PushButton")
        self.ViewInsurancePolicy_PushButton = QtWidgets.QPushButton(Dialog)
        self.ViewInsurancePolicy_PushButton.setGeometry(QtCore.QRect(120, 400, 101, 23))
        self.ViewInsurancePolicy_PushButton.setObjectName("ViewInsurancePolicy_PushButton")
        self.GenerateReport_PushButton = QtWidgets.QPushButton(Dialog)
        self.GenerateReport_PushButton.setGeometry(QtCore.QRect(300, 460, 91, 23))
        self.GenerateReport_PushButton.setObjectName("GenerateReport_PushButton")
        self.IntailValueLabel = QtWidgets.QLabel(Dialog)
        self.IntailValueLabel.setGeometry(QtCore.QRect(30, 190, 61, 16))
        self.IntailValueLabel.setObjectName("IntailValueLabel")
        self.IntialValueText = QtWidgets.QLineEdit(Dialog)
        self.IntialValueText.setGeometry(QtCore.QRect(100, 190, 51, 21))
        self.IntialValueText.setObjectName("IntialValueText")
        self.FinalValueLabel = QtWidgets.QLabel(Dialog)
        self.FinalValueLabel.setGeometry(QtCore.QRect(380, 190, 61, 16))
        self.FinalValueLabel.setObjectName("FinalValueLabel")
        self.DepreciationPeriodText = QtWidgets.QLineEdit(Dialog)
        self.DepreciationPeriodText.setGeometry(QtCore.QRect(270, 190, 51, 21))
        self.DepreciationPeriodText.setObjectName("DepreciationPeriodText")
        self.DepreciationPeriodLabel = QtWidgets.QLabel(Dialog)
        self.DepreciationPeriodLabel.setGeometry(QtCore.QRect(170, 190, 101, 16))
        self.DepreciationPeriodLabel.setObjectName("DepreciationPeriodLabel")
        self.FinalValueText = QtWidgets.QLineEdit(Dialog)
        self.FinalValueText.setGeometry(QtCore.QRect(440, 190, 51, 21))
        self.FinalValueText.setObjectName("FinalValueText")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QtCore.QRect(330, 190, 41, 16))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Vehicle"))
        self.VehicleTypeLabel.setText(_translate("Dialog", "Vehicle Type"))
        self.PeriodicalMaintainceLabel.setText(_translate("Dialog", "Periodical Maintenance"))
        self.VehicleTypeText.setPlaceholderText(_translate("Dialog", "Daewoo/Lanos/2010"))
        self.OwnerNameLabel.setText(_translate("Dialog", "Owner name"))
        self.OwnerNameText.setPlaceholderText(_translate("Dialog", "Mohamed Yones"))
        self.PhoneNumberText.setPlaceholderText(_translate("Dialog", "010058104514"))
        self.EmailAddressText.setPlaceholderText(_translate("Dialog", "example@gmail.com"))
        self.EmailAddressLabel.setText(_translate("Dialog", "Email"))
        self.PhoneNumberTextLabel.setText(_translate("Dialog", "Phone"))
        self.ContractTypeLabel.setText(_translate("Dialog", "Contract Type"))
        self.ContractTypeCheckBox.setItemText(0, _translate("Dialog", "Daily"))
        self.ContractTypeCheckBox.setItemText(1, _translate("Dialog", "Monthly"))
        self.ContractTypeCheckBox.setItemText(2, _translate("Dialog", "Annual"))
        self.ContractTypeCheckBox.setItemText(3, _translate("Dialog", "Per KM"))
        self.ContractTypeCheckBox.setItemText(4, _translate("Dialog", "Other"))
        self.ContractStartDateLabel.setText(_translate("Dialog", "Contract Start Date"))
        self.ContactExpiryDate.setText(_translate("Dialog", "Contract Expiry Date"))
        self.DateOfServiceStart.setText(_translate("Dialog", "Date of service start"))
        self.KMAtServiceStart.setText(_translate("Dialog", "KM at service start"))
        self.LastPeriodicalMaintainceatLabel.setText(_translate("Dialog", "Last Periodic maintenance at"))
        self.LastPeriodicMaintainceText.setPlaceholderText(_translate("Dialog", "5000 KM"))
        self.InsruancePolicyLabel.setText(_translate("Dialog", "Insurance Policy"))
        self.InsurancePolicyDateLabel.setText(_translate("Dialog", "Expiry Date"))
        self.UploadInsurancePolicy_PushButton.setText(_translate("Dialog", "Upload Document"))
        self.pushButton_2.setText(_translate("Dialog", "Edit Data"))
        self.pushButton_3.setText(_translate("Dialog", "Archive Data"))
        self.Save_PushButton.setText(_translate("Dialog", "Save"))
        self.LicenseNumberExpiryDateLabel.setText(_translate("Dialog", "Expiry date"))
        self.LicenseNumberTextBox.setPlaceholderText(_translate("Dialog", "012345678912345"))
        self.LicenseNumberLabel.setText(_translate("Dialog", "License number"))
        self.UploadCarPhoto_PushButton.setText(_translate("Dialog", "Upload Car Photo"))
        self.UploadLicensePhoto_PushButton.setText(_translate("Dialog", "Upload Document"))
        self.UploadContractType_PushButton.setText(_translate("Dialog", "Upload Document"))
        self.UploadOwnerID_PushButton.setText(_translate("Dialog", "Upload Owner ID"))
        self.PeriodicalMaintainceComboBox.setItemText(0, _translate("Dialog", "5000"))
        self.PeriodicalMaintainceComboBox.setItemText(1, _translate("Dialog", "10000"))
        self.OwnedByThirdPartyCheckBox.setText(_translate("Dialog", "Owned by 3rd party"))
        self.ViewLicensePhoto_PushButton.setText(_translate("Dialog", "View Document"))
        self.ViewCarPhoto_PushButton.setText(_translate("Dialog", "View Document"))
        self.ViewOwnerID_Pusbutton.setText(_translate("Dialog", "View Owner ID"))
        self.ViewContractType_PushButton.setText(_translate("Dialog", "View Document"))
        self.ViewInsurancePolicy_PushButton.setText(_translate("Dialog", "View Document"))
        self.GenerateReport_PushButton.setText(_translate("Dialog", "Generate Report"))
        self.IntailValueLabel.setText(_translate("Dialog", "Intial Value"))
        self.IntialValueText.setPlaceholderText(_translate("Dialog", "19"))
        self.FinalValueLabel.setText(_translate("Dialog", "Final Value "))
        self.DepreciationPeriodText.setPlaceholderText(_translate("Dialog", "19"))
        self.DepreciationPeriodLabel.setText(_translate("Dialog", "Depreciation period "))
        self.FinalValueText.setPlaceholderText(_translate("Dialog", "19"))
        self.label_8.setText(_translate("Dialog", "Month"))
        self.KMatServiceStartText.setPlaceholderText(_translate("Dialog","5000 KM"))
        self.setButtonVisiblityDefautlSettings()
        self.UploadLicensePhoto_PushButton.clicked.connect(self.UploadLicensePhoto)
        self.UploadContractType_PushButton.clicked.connect(self.UploadContractType)
        self.UploadOwnerID_PushButton.clicked.connect(self.UploadOwnerID)
        self.UploadInsurancePolicy_PushButton.clicked.connect(self.UploadInsurancePolicy)
        self.UploadCarPhoto_PushButton.clicked.connect(self.UploadCarPhoto)
        self.OwnedByThirdPartyCheckBox.clicked.connect(self.EnableOwnedByThirdPartyFields)
        self.IntialValueText.textChanged[str].connect(self.IntialValueTextStatus)
        self.IntialValueText.setValidator(QtGui.QIntValidator())
        self.DepreciationPeriodText.textChanged[str].connect(self.DepreciationPeriodTextStatus)
        self.DepreciationPeriodText.setValidator(QtGui.QIntValidator())
        self.FinalValueText.textChanged[str].connect(self.FinalValueTextStatus)
        self.FinalValueText.setValidator(QtGui.QIntValidator())
        self.EmailAddressText.textChanged[str].connect(self.EmailAddressTextStatus)
        self.EmailAddressText.setValidator(self._RentalCarCommon.EmailRegexValidator)
        self.PhoneNumberText.textChanged[str].connect(self.PhoneNumberTextStatus)
        self.PhoneNumberText.setValidator(self._RentalCarCommon.IntegerRegexValidator)
        self.OwnerNameText.setValidator(self._RentalCarCommon.StringRegexValidator)
        self.OwnerNameText.textChanged[str].connect(self.OwnerNameTextStatus)
        self.KMatServiceStartText.textChanged[str].connect(self.KMAtServiceStartTextStatus)
        self.KMatServiceStartText.setValidator(self._RentalCarCommon.IntegerRegexValidator)
        self.VehicleTypeText.textChanged[str].connect(self.VehicleTypeTextStatus)
        self.VehicleTypeText.setValidator(self._RentalCarCommon.VehicleTypeRegexValidator)
        self.Save_PushButton.clicked.connect(lambda: self.InsertInDatabase(Dialog))
        self.LicenseNumberTextBox.textChanged[str].connect(self.LicenseNumberTextBoxCheckStatus)
        


        
    def LicenseNumberTextBoxCheckStatus(self):
        if(len(self.LicenseNumberTextBox.text())<14):
            self.LicenseNumberTextBox.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        else:
            self.LicenseNumberTextBox.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True
            
    def IntialValueTextStatus(self):
        if(self.IntialValueText.text()==""):
            self.IntialValueText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        else:
            self.IntialValueText.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True
    
    def DepreciationPeriodTextStatus(self):
        if(self.DepreciationPeriodText.text()==""):
            self.DepreciationPeriodText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        else:
            self.DepreciationPeriodText.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True

    def FinalValueTextStatus(self):
        if(self.FinalValueText.text()==""):
            self.FinalValueText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        else:
            self.FinalValueText.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True
            

    def EmailAddressTextStatus(self):
        if('@' and '.com' not in self.EmailAddressText.text()):
            self.EmailAddressText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False   
        else:
            self.EmailAddressText.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True
            
    
    def PhoneNumberTextStatus(self):
        if(len(self.PhoneNumberText.text())<11):
            self.PhoneNumberText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        else:
            self.PhoneNumberText.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True
            
    def KMAtServiceStartTextStatus(self):
        if(self.KMatServiceStartText.text()==""):
            self.KMatServiceStartText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        else:
            self.KMatServiceStartText.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True
            
            
    def VehicleTypeTextStatus(self):
        if((self.VehicleTypeText.text()).count("/")!=2):
            self.VehicleTypeText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        else:
            self.VehicleTypeText.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True
    
    def OwnerNameTextStatus(self):
        if(self.OwnerNameText.text()==""):
            self.OwnerNameText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        else:
            self.OwnerNameText.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True

    def ValidateNoEmptyFields(self):
        if (self.LicenseNumberTextBox.text()==''):
             self.LicenseNumberTextBox.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
             self.bSaveButtonActive=False
        if (self.VehicleTypeText.text()==''):
            self.VehicleTypeText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        if (self.KMatServiceStartText.text()==''):
            self.KMatServiceStartText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        if (self.PhoneNumberText.text()==''):
            self.PhoneNumberText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        if (self.EmailAddressText.text()==''):
            self.EmailAddressText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        if (self.FinalValueText.text()==''):
            self.FinalValueText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        if (self.OwnedByThirdPartyCheckBox.isChecked()== False and self.DepreciationPeriodText.text()==''):
            self.DepreciationPeriodText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        if (self.OwnedByThirdPartyCheckBox.isChecked()== False and self.IntialValueText.text()==''):
            self.IntialValueText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        if(self.OwnedByThirdPartyCheckBox.isChecked()== True and self.OwnerNameText.text()==""):
            self.OwnerNameText.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        
        
            
            
    def InsertInDatabase(self,Dialog):
        self.ValidateNoEmptyFields()
        if (self.bSaveButtonActive==False):
#            QtWidgets.QMessageBox.question(self, 'PyQt5 message', "Do you want to save?", QtWidgets.QMessageBox.Yes)
             QMessageBox().about(Dialog,"Error","Please Enter Required Fields")
        
        
        
        
    
    def UploadLicensePhoto(self):
        ImagePath=self._RentalCarCommon.openFileNameDialog()
        
    def UploadContractType(self):
        ImagePath=self._RentalCarCommon.openFileNameDialog()
        
    def UploadOwnerID(self):
        ImagePath=self._RentalCarCommon.openFileNameDialog()
        
    def UploadInsurancePolicy(self):
        ImagePath=self._RentalCarCommon.openFileNameDialog()
     
    def UploadCarPhoto(self):
        ImagePath=self._RentalCarCommon.openFileNameDialog()
        
    def setButtonVisiblityDefautlSettings(self):
        self.ViewCarPhoto_PushButton.hide()
        self.ViewContractType_PushButton.hide()
        self.ViewInsurancePolicy_PushButton.hide()
        self.ViewLicensePhoto_PushButton.hide()
        self.ViewOwnerID_Pusbutton.hide()
        
    def EnableOwnedByThirdPartyFields(self):
        if(self.OwnedByThirdPartyCheckBox.isChecked()==True):
            self.OwnerNameText.setEnabled(True)
            self.UploadOwnerID_PushButton.setEnabled(True)
            self.IntialValueText.setEnabled(False)
            self.FinalValueText.setEnabled(False)
            self.IntialValueText.clear()
            self.FinalValueText.clear()
            self.DepreciationPeriodText.setEnabled(False)
            self.IntialValueText.setStyleSheet("QLineEdit { background:gray border-style: outset;border-width: 1px;border-color: black;}")
            self.FinalValueText.setStyleSheet("QLineEdit { background:gray border-style: outset;border-width: 1px;border-color: black;}")
            self.DepreciationPeriodText.setStyleSheet("QLineEdit { background:gray border-style: outset;border-width: 1px;border-color: black;}")
            
        if  (self.OwnedByThirdPartyCheckBox.isChecked()!=True):
            self.OwnerNameText.setEnabled(False)
            self.UploadOwnerID_PushButton.setEnabled(False)
            self.OwnerNameText.clear()
            self.OwnerNameText.setStyleSheet("QLineEdit { background:gray border-style: outset;border-width: 1px;border-color: black;}")
            self.IntialValueText.setEnabled(True)
            self.FinalValueText.setEnabled(True)
            self.DepreciationPeriodText.setEnabled(True)

            
    
if __name__ == "__main__":
    import sys
    def run():
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Vehicle()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()
    run()

