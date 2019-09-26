# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:53:12 2019

@author: oaboe
"""
import pymysql as db
from RentalCarCommenDatabase import RentalCarCommonDatabase
class RentalCarCaptaindb():
    def __init__(self):
        self.initializeConnection()
        self._RentalCarCommenDatabase=RentalCarCommonDatabase()
        
    def initializeConnection(self):
        try:
          self.connection = db.connect(user='root',password='admin', database='carrent')
          self.cursor = self.connection.cursor()
        except db.Error as err:
            print("Something went wrong: {}".format(err)) 
          
    def convertNoneToEmptyString(self,values):
        return self._RentalCarCommenDatabase.convertNoneToEmptyString(values)  
        
    def IsRecoredExistCaptain(self,value):
        if(value!=''):
              try:
                quary="SELECT * from captain where IDnumber=%s"
                fieldText=value
                self.cursor.execute(quary,fieldText)
                self.connection.commit()
                record=self.cursor.fetchone()
                return True,record 
              except db.Error as err:
                   print("Something went wrong: {}".format(err))
                   return False,None
    
    def insetCertificationImages(self,CertificationImages,idcaptain):
        query="insert (idcaptain,CertificationImage) Values (%s,%s)"
        if(len(CertificationImages)>1):
            for CertificationImage in CertificationImages:
                 image=self._RentalCarCommenDatabase.convertImageToBinaryData(CertificationImage)
                 values=[idcaptain,image]
                 self.cursor.execute(query,values)
                 self.connection.commit()
        else:
            image=self._RentalCarCommenDatabase.convertImageToBinaryData(CertificationImages)
            values=[idcaptain,image]
            self.cursor.execute(query,values)
            self.connection.commit()
                 
                 
    def getCurrentClient(self):
        query="select idclient from client"             
                 
           
    def insertIntoCaptainTable(self,Values):
        
# =============================================================================
#         ['idcaptian', 'captianName', 'IDNumber', 'LisenceNumber', 'IDNumberExpiryDate', 'LisenceNumberExpiryDate', 'IDnumberImage', 
#          'LisenceNumberImage', 'CertificationImage', 'PhoneNumber', 'Email', 'AgreementType', 'AgreementTypeImage', 
#          'Fees', 'DateofStartService']
# =============================================================================
        try:
             self.initializeConnection()
#             self.
             CaptainName=Values[0]
             IDNumber=Values[1]
             LisenceNumber=Values[2]
             IDNumberExpiryDate=Values[3]
             LisenceNumberExpiryDate=Values[4]
             IDnumberImage=self.convertImageToBinaryData(Values[5])
             LisenceNumberImage=self.convertImageToBinaryData(Values[6])
             self.insetCertificationImages(Values[7])
             PhoneNumber=Values[8]
             Email=Values[9]
             AgreementType=Values[10]
             AgreementTypeImage=self.convertImageToBinaryData(Values[11])
             Fees=Values[12]
             DateofStartService=Values[13]
            
            
             insertQuary="""INSERT INTO captain (captianName, IDNumber, LisenceNumber, IDNumberExpiryDate, LisenceNumberExpiryDate, IDnumberImage, LisenceNumberImage, PhoneNumber, Email, AgreementType, AgreementTypeImage, Fees, DateofStartService) 
             VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
             insertionValues=[ CaptainName, IDNumber, LisenceNumber, IDNumberExpiryDate, LisenceNumberExpiryDate, IDnumberImage, LisenceNumberImage, PhoneNumber, Email, AgreementType, AgreementTypeImage, Fees, DateofStartService]
             self.cursor.execute(insertQuary,insertionValues)
             self.connection.commit()
        except db.Error as err:
                print("Something went wrong: {}".format(err))
        finally:
                self.connection.close()
                self.cursor.close()
                print("MySQL connection is closed")
    