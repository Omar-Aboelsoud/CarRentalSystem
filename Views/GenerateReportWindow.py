# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GenerateReportWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GenerateReportPeriod(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(381, 108)
        self.FromLabel = QtWidgets.QLabel(Dialog)
        self.FromLabel.setGeometry(QtCore.QRect(20, 20, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FromLabel.setFont(font)
        self.FromLabel.setObjectName("FromLabel")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(60, 20, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(230, 20, 110, 22))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 20, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GenerateReportDate"))
        self.FromLabel.setText(_translate("Dialog", "From"))
        self.label.setText(_translate("Dialog", "To"))
        self.pushButton.setText(_translate("Dialog", "Generate"))


if __name__ == "__main__":
    import sys
    def run():  
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_GenerateReportPeriod()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()
    run()
