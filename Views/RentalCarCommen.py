# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:29:38 2019

@author: oaboe
"""
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore ,QtWidgets
class RentalCarCommon:
    
#    def __init__ (self):
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
#    def InsertImageIntoTable(self,):
#         try:
#            connection = mysql.connector.connect(host='localhost',
#                                                 database='python_db',
#                                                 user='pynative',
#                                                 password='pynative@#29')
#            cursor = connection.cursor()
#            sql_insert_blob_query = """ INSERT INTO python_employee
#                              (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""
#            empPicture = convertToBinaryData(photo)
#            file = convertToBinaryData(biodataFile)
#            # Convert data into tuple format
#            insert_blob_tuple = (emp_id, name, empPicture, file)
#            result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
#            connection.commit()
#            print("Image and file inserted successfully as a BLOB into python_employee table", result)
#            
#    except mysql.connector.Error as error:
#            print("Failed inserting BLOB data into MySQL table {}".format(error))
#        
#    finally:
#            if (connection.is_connected()):
#                cursor.close()
#                connection.close()
#                print("MySQL connection is closed")