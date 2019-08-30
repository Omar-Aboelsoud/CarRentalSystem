# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Activity.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDate
from datetime import datetime
from RentalCarCommen import RentalCarCommon
from DayOffMaintainceTable import Ui_DayOffMaintainceTable
from NonOperatingExpenses import Ui_NonOperatingExpenses
class Ui_Activity(object):
        def __init__(self):
            self._RentalCarCommon=RentalCarCommon()
        def setupUi(self,Dialog):
            Dialog.setObjectName("Dialog")
            Dialog.resize(628, 454)
            self.FuelLabel = QtWidgets.QLabel(Dialog)
            self.FuelLabel.setGeometry(QtCore.QRect(20, 150, 47, 13))
            self.FuelLabel.setObjectName("FuelLabel")
            self.TripShiftLabel = QtWidgets.QLabel(Dialog)
            self.TripShiftLabel.setGeometry(QtCore.QRect(260, 50, 47, 13))
            self.TripShiftLabel.setObjectName("TripShiftLabel")
            self.AccidentDescription_Label = QtWidgets.QLabel(Dialog)
            self.AccidentDescription_Label.setGeometry(QtCore.QRect(260, 85, 150, 13))
            self.AccidentDescription_Label.setObjectName("AccidentDescription_Label")
            self.CarPlateNumber_text = QtWidgets.QLineEdit(Dialog)
            self.CarPlateNumber_text.setGeometry(QtCore.QRect(110, 20, 101, 20))
            self.CarPlateNumber_text.setObjectName("CarPlateNumber_text")
            self.CarPlateNumber_label = QtWidgets.QLabel(Dialog)
            self.CarPlateNumber_label.setGeometry(QtCore.QRect(20, 20, 91, 16))
            self.CarPlateNumber_label.setObjectName("CarPlateNumber_label")
            self.FuelText = QtWidgets.QLineEdit(Dialog)
            self.FuelText.setEnabled(False)
            self.FuelText.setGeometry(QtCore.QRect(70, 150, 61, 20))
            self.FuelText.setObjectName("FuelText")
            self.Expenses_label = QtWidgets.QLabel(Dialog)
            self.Expenses_label.setGeometry(QtCore.QRect(20, 220, 61, 16))
            self.Expenses_label.setObjectName("Expenses_label")
            self.GrossIncomeLabel = QtWidgets.QLabel(Dialog)
            self.GrossIncomeLabel.setGeometry(QtCore.QRect(20, 260, 71, 16))
            self.GrossIncomeLabel.setObjectName("GrossIncomeLabel")
            self.GrossIncomeText = QtWidgets.QLineEdit(Dialog)
            self.GrossIncomeText.setGeometry(QtCore.QRect(120, 260, 111, 20))
            self.GrossIncomeText.setObjectName("GrossIncomeText")
            self.SaveButton = QtWidgets.QPushButton(Dialog)
            self.SaveButton.setGeometry(QtCore.QRect(260, 420, 75, 23))
            self.SaveButton.setObjectName("SaveButton")
            self.UploadTripBillScreenshot_button = QtWidgets.QPushButton(Dialog)
            self.UploadTripBillScreenshot_button.setGeometry(QtCore.QRect(290, 260, 111, 23))
            self.UploadTripBillScreenshot_button.setObjectName("UploadTripBillScreenshot_button")
            self.PickupKM_label = QtWidgets.QLabel(Dialog)
            self.PickupKM_label.setGeometry(QtCore.QRect(20, 80, 47, 13))
            self.PickupKM_label.setObjectName("PickupKM_label")
            self.ReturnKMLabel = QtWidgets.QLabel(Dialog)
            self.ReturnKMLabel.setGeometry(QtCore.QRect(360, 80, 51, 16))
            self.ReturnKMLabel.setObjectName("ReturnKMLabel")
            self.ReturnKMText = QtWidgets.QLineEdit(Dialog)
            self.ReturnKMText.setGeometry(QtCore.QRect(420, 80, 61, 20))
            self.ReturnKMText.setObjectName("ReturnKMText")
            self.PickupKM_text = QtWidgets.QLineEdit(Dialog)
            self.PickupKM_text.setGeometry(QtCore.QRect(110, 80, 71, 20))
            self.PickupKM_text.setObjectName("PickupKM_text")
            self.ReturnKM_PushButton = QtWidgets.QPushButton(Dialog)
            self.ReturnKM_PushButton.setGeometry(QtCore.QRect(510, 80, 111, 23))
            self.ReturnKM_PushButton.setObjectName("ReturnKM_PushButton")
            self.PickupKM_PushButton = QtWidgets.QPushButton(Dialog)
            self.PickupKM_PushButton.setGeometry(QtCore.QRect(210, 80, 111, 23))
            self.PickupKM_PushButton.setObjectName("PickupKM_PushButton")
            self.AccidentBill_button = QtWidgets.QPushButton(Dialog)
            self.AccidentBill_button.setGeometry(QtCore.QRect(290, 220, 111, 23))
            self.AccidentBill_button.setObjectName("AccidentBill_button")
            self.UploadFuelBill_PushButton = QtWidgets.QPushButton(Dialog)
            self.UploadFuelBill_PushButton.setEnabled(False)
            self.UploadFuelBill_PushButton.setGeometry(QtCore.QRect(210, 150, 111, 23))
            self.UploadFuelBill_PushButton.setObjectName("UploadFuelBill_PushButton")
            self.AccidentLabel = QtWidgets.QLabel(Dialog)
            self.AccidentLabel.setGeometry(QtCore.QRect(260, 20, 47, 13))
            self.AccidentLabel.setObjectName("AccidentLabel")
            self.KMnumberFueledAtLabel = QtWidgets.QLabel(Dialog)
            self.KMnumberFueledAtLabel.setGeometry(QtCore.QRect(390, 150, 101, 16))
            self.KMnumberFueledAtLabel.setObjectName("KMnumberFueledAtLabel")
            self.KMnumberFueledAtText = QtWidgets.QLineEdit(Dialog)
            self.KMnumberFueledAtText.setEnabled(False)
            self.KMnumberFueledAtText.setGeometry(QtCore.QRect(500, 150, 61, 20))
            self.KMnumberFueledAtText.setObjectName("KMnumberFueledAtText")
            self.IsFueledLabel = QtWidgets.QLabel(Dialog)
            self.IsFueledLabel.setGeometry(QtCore.QRect(20, 120, 47, 13))
            self.IsFueledLabel.setObjectName("IsFueledLabel")
            self.CaptainNameComboBox = QtWidgets.QComboBox(Dialog)
            self.CaptainNameComboBox.setGeometry(QtCore.QRect(110, 50, 111, 22))
            self.CaptainNameComboBox.setEditable(True)
            self.CaptainNameComboBox.setObjectName("CaptainNameComboBox")
            self.CaptainName_Label = QtWidgets.QLabel(Dialog)
            self.CaptainName_Label.setGeometry(QtCore.QRect(20, 50, 70, 16))
            self.CaptainName_Label.setObjectName("CaptainName_Label")
            self.ExpensesComboBox = QtWidgets.QComboBox(Dialog)
            self.ExpensesComboBox.setGeometry(QtCore.QRect(120, 220, 111, 22))
            self.ExpensesComboBox.setEditable(True)
            self.ExpensesComboBox.setObjectName("ExpensesComboBox")
            self.ExpensesComboBox.addItem("")
            self.ExpensesComboBox.addItem("")
            self.ExpensesComboBox.addItem("")
            self.ExpensesComboBox.addItem("")
            self.CaptainPaymentLabel = QtWidgets.QLabel(Dialog)
            self.CaptainPaymentLabel.setGeometry(QtCore.QRect(20, 340, 81, 20))
            self.CaptainPaymentLabel.setObjectName("CaptainPaymentLabel")
            self.CaptainPaymentText = QtWidgets.QLineEdit(Dialog)
            self.CaptainPaymentText.setEnabled(True)
            self.CaptainPaymentText.setGeometry(QtCore.QRect(120, 340, 113, 20))
            self.CaptainPaymentText.setDragEnabled(False)
            self.CaptainPaymentText.setClearButtonEnabled(False)
            self.CaptainPaymentText.setObjectName("CaptainPaymentText")
            self.ShowAllUpComingAlerts_PushButton = QtWidgets.QPushButton(Dialog)
            self.ShowAllUpComingAlerts_PushButton.setGeometry(QtCore.QRect(300, 370, 141, 23))
            self.ShowAllUpComingAlerts_PushButton.setObjectName("ShowAllUpComingAlerts_PushButton")
            self.AlertLabel = QtWidgets.QLabel(Dialog)
            self.AlertLabel.setGeometry(QtCore.QRect(50, 370, 200, 20))
            font = QtGui.QFont()
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            self.AlertLabel.setFont(font)
            self.AlertLabel.setObjectName("AlertLabel")
            self.AlertLabel.setStyleSheet('color:red')
            self.DeductionLabel = QtWidgets.QLabel(Dialog)
            self.DeductionLabel.setGeometry(QtCore.QRect(20, 300, 47, 13))
            self.DeductionLabel.setObjectName("DeductionLabel")
            self.DeductionText = QtWidgets.QLineEdit(Dialog)
            self.DeductionText.setGeometry(QtCore.QRect(120, 300, 111, 20))
            self.DeductionText.setObjectName("DeductionText")
            self.TodayDateTime = QtWidgets.QDateEdit(Dialog)
            self.TodayDateTime.setGeometry(QtCore.QRect(520, 10, 91, 22))
            self.TodayDateTime.setMouseTracking(False)
            self.TodayDateTime.setCalendarPopup(True)
            self.TodayDateTime.setObjectName("TodayDateTime")
            self.AccdientCheckBoxYes = QtWidgets.QCheckBox(Dialog)
            self.AccdientCheckBoxYes.setGeometry(QtCore.QRect(330, 20, 70, 17))
            self.AccdientCheckBoxYes.setObjectName("AccdientCheckBoxYes")
            self.AccdientcheckBoxNo = QtWidgets.QCheckBox(Dialog)
            self.AccdientcheckBoxNo.setGeometry(QtCore.QRect(390, 20, 70, 17))
            self.AccdientcheckBoxNo.setChecked(True)
            self.AccdientcheckBoxNo.setObjectName("AccdientcheckBoxNo")
            self.TripShift12CheckBox = QtWidgets.QCheckBox(Dialog)
            self.TripShift12CheckBox.setGeometry(QtCore.QRect(330, 50, 70, 17))
            self.TripShift12CheckBox.setChecked(True)
            self.TripShift12CheckBox.setObjectName("TripShift12CheckBox")
            self.TripShift8CheckBox = QtWidgets.QCheckBox(Dialog)
            self.TripShift8CheckBox.setGeometry(QtCore.QRect(390, 50, 70, 17))
            self.TripShift8CheckBox.setObjectName("TripShift8CheckBox")
            self.DailyRentCheckBox = QtWidgets.QCheckBox(Dialog)
            self.DailyRentCheckBox.setGeometry(QtCore.QRect(450, 50, 70, 17))
            self.DailyRentCheckBox.setObjectName("DailyRentCheckBox")
            self.IsFueledCheckBoxYes = QtWidgets.QCheckBox(Dialog)
            self.IsFueledCheckBoxYes.setGeometry(QtCore.QRect(210, 120, 70, 17))
            self.IsFueledCheckBoxYes.setObjectName("IsFueledCheckBoxYes")
            self.IsFueledCheckBoxNo = QtWidgets.QCheckBox(Dialog)
            self.IsFueledCheckBoxNo.setGeometry(QtCore.QRect(270, 120, 70, 17))
            self.IsFueledCheckBoxNo.setChecked(True)
            self.IsFueledCheckBoxNo.setObjectName("IsFueledCheckBoxNo")
            self.ViewReturnKM_PushButton = QtWidgets.QPushButton(Dialog)
            self.ViewReturnKM_PushButton.setGeometry(QtCore.QRect(510, 80, 111, 23))
            self.ViewReturnKM_PushButton.setObjectName("ViewReturnKM_PushButton")
            self.ViewPickUpKM_PushButton = QtWidgets.QPushButton(Dialog)
            self.ViewPickUpKM_PushButton.setGeometry(QtCore.QRect(210, 80, 111, 23))
            self.ViewPickUpKM_PushButton.setObjectName("ViewPickUpKM_PushButton")
            self.ViewFuelBill_PushButton = QtWidgets.QPushButton(Dialog)
            self.ViewFuelBill_PushButton.setEnabled(False)
            self.ViewFuelBill_PushButton.setGeometry(QtCore.QRect(210, 150, 111, 23))
            self.ViewFuelBill_PushButton.setObjectName("ViewFuelBill_PushButton")
            self.ViewAccidentBill_PushButton = QtWidgets.QPushButton(Dialog)
            self.ViewAccidentBill_PushButton.setGeometry(QtCore.QRect(290, 220, 111, 23))
            self.ViewAccidentBill_PushButton.setObjectName("ViewAccidentBill_PushButton")
            self.LaborText=QtWidgets.QLineEdit(Dialog)
            self.LaborText.setGeometry(290, 220, 111, 23)
            self.LaborText.setObjectName("LaborText")
            self.ViewTripBillScreenshot_PushButton = QtWidgets.QPushButton(Dialog)
            self.ViewTripBillScreenshot_PushButton.setGeometry(QtCore.QRect(290, 260, 111, 23))
            self.ViewTripBillScreenshot_PushButton.setObjectName("ViewTripBillScreenshot_PushButton")
            self.AccdientReasonDescription_Text= QtWidgets.QTextEdit(Dialog)
            self.AccdientReasonDescription_Text.setGeometry(375,70,201,71)
            self.AccdientReasonDescription_Text.setObjectName("AccdientReasonDescription_Text")
            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog)

        def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Activity"))
            self.FuelLabel.setText(_translate("Dialog", "Fuel"))
            self.TripShiftLabel.setText(_translate("Dialog", "Trip Shift"))
            self.AccidentDescription_Label.setText(_translate("Dialog", "Accident Description"))
            self.CarPlateNumber_text.setPlaceholderText(_translate("Dialog", "س ل ع 124"))
            self.LaborText.setPlaceholderText(_translate("Dialog","200 L.E"))
            self.CarPlateNumber_label.setText(_translate("Dialog", "Car plate number"))
            self.FuelText.setPlaceholderText(_translate("Dialog", "300 L.E"))
            self.Expenses_label.setText(_translate("Dialog", "Expenses"))
            self.GrossIncomeLabel.setText(_translate("Dialog", "Gross Income"))
            self.GrossIncomeText.setPlaceholderText(_translate("Dialog", "200"))
            self.SaveButton.setText(_translate("Dialog", "Save"))
            self.UploadTripBillScreenshot_button.setText(_translate("Dialog", "Upload Attachment"))
            self.PickupKM_label.setText(_translate("Dialog", "Pickup KM"))
            self.ReturnKMLabel.setText(_translate("Dialog", "Return KM"))
            self.ReturnKMText.setPlaceholderText(_translate("Dialog", "50 KM"))
            self.PickupKM_text.setPlaceholderText(_translate("Dialog", "30 KM"))
            self.ReturnKM_PushButton.setText(_translate("Dialog", "Upload Attachment"))
            self.PickupKM_PushButton.setText(_translate("Dialog", "Upload Attachment"))
            self.AccidentBill_button.setText(_translate("Dialog", "Upload Attachment"))
            self.UploadFuelBill_PushButton.setText(_translate("Dialog", "Upload Attachment"))
            self.AccidentLabel.setText(_translate("Dialog", "Accident"))
            self.KMnumberFueledAtLabel.setText(_translate("Dialog", "KM number fueled at"))
            self.KMnumberFueledAtText.setPlaceholderText(_translate("Dialog", "150"))
            self.IsFueledLabel.setText(_translate("Dialog", "Fueled"))
            self.CaptainName_Label.setText(_translate("Dialog", "Captain Name"))
            self.ExpensesComboBox.setItemText(0, _translate("Dialog", "Select an Option"))
            self.ExpensesComboBox.setItemText(1, _translate("Dialog", "Labor"))
            self.ExpensesComboBox.setItemText(2, _translate("Dialog", "Spare Parts"))
            self.ExpensesComboBox.setItemText(3, _translate("Dialog", "Others"))
            self.CaptainPaymentLabel.setText(_translate("Dialog", "Captain Payment"))
            self.CaptainPaymentText.setPlaceholderText(_translate("Dialog", "500 "))
            self.ShowAllUpComingAlerts_PushButton.setText(_translate("Dialog", "Show All Upcoming Alerts"))
            self.AlertLabel.setText(_translate("Dialog", "Captain\'s license is about to expire"))
            self.DeductionLabel.setText(_translate("Dialog", "Deduction"))
            self.DeductionText.setPlaceholderText(_translate("Dialog", "200"))
            self.AccdientCheckBoxYes.setText(_translate("Dialog", "Yes"))
            self.AccdientcheckBoxNo.setText(_translate("Dialog", "No"))
            self.TripShift12CheckBox.setText(_translate("Dialog", "12/12"))
            self.TripShift8CheckBox.setText(_translate("Dialog", "8/8/8"))
            self.DailyRentCheckBox.setText(_translate("Dialog", "DailyRent"))
            self.IsFueledCheckBoxYes.setText(_translate("Dialog", "Yes"))
            self.IsFueledCheckBoxNo.setText(_translate("Dialog", "No"))
            self.ViewReturnKM_PushButton.setText(_translate("Dialog", "View Attachment"))
            self.ViewPickUpKM_PushButton.setText(_translate("Dialog", "View Attachment"))
            self.ViewFuelBill_PushButton.setText(_translate("Dialog", "View Attachment"))
            self.ViewAccidentBill_PushButton.setText(_translate("Dialog", "View Attachment"))
            self.ViewTripBillScreenshot_PushButton.setText(_translate("Dialog", "View Attachment"))
            
          
            self.SetCurrentDate()
            self.setHideAlertsFieldsDefaultSettings(Dialog)
            self.setButtonVisiblityDefautlSettings()
            #CheckBoxConnection
            self.IsFueledCheckBoxNo.clicked.connect(self.DisableFueled)
            self.IsFueledCheckBoxYes.clicked.connect(self.EnableFueled)
            self.TripShift8CheckBox.clicked.connect(self.Enable8Shift)
            self.TripShift12CheckBox.clicked.connect(self.Enable12Shift)
            self.DailyRentCheckBox.clicked.connect(self.EnableDailyRentShift)
            self.ReturnKM_PushButton.clicked.connect(self.UploadReturnKMScreenShots)
            self.PickupKM_PushButton.clicked.connect(self.UploadPickUpKMScreenShots)
            self.AccidentBill_button.clicked.connect(self.UploadAccidentBil)
            self.UploadTripBillScreenshot_button.clicked.connect(self.UploadTripBill) 
            self.UploadFuelBill_PushButton.clicked.connect(self.UploadFuelBill)
            self.ExpensesComboBox.currentIndexChanged.connect(self.ExpneseHandler)
            self.AccdientCheckBoxYes.clicked.connect( lambda : self.SetAccidentYes(Dialog))
            self.AccdientcheckBoxNo.clicked.connect(lambda : self.SetAccidentNo(Dialog))
           
            self.AccidentBill_button.hide()
        def SetCurrentDate(self):
             CurrentDate=datetime.now()
             self.TodayDateTime.setDate(QDate(CurrentDate.year,CurrentDate.month,CurrentDate.day))
        
        def SaveAndDailogResizeWithHidingAlert(self,Dialog):
            #supposetoHaveIfConditionifDayOffYesIsChecked
             self.SaveButton.move(280,370)
             Dialog.resize(628, 410)
             
        def SaveAndDailogResizeWithoutHidingAlert(self,Dialog):
             #supposetoHaveIfConditionifDayOffYesIsChecked
            self.SaveButton.move(260, 420)
            Dialog.resize(628, 454)
            

        def SaveAndDailogResizeWithAccdientNo(self,Dialog):
            self.SaveAndDailogResizeWithHidingAlert(Dialog)
            
        def SaveAndDailogResizeWithAccdientYes(self,Dialog):
            self.SaveButton.move(280,150)
            Dialog.resize(628, 190)
            
        def setHideAlertsFieldsDefaultSettings(self,Dialog):
             self.SaveAndDailogResizeWithHidingAlert(Dialog)
             self.AlertLabel.hide()
             self.ShowAllUpComingAlerts_PushButton.hide()
        
        def setShowAlertsFieldsDefaultSettings(self,Dialog):
            self.SaveAndDailogResizeWithoutHidingAlert(Dialog)
            self.AlertLabel.show()
            self.ShowAllUpComingAlerts_PushButton.show()
        
        def MoveExpensesComboBoxandLabelInCaseOfNoAccdient(self):
            self.ExpensesComboBox.move(120, 220)
            self.Expenses_label.move(20, 220)
            
            
        def MoveExpensesComboBoxandLabelInCaseOfAccdient(self):
            self.ExpensesComboBox.move(110, 80)
            self.Expenses_label.move(20, 85)
      
        def setButtonVisiblityDefautlSettings(self):
            self.ViewAccidentBill_PushButton.hide()
            self.ViewFuelBill_PushButton.hide()
            self.ViewPickUpKM_PushButton.hide()
            self.ViewReturnKM_PushButton.hide()
            self.ViewTripBillScreenshot_PushButton.hide()
            self.LaborText.hide()
            self.AccidentBill_button.hide()
            self.DisableDayOffReasonVisiablity()
    
        
        def DisableDayOffReasonVisiablity(self):
            self.AccidentDescription_Label.hide()
            self.AccdientReasonDescription_Text.hide()

            
        def EnableayOffReasonVisiablity(self):
            self.AccidentDescription_Label.show()
            self.AccdientReasonDescription_Text.show()
            
          
            
            
        def SetAccidentYes(self,Dialog):
            self.AccdientcheckBoxNo.setChecked(False)
            self.setButtonVisiblityDefautlSettings()
            self.FuelLabel.hide()
            self.FuelText.hide()
            self.GrossIncomeLabel.hide()
            self.GrossIncomeText.hide()
            self.UploadTripBillScreenshot_button.hide()
            self.PickupKM_label.hide()
            self.PickupKM_PushButton.hide()
            self.PickupKM_text.hide()
            self.ReturnKMLabel.hide()

            self.ReturnKM_PushButton.hide()
            self.ReturnKMText.hide()
            self.AccidentBill_button.hide()
            self.UploadFuelBill_PushButton.hide()
            self.KMnumberFueledAtLabel.hide()
            self.KMnumberFueledAtText.hide()
            self.IsFueledLabel.hide()
            self.CaptainPaymentLabel.hide()
            self.CaptainPaymentText.hide()
            self.ShowAllUpComingAlerts_PushButton.hide()
            self.AlertLabel.hide()
            self.DeductionLabel.hide()
            self.DeductionText.hide()
            self.IsFueledCheckBoxYes.hide()
            self.IsFueledCheckBoxNo.hide()
            self.LaborText.hide()
            self.EnableayOffReasonVisiablity()
            self.SaveAndDailogResizeWithAccdientYes(Dialog)
            self.MoveAlertFieldsInCaseOfAccdeint()
            self.MoveAlertFieldsInCaseOfNoAccdeint()
            self.EnableayOffReasonVisiablity()
            self.MoveExpensesComboBoxandLabelInCaseOfAccdient()
                
                  
        def SetAccidentNo(self,Dialog):
            self.AccdientCheckBoxYes.setChecked(False)
      
            self.FuelLabel.show()
            self.FuelText.show()
            self.GrossIncomeLabel.show()
            self.GrossIncomeText.show()
            self.UploadTripBillScreenshot_button.show()
            self.PickupKM_label.show()
            self.PickupKM_PushButton.show()
            self.PickupKM_text.show()
            self.ReturnKMLabel.show()

            self.ReturnKM_PushButton.show()
            self.ReturnKMText.show()
            self.AccidentBill_button.show()
            self.UploadFuelBill_PushButton.show()
            self.KMnumberFueledAtLabel.show()
            self.KMnumberFueledAtText.show()
            self.IsFueledLabel.show()
            self.CaptainPaymentLabel.show()
            self.CaptainPaymentText.show()
            self.DeductionLabel.show()
            self.DeductionText.show()
            self.IsFueledCheckBoxYes.show()
            self.IsFueledCheckBoxNo.show()
            self.LaborText.hide()
            self.AccidentBill_button.hide()
            self.DisableDayOffReasonVisiablity()
            self.SaveAndDailogResizeWithAccdientNo(Dialog)
            self.MoveExpensesComboBoxandLabelInCaseOfNoAccdient()
     
          
        def ExpneseHandler(self):
            CheckBoxStatus= self.ExpensesComboBox.currentText()
            if(CheckBoxStatus=='Spare Parts'):
                self.OpenMaintainceTable()
                self.LaborText.hide()
                
            if(CheckBoxStatus=='Others'):
                self.OpenNonOperatingExpenses()
                self.LaborText.hide()
            if(CheckBoxStatus=='Labor'):
                self.LaborText.show()
                
#            if(CheckBoxStatus!='Select an Option'):
                
      
        def  MoveAlertFieldsInCaseOfNoAccdeint(self):
            self.AlertLabel.move(50,110)
            self.ShowAllUpComingAlerts_PushButton.move(300,110)
            
            
        def  MoveAlertFieldsInCaseOfAccdeint(self):
            self.AlertLabel.move(50,160)
            self.ShowAllUpComingAlerts_PushButton.move(300,160)
            
            
        def OpenMaintainceTable(self):
            self._OpenMaintainceTableUI= QtWidgets.QDialog()
            self._OpenMaintainceTable= Ui_DayOffMaintainceTable()
            self._OpenMaintainceTable.setupUi(self._OpenMaintainceTableUI)
            self._OpenMaintainceTableUI.show()
        
        def OpenNonOperatingExpenses(self):
            self._OpenNonOperatingExpensesUI= QtWidgets.QDialog()
            self._OpenNonOperatingExpenses= Ui_NonOperatingExpenses()
            self._OpenNonOperatingExpenses.setupUi(self._OpenNonOperatingExpensesUI)
            self._OpenNonOperatingExpensesUI.show()
                                 
        def EnableFueled(self):
                self.IsFueledCheckBoxYes.setChecked(True)
                self.IsFueledCheckBoxNo.setChecked(False)
                
                self.FuelText.setEnabled(True)
                self.UploadFuelBill_PushButton.setEnabled(True)
                self.KMnumberFueledAtText.setEnabled(True)
                
        def DisableFueled(self):
            self.IsFueledCheckBoxNo.setChecked(True)
            self.IsFueledCheckBoxYes.setChecked(False)
            
            self.FuelText.setEnabled(False)
            self.UploadFuelBill_PushButton.setEnabled(False)
            self.KMnumberFueledAtText.setEnabled(False)
                
        def Enable8Shift(self):
            self.TripShift12CheckBox.setChecked(False)
            self.TripShift8CheckBox.setChecked(True)
            self.DailyRentCheckBox.setChecked(False)
            
            
        def Enable12Shift(self):
            self.TripShift12CheckBox.setChecked(True)
            self.TripShift8CheckBox.setChecked(False)
            self.DailyRentCheckBox.setChecked(False)
        
        def EnableDailyRentShift(self):
             
            self.TripShift12CheckBox.setChecked(False)
            self.TripShift8CheckBox.setChecked(False)
            self.DailyRentCheckBox.setChecked(True)
            
        def UploadPickUpKMScreenShots(self):
            ImagePath=self._RentalCarCommon.openFileNameDialog()
            
        def UploadReturnKMScreenShots(self):
            ImagePath=self._RentalCarCommon.openFileNameDialog()
            
        def UploadFuelBill(self):
            ImagePath=self._RentalCarCommon.openFileNameDialog()
        
        def UploadAccidentBil(self):
            ImagePath=self._RentalCarCommon.openFileNameDialog()
        
        def UploadTripBill(self):
            ImagePath=self._RentalCarCommon.openFileNameDialog()

if __name__ == "__main__":
    import sys
    def run():
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Activity()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()
    run()

