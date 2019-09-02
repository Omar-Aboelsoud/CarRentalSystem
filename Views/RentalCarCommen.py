# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:29:38 2019

@author: oaboe
"""
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore ,QtWidgets
from PyQt5 import QtGui
import mysql
class RentalCarCommon:
    
    def __init__ (self):
        Emailregex=QtCore.QRegExp("[a-z-A-Z-@-._]+")
        StringRegex=QtCore.QRegExp("[a-z-A-Z- ]+")
        VehicleTypeStringRegex=QtCore.QRegExp("[a-z-A-Z-0-9-/]+")
        IntRegex=QtCore.QRegExp("[0-9]+")
        self.EmailRegexValidator = QtGui.QRegExpValidator(Emailregex)
        self.StringRegexValidator=QtGui.QRegExpValidator(StringRegex)
        self.IntegerRegexValidator=QtGui.QRegExpValidator(IntRegex)
        self.VehicleTypeRegexValidator=QtGui.QRegExpValidator(VehicleTypeStringRegex)
#        self.InitializeDataBaseConnection()
#    
#    def InitializeDataBaseConnection(self):
        
    def openFileNameDialog(self): 
        
        fname,_ext = QFileDialog.getOpenFileName(QtWidgets.QDialog(), 'Single File', QtCore.QDir.rootPath() , '*.png *.jpg *.JPEG ')
        return fname

    def convertToBinaryData(self,filename):
    # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
#    
    def InsertImageIntoTable(self,photo,fieldName):
            connection = mysql.connector.connect(host='localhost',
                                                 database='carrent',
                                                 user='root',
                                                 password='root')
            cursor = connection.cursor()
            sql_insert_blob_query = """ INSERT INTO vehicle
                              (fieldName) VALUES (%s,%s,%s,%s)"""
            empPicture = self.convertToBinaryData(photo)
            # Convert data into tuple format
            insert_blob_tuple = (emp_id, name, empPicture, file)
            result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
            connection.commit()
            print("Image and file inserted successfully as a BLOB into python_employee table", result)
            connection.close()
    
            
