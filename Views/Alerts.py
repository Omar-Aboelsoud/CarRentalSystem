# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Alerts.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Alerts(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 240)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 411, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 0, item)
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(120, 30, 91, 22))
        self.dateEdit.setMinimumDate(QtCore.QDate(2018, 9, 14))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(220, 30, 91, 22))
        self.dateEdit_2.setMinimumDate(QtCore.QDate(2019, 12, 14))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.GenerateReport_PushButton = QtWidgets.QPushButton(Dialog)
        self.GenerateReport_PushButton.setGeometry(QtCore.QRect(170, 200, 91, 23))
        self.GenerateReport_PushButton.setObjectName("GenerateReport_PushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Last Renwal Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "New Renwal Date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Action"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "Driver License Expery"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.GenerateReport_PushButton.setText(_translate("Dialog", "Generate Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Alerts()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

