# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DayOff-ifYes-MaintenanceTable.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DayOffMaintainceTable(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(423, 234)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 421, 151))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        self.warranty_comboBox = QtWidgets.QComboBox(Dialog)
        self.warranty_comboBox.setGeometry(QtCore.QRect(230, 60, 69, 22))
        self.warranty_comboBox.setObjectName("warranty_comboBox")
        self.warranty_comboBox.addItem("")
        self.warranty_comboBox.addItem("")
        self.Bill_button = QtWidgets.QPushButton(Dialog)
        self.Bill_button.setGeometry(QtCore.QRect(330, 60, 75, 23))
        self.Bill_button.setObjectName("Bill_button")
        self.Cost_text = QtWidgets.QLineEdit(Dialog)
        self.Cost_text.setGeometry(QtCore.QRect(130, 60, 61, 20))
        self.Cost_text.setObjectName("Cost_text")
        self.PartType_text = QtWidgets.QLineEdit(Dialog)
        self.PartType_text.setGeometry(QtCore.QRect(30, 60, 61, 20))
        self.PartType_text.setObjectName("PartType_text")
        self.warranty_comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.warranty_comboBox_2.setGeometry(QtCore.QRect(230, 90, 69, 22))
        self.warranty_comboBox_2.setObjectName("warranty_comboBox_2")
        self.warranty_comboBox_2.addItem("")
        self.warranty_comboBox_2.addItem("")
        self.Bill_button_2 = QtWidgets.QPushButton(Dialog)
        self.Bill_button_2.setGeometry(QtCore.QRect(330, 90, 75, 23))
        self.Bill_button_2.setObjectName("Bill_button_2")
        self.PartType_text_2 = QtWidgets.QLineEdit(Dialog)
        self.PartType_text_2.setGeometry(QtCore.QRect(30, 90, 61, 20))
        self.PartType_text_2.setObjectName("PartType_text_2")
        self.Cost_text_2 = QtWidgets.QLineEdit(Dialog)
        self.Cost_text_2.setGeometry(QtCore.QRect(130, 90, 61, 20))
        self.Cost_text_2.setObjectName("Cost_text_2")
        self.OkPushButton = QtWidgets.QPushButton(Dialog)
        self.OkPushButton.setGeometry(QtCore.QRect(100, 180, 75, 23))
        self.OkPushButton.setObjectName("OkPushButton")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 180, 91, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Maintaince Table"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Part Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Cost"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Warranty"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Bill"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.warranty_comboBox.setItemText(0, _translate("Dialog", "Yes"))
        self.warranty_comboBox.setItemText(1, _translate("Dialog", "No"))
        self.Bill_button.setText(_translate("Dialog", "Attach Billl"))
        self.warranty_comboBox_2.setItemText(0, _translate("Dialog", "Yes"))
        self.warranty_comboBox_2.setItemText(1, _translate("Dialog", "No"))
        self.Bill_button_2.setText(_translate("Dialog", "Attach Billl"))
        self.OkPushButton.setText(_translate("Dialog", "Ok"))
        self.pushButton.setText(_translate("Dialog", "GenerateReport"))


if __name__ == "__main__":
    import sys
    def run():
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_DayOffMaintainceTable()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()
        
    run()

