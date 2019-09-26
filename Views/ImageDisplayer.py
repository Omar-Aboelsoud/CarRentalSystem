# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:15:46 2019

@author: oaboe
"""

from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageDisplayer(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QLabel(Dialog)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Image Displayer Window"))
        
    
  
    def DisplayImage(self,imageBlob):
        # Create widget
        
        qimg = QtGui.QImage.fromData(imageBlob)
        pixmap = QtGui.QPixmap.fromImage(qimg)
        print(pixmap)
#        self.label.setPixmap(pixmap)
#        self.resize(pixmap.width(),pixmap.height())
#        
#        self.show()
    
    

if __name__ == "__main__":
    import sys
    def run():
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_ImageDisplayer()
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec_()
    run()