# -*- coding: utf-8 -*-


from PyQt5.QtCore import QObject, pyqtSignal


class VendorModel(QObject):
    VendorNameSignal= pyqtSignal(str)
    VendorPhoneNumberSignal=pyqtSignal(int)
    VendorContactPesronSignal=pyqtSignal(str)
    TypeofVendorSignal=pyqtSignal(str)
   
    def __init__(self):
        self._vendorName=""
        self._vendorContactPesron=""
        self._vendorPhoneNumber=0
        self._typeofVendorComboBox=""
        
    @property
    def getVendorName(self):
        return self._vendorName
    
    @property.setter
    def setVendorName(self,VendorName):
        self._vendorName=VendorName
#        self.VendorNameSignal.
        
        
        
    #databaseLogic
    
       