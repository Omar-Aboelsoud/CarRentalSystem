# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 08:39:12 2019

@author: oaboe
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot 
from Views.Activity import Ui_Activity
from Views.ClientViewTrail import CleintWindow
class MainController(QObject):
        
        def OpenClientWindow(self):
          self.client=CleintWindow()
          self.client.showCleintWindow()
         
           
          
            
        
class Client(QtWidgets.QMainWindow,CleintWindow ):
    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        
#x=  MainController()
#x.OpenClientWindow()
       
                     
                     