# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:29:38 2019

@author: oaboe
"""
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore ,QtWidgets
from PyQt5 import QtGui
import string , random
from collections import Iterable
from ImageDisplayer import Ui_ImageDisplayer

class RentalCarCommonUi:
    
    def __init__ (self):
        Emailregex=QtCore.QRegExp("[a-z-A-Z-@-._]+")
        StringRegex=QtCore.QRegExp("[a-z-A-Z- ]+")
        VehicleTypeStringRegex=QtCore.QRegExp("[a-z-A-Z-0-9-/]+")
        CarPlateNumberRegex=QtCore.QRegExp("^[\u0621-\u064A\s0-9- ]+")
        IntRegex=QtCore.QRegExp("[0-9]+")
        self.EmailRegexValidator = QtGui.QRegExpValidator(Emailregex)
        self.StringRegexValidator=QtGui.QRegExpValidator(StringRegex)
        self.IntegerRegexValidator=QtGui.QRegExpValidator(IntRegex)
        self.VehicleTypeRegexValidator=QtGui.QRegExpValidator(VehicleTypeStringRegex)
        self.CarPlateNumberValidtor=QtGui.QRegExpValidator(CarPlateNumberRegex)
        self.MaxLenghtOfCarPlateNumber=9
        self.MaxLenghtofIDNumber=14
        self.MaxLengthofPhoneNumber=11
        self.bSaveButtonActive=False
        self._ImageDisplayer=Ui_ImageDisplayer()
     
    @property
    def EnableSaveButton(self):
        return self.bSaveButtonActive
    @EnableSaveButton.setter
    def x(self,value):
        self.bSaveButtonActive=value
        
        
    def displayImage(self,ImageinBinary):
        self._ImageDisplayer.DisplayImage(ImageinBinary)
    
    def hideFields(self,object):
        for fields in object:
            fields.hide()
    
    def clearAllFields(self,object):
        for field in object:
            field.clear()
    
    def OnClickSaveButton(self,object):
      
        for TextboxName in object:
            if (TextboxName.text()=='' and TextboxName.isEnabled()==True):
                TextboxName.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
                self.bSaveButtonActive=False
        
          
                
               
    def isEmptyOrNoneImagePath(self,object,ImagePaths):
        for PushButton,ImagePath in zip(ImagePaths,object):
            if ((ImagePath=='' or ImagePath is None) and PushButton.isEnabled()==True):
               PushButton.setStyleSheet(" QPushButton { border-style: outset;border-width: 1px;border-color: red; background-color: light gray}")
               self.bSaveButtonActive=False
            else:
                PushButton.setStyleSheet(" QPushButton { border-style: outset;border-width: 1px;border-color: black;background-color: light gray}")
               
    def IsFeildisNotAssigned(self,Fieldslist,object):
        for comboBox,Field in zip(object,Fieldslist):            
            if(len(Field)==0):
                comboBox.setStyleSheet("QComboBox { border-style: outset;border-width: 2px;border-color: red;}")
                self.bSaveButtonActive=False
            else:
                comboBox.setStyleSheet("QComboBox { border-style: outset;border-width: 1px;border-color: black;}")
                self.bSaveButtonActive=True
        
    def EmailAddressTextStatus(self ,object):
        if('@' and '.com' not in object.text()):
            object.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False   
        else:
            object.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True
                
    def VehicleTypeTextStatus(self,object):
        if((object.text()).count("/")!=2):
            object.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        else:
            object.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True  
        
    def IsEmptyTextbox(self,object):
        if(object.text()==""):
            object.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        else:
            object.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True
    
    def IsLengthofStringVaild(self,object,TextLength):
        if(len(object.text())<TextLength):
            object.setStyleSheet("QLineEdit { border-style: outset;border-width: 2px;border-color: red;}")
            self.bSaveButtonActive=False
        else:
            object.setStyleSheet("QLineEdit { border-style: outset;border-width: 1px;border-color: black;}")
            self.bSaveButtonActive=True
            
    def clearImagePaths(self,strings):
        for i in range(len(strings)):
            if(strings[i]!=''):
                strings[i]=''
                
    def DisableFields(self,object):
        for field in object:
            field.setEnabled(False)
            field.setStyleSheet("background-color: white}")
            
    def ShowFields(self,object):
        for field in object:
            field.show()
            
    def StringToDate(self,string):
        date=string.split("-")
        return QtCore.QDate(int(date[0]),int(date[1]),int(date[2]))
            
    
    def TextComboBoxIndex(self,object,ComboBoxtext):
        index=object.findText(ComboBoxtext, QtCore.Qt.MatchFixedString)
        return index
    def openFileNameDialog(self): 
        fname,_ext = QFileDialog.getOpenFileNames(QtWidgets.QDialog(), 'Single File', QtCore.QDir.rootPath() , '*.png *.jpg *.JPEG ')
        return fname
    
    def setItemsInComboBox(self,object,values):
        object.addItem("")
    
    def removeitemfromComboBox(self,object,Text):
        index = object.findText(Text, QtCore.Qt.MatchFixedString)
        object.removeItem(index)
        
    def randomString(self,stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength)) 
    
    def write_image_in_file(self,data):
        filename=self.randomString()+".jpg"
    # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data.encode()) 
    
    def single_list(self,l):
        singleList=[]
        
        for i in l:      
            if(len(i)<=1):       
                for j in i:
                    singleList.append(j)
            else:
                singleList.append(i)
        return singleList
                
        
    

#    def LoadImageFromDB(self,image):
#       labelPicture= QtWidgets.QLabel()
#       pm = QtGui.QPixmap()
#       pm.loadFromData(base64.b64decode(image))
#       labelPicture.setPixmap(QtGui.QPixmap(pm))
#       labelPicture.resize(pm.width(),pm.height())
#       labelPicture.show()
            
if __name__=="__main__":
    x=RentalCarCommonUi()
    res=x.single_list([['C:/Users/oaboe/Downloads/test.jpg'], ['C:/Users/oaboe/Downloads/test.jpg']])
    print(res)
#    x.write_image_in_file("0100001001010")
    
   