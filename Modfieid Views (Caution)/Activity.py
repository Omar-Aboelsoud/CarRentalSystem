# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Activity.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(628, 454)
        self.FuelLabel = QtWidgets.QLabel(Dialog)
        self.FuelLabel.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.FuelLabel.setObjectName("FuelLabel")
        self.TripShiftLabel = QtWidgets.QLabel(Dialog)
        self.TripShiftLabel.setGeometry(QtCore.QRect(260, 50, 47, 13))
        self.TripShiftLabel.setObjectName("TripShiftLabel")
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
        self.DayoffLabel = QtWidgets.QLabel(Dialog)
        self.DayoffLabel.setGeometry(QtCore.QRect(260, 20, 47, 13))
        self.DayoffLabel.setObjectName("DayoffLabel")
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
        self.DriverNameComboBox = QtWidgets.QComboBox(Dialog)
        self.DriverNameComboBox.setGeometry(QtCore.QRect(110, 50, 111, 22))
        self.DriverNameComboBox.setEditable(True)
        self.DriverNameComboBox.setObjectName("DriverNameComboBox")
        self.CarAssigen_Label = QtWidgets.QLabel(Dialog)
        self.CarAssigen_Label.setGeometry(QtCore.QRect(20, 50, 61, 16))
        self.CarAssigen_Label.setObjectName("CarAssigen_Label")
        self.ExpensesComboBox = QtWidgets.QComboBox(Dialog)
        self.ExpensesComboBox.setGeometry(QtCore.QRect(120, 220, 111, 22))
        self.ExpensesComboBox.setEditable(True)
        self.ExpensesComboBox.setObjectName("ExpensesComboBox")
        self.ExpensesComboBox.addItem("")
        self.ExpensesComboBox.addItem("")
        self.DriverPaymentLabel = QtWidgets.QLabel(Dialog)
        self.DriverPaymentLabel.setGeometry(QtCore.QRect(20, 340, 81, 20))
        self.DriverPaymentLabel.setObjectName("DriverPaymentLabel")
        self.DriverPaymentText = QtWidgets.QLineEdit(Dialog)
        self.DriverPaymentText.setEnabled(True)
        self.DriverPaymentText.setGeometry(QtCore.QRect(120, 340, 113, 20))
        self.DriverPaymentText.setDragEnabled(False)
        self.DriverPaymentText.setClearButtonEnabled(False)
        self.DriverPaymentText.setObjectName("DriverPaymentText")
        self.ShowAllUpComingAlerts_PushButton = QtWidgets.QPushButton(Dialog)
        self.ShowAllUpComingAlerts_PushButton.setGeometry(QtCore.QRect(300, 370, 141, 23))
        self.ShowAllUpComingAlerts_PushButton.setObjectName("ShowAllUpComingAlerts_PushButton")
        self.AlertLabel = QtWidgets.QLabel(Dialog)
        self.AlertLabel.setGeometry(QtCore.QRect(50, 370, 191, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.AlertLabel.setFont(font)
        self.AlertLabel.setObjectName("AlertLabel")
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
        self.DayoffcheckBoxYes = QtWidgets.QCheckBox(Dialog)
        self.DayoffcheckBoxYes.setGeometry(QtCore.QRect(330, 20, 70, 17))
        self.DayoffcheckBoxYes.setObjectName("DayoffcheckBoxYes")
        self.DayoffcheckBoxNo = QtWidgets.QCheckBox(Dialog)
        self.DayoffcheckBoxNo.setGeometry(QtCore.QRect(390, 20, 70, 17))
        self.DayoffcheckBoxNo.setChecked(True)
        self.DayoffcheckBoxNo.setObjectName("DayoffcheckBoxNo")
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
        self.ViewTripBillScreenshot_PushButton = QtWidgets.QPushButton(Dialog)
        self.ViewTripBillScreenshot_PushButton.setGeometry(QtCore.QRect(290, 260, 111, 23))
        self.ViewTripBillScreenshot_PushButton.setObjectName("ViewTripBillScreenshot_PushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.FuelLabel.setText(_translate("Dialog", "Fuel"))
        self.TripShiftLabel.setText(_translate("Dialog", "Trip Shift"))
        self.CarPlateNumber_text.setPlaceholderText(_translate("Dialog", "س ل ع 124"))
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
        self.DayoffLabel.setText(_translate("Dialog", "DayOff"))
        self.KMnumberFueledAtLabel.setText(_translate("Dialog", "KM number fueled at"))
        self.KMnumberFueledAtText.setPlaceholderText(_translate("Dialog", "150"))
        self.IsFueledLabel.setText(_translate("Dialog", "Fueled"))
        self.CarAssigen_Label.setText(_translate("Dialog", "Driver Name"))
        self.ExpensesComboBox.setItemText(0, _translate("Dialog", "Spare Parts"))
        self.ExpensesComboBox.setItemText(1, _translate("Dialog", "Others"))
        self.DriverPaymentLabel.setText(_translate("Dialog", "Driver Payment"))
        self.DriverPaymentText.setPlaceholderText(_translate("Dialog", "500 "))
        self.ShowAllUpComingAlerts_PushButton.setText(_translate("Dialog", "Show All Upcoming Alerts"))
        self.AlertLabel.setText(_translate("Dialog", "Driver\'s license is about to expire"))
        self.DeductionLabel.setText(_translate("Dialog", "Deduction"))
        self.DeductionText.setPlaceholderText(_translate("Dialog", "200"))
        self.DayoffcheckBoxYes.setText(_translate("Dialog", "Yes"))
        self.DayoffcheckBoxNo.setText(_translate("Dialog", "No"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

