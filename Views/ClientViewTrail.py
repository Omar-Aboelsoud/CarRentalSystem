# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:25:25 2019

@author: oaboe
"""
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

Ui_Client, ClientClass = uic.loadUiType("Client.ui")

class CleintWindow(QtWidgets.QDialog, Ui_Client):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_Client.__init__(self)
        self.setupUi(self) 
        
#    def showCleintWindow(self):
#        app=QtWidgets.QApplication(sys.argv)
#        window = CleintWindow()
#        window.show()
#        app.exec_()
#        
        


if __name__ == '__main__':
    def run():
        app = QtWidgets.QApplication(sys.argv)
        window = CleintWindow()
        window.show()
        app.exec_()
    run()
    
   