# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#import Classes
from Client import Ui_Client
from Captain import Ui_Captian
from Alerts import Ui_Alerts
from vehicle import Ui_Vehicle
from Activity import Ui_Activity
from vendor import Ui_Vendor
from GenerateReportWindow import Ui_GenerateReportPeriod

########################
class Ui_MainWindow(object):
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
        self.Captian_button = QtWidgets.QPushButton(Dialog)
        self.Captian_button.setGeometry(QtCore.QRect(210, 10, 161, 51))
        self.Captian_button.setObjectName("Captian_button")
        self.Alerts_button = QtWidgets.QPushButton(Dialog)
        self.Alerts_button.setGeometry(QtCore.QRect(10, 160, 161, 51))
        self.Alerts_button.setObjectName("Alerts_button")
        self.GenerateReport_button = QtWidgets.QPushButton(Dialog)
        self.GenerateReport_button.setGeometry(QtCore.QRect(210, 160, 161, 51))
        self.GenerateReport_button.setObjectName("GenerateReport_button")
        self.LoadOldData_button = QtWidgets.QPushButton(Dialog)
        self.LoadOldData_button.setGeometry(QtCore.QRect(210, 230, 161, 51))
        self.LoadOldData_button.setObjectName("LoadOldData_button")
        self.Vendor_button = QtWidgets.QPushButton(Dialog)
        self.Vendor_button.setGeometry(QtCore.QRect(10, 230, 161, 51))
        self.Vendor_button.setObjectName("Vendor_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Mainwindow"))
        self.Vehicle_button.setText(_translate("Dialog", "Vehicle "))
        self.Client_button.setText(_translate("Dialog", "Client"))
        self.Activity_button.setText(_translate("Dialog", "Activity"))
        self.Captian_button.setText(_translate("Dialog", "Captian"))
        self.Alerts_button.setText(_translate("Dialog", "Alerts"))
        self.GenerateReport_button.setText(_translate("Dialog", "Generate Report"))
        self.LoadOldData_button.setText(_translate("Dialog", "Load Open Balance"))
        self.Vendor_button.setText(_translate("Dialog", "Vendor"))


   

        
        #OpenTheWindows
        
        self.Client_button.clicked.connect(self.OpenClientWindow)
        self.Captian_button.clicked.connect(self.OpenCaptianWindow)
        self.Alerts_button.clicked.connect(self.OpenAlertWindow)
        self.Vehicle_button.clicked.connect(self.OpenVehicleWindow)
        self.Activity_button.clicked.connect(self.OpenActivityWindow)
        self.Vendor_button.clicked.connect(self.OpenVendorWindow)
        self.LoadOldData_button.clicked.connect(self.OpenGenerateReportPeriodWindow)
        



    def OpenClientWindow(self):
        self._clientwindowUI= QtWidgets.QDialog()
        self._client= Ui_Client()
        self._client.setupUi(self._clientwindowUI)
        self._clientwindowUI.show()
        
    def OpenCaptianWindow(self):
        self._CaptianwindowUI= QtWidgets.QDialog()
        self._Captian= Ui_Captian()
        self._Captian.setupUi(self._CaptianwindowUI)
        self._CaptianwindowUI.show()
        
    def OpenAlertWindow(self):
        self._AlertrwindowUI= QtWidgets.QDialog()
        self._Alert= Ui_Alerts()
        self._Alert.setupUi(self._AlertrwindowUI)
        self._AlertrwindowUI.show()
        
    def OpenVehicleWindow(self):
        self._VehiclewindowUI= QtWidgets.QDialog()
        self._Vehicle= Ui_Vehicle()
        self._Vehicle.setupUi(self._VehiclewindowUI)
        self._VehiclewindowUI.show()
        
    def OpenActivityWindow(self):
        self._ActivitywindowUI= QtWidgets.QDialog()
        self._Activity= Ui_Activity()
        self._Activity.setupUi(self._ActivitywindowUI)
        self._ActivitywindowUI.show()
        
    def OpenVendorWindow(self):
        self._VendorwindowUI= QtWidgets.QDialog()
        self._Vendor= Ui_Vendor()
        self._Vendor.setupUi(self._VendorwindowUI)
        self._VendorwindowUI.show()
        
    def OpenGenerateReportPeriodWindow(self):
        self._GenerateReportPeriodUI= QtWidgets.QDialog()
        self._GenerateReportPeriod= Ui_GenerateReportPeriod()
        self._GenerateReportPeriod.setupUi(self._GenerateReportPeriodUI)
        self._GenerateReportPeriodUI.show()
    
        






if __name__ == "__main__":
    import sys
    def run():
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_MainWindow()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()
    run()
