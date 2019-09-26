# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:51:28 2019

@author: oaboe
"""

import pymysql as db
from RentalCarCommenDatabase import RentalCarCommonDatabase
class RentalCarClientdb():
    def __init__ (self):
        self.initializeConnection()
        self._RentalCarCommenDatabase=RentalCarCommonDatabase()
        
#    def reteriveApprovedCaptainNames(self):
        
    
    def convertNoneToEmptyString(self,values):
        return self._RentalCarCommenDatabase.convertNoneToEmptyString(values)
        
        
    def convertImageToBinaryData(self,filename):
       return self._RentalCarCommenDatabase.convertImageToBinaryData(filename)
    
    def initializeConnection(self):
        try:
          self.connection = db.connect(user='root',password='admin', database='carrent')
          self.cursor = self.connection.cursor()
          
        except db.Error as err:
            print("Something went wrong: {}".format(err))
    
    def isClient_CaptainTableEmpty(self):
        
       
        try:
            
            query="select Count(*) from client_captian"
            self.cursor.execute(query)
            NumberoFRecoreds=self.cursor.fetchone()
        
            if (NumberoFRecoreds[0]==0):
                return True
            else:
                return False
        except db.Error as err:
                print("Something went wrong Cleitn Captain is Empty: {}".format(err))    

    def isClient_VehicleTableEmpty(self):
        
        try:
            
            query="select Count(*) from client_vehicle"
            self.cursor.execute(query)
            self.connection.commit()
            NumberoFRecoreds=self.cursor.fetchone()
        
            if (NumberoFRecoreds[0]==0):
                return True
            else:
                return False
        except db.Error as err:
                print("Something went wrong Client Vehicle is Empty: {}".format(err))
                
                
                
    def insertIntoClientVehcileTableForTheFirstTime(self,VehiclesApproved,idclient):
#        ['idClient_Vehicle_Driver', 'VehicleName', 'idclient']
#         self.initializeConnection()
         try:
           for vehicleApproved in VehiclesApproved:
                insertionQuery="INSERT INTO client_vehicle (idClient_Vehicle_Driver, VehicleName, idclient)  VALUES (%s,%s,%s)"
                insertionValues=(0,vehicleApproved,idclient)
                self.cursor.execute(insertionQuery,insertionValues)
                self.connection.commit()
         except db.Error as err:
                print("Something went wrong Checking Client Vehicle for the first time: {}".format(err))
                
                
    def insertIntoClientCaptainTableForTheFirstTime(self,idclient,CaptainsApproved):
#               ['idclient_captian', 'idclient', 'clientName']
        
        try:
            for captainApproved in CaptainsApproved:
                insertionQuery="INSERT INTO client_captian (idclient_captian, idclient, clientName)  VALUES (%s,%s,%s)"
                insertionValues=(0,idclient,captainApproved)
                self.cursor.execute(insertionQuery,insertionValues)
                self.connection.commit()
        except db.Error as err:
                print("Something went wrong Checking Client Captain  inserted for the first time: {}".format(err))
          
    def loadCaptainNames(self):
        try:
            captainNames=[]
            searchQuary="Select captainName from captain"
            self.cursor.execute(searchQuary)
            captainNames=[Name[0] for Name in self.cursor.fetchall()]    
            return captainNames
        except db.Error as err:
                print("Something went wrong: {}".format(err))
#        finally:
##                   if (self.connection.is_connected()):
#                       self.connection.close()
#                       self.cursor.close()
#                       print("MySQL connection is closed")           
                

    def getLatestidInsertedfromClientTable(self):
        try:
            
            query="select idcilent from client Order By idcilent DESC Limit 1"
            self.cursor.execute(query)
            latestidinserted=self.cursor.fetchall()
            return latestidinserted
        except db.Error as err:
                print("Something went wrong: {}".format(err))
                
    def loadVehiclesNames(self):
          self.initializeConnection()  
          try:
            vehicles=[]
            searchQuary="Select VehicleType from vehicle"
            self.cursor.execute(searchQuary)
            vehicles=[Name[0] for Name in self.cursor.fetchall()]
                
                 
            return tuple(vehicles)
          except db.Error as err:
                print("Something went wrong: {}".format(err))
#          finally:
#    #                   if (self.connection.is_connected()):
#                       self.connection.close()
#                       self.cursor.close()
#                       print("MySQL connection is closed")     
    
    def getCurrentClientid(self):
        currentClientid=self.getLatestidInsertedfromClientTable()
    
        if (len(currentClientid)==0 or currentClientid==None):
            currentClientid=0
        else:
            
            currentClientid=currentClientid[0][0]+1
            
        return currentClientid

    def insertIntoClientVehicleTable(self,VehiclesApproved,idcilent):
        
        try:
            for vehicleApproved in VehiclesApproved:
                if (self.isClient_VehicleTableEmpty()==True):
                    self.insertIntoClientVehcileTableForTheFirstTime(vehicleApproved,idcilent)
                else:
                        insertionIntoVehiclesApprovedQuery="INSERT INTO client_vehicle (VehicleName, idclient)  VALUES (%s,%s)"
                        insertionValues=[vehicleApproved,idcilent]
                        self.cursor.execute(insertionIntoVehiclesApprovedQuery,insertionValues)
                        self.connection.commit()
        except db.Error as err:
            print("Something went wrong in inserting Client_Vehicle: {}".format(err))
       
            
            
    def insertIntoClientCaptainTable(self,CaptainsApproved,idcilent):
        try:
            for captainApproved in CaptainsApproved:
           
                if (self.isClient_CaptainTableEmpty()==True):
                    self.insertIntoClientCaptainTableForTheFirstTime(idcilent,CaptainsApproved)
                else:
                        insertionIntoCaptainApprovedQuery="INSERT INTO client_captian ( idclient,clientName)  VALUES (%s,%s)"
                        insertionValues=[idcilent,captainApproved]
                        self.cursor.execute(insertionIntoCaptainApprovedQuery,insertionValues)
                        self.connection.commit()
        except db.Error as err:
            print("Something went wrong in inserting Client_Captain: {}".format(err))
    
    
    def insertIntoClientTable(self,Values):
# =============================================================================
#       ['idcilent', 'ClientName', 'ContantName', 'Phone', 'Email', 'ContractType', 
#        'ContractImage', 'ContractStartDate', 'ContractExpiryDate', 'Fees']
# =============================================================================
       
        idcilent=self.getCurrentClientid()
        ClientName=Values[0]
        ContantName=Values[1]
        Phone=Values[2]
        Email=Values[3]
        ContractType=Values[4]
        ContractImage=self.convertImageToBinaryData(Values[5])
        ContractStartDate=Values[6]
        ContractExpiryDate=Values[7]
        Fees=Values[8]
        VehiclesApproved=Values[9]
        CaptainApproved=Values[10]
       

        VehiclesApproved=Values[9]
        CaptainApproved=Values[10]
        
        
      
        
        insertIntoClientQuery="""INSERT INTO client (idcilent, ClientName, ContantName, Phone, Email, ContractType, 
        ContractImage, ContractStartDate, ContractExpiryDate, Fees) VALUES 
                                                                    ( %s ,  %s ,  %s ,  %s ,  %s ,  %s ,  %s ,  %s ,  %s ,  %s )"""
        
        Clientvalues=[ idcilent ,  ClientName ,  ContantName ,  Phone ,  Email ,  ContractType ,  ContractImage ,  ContractStartDate ,  ContractExpiryDate ,  Fees ]
        try:
             self.cursor.execute(insertIntoClientQuery,Clientvalues)
             self.connection.commit()
             self.insertIntoClientVehicleTable(VehiclesApproved,idcilent) #closeConnection
             self.insertIntoClientCaptainTable(CaptainApproved,idcilent)
             
        except db.Error as err:
            print("Something went wrong in inserting Client: {}".format(err))
        finally:
                self.connection.close()
                self.cursor.close()
                print("MySQL connection is closed")    
                        
   
        
        
        
if __name__ == "__main__":
    x=RentalCarClientdb()
    x.getCurrentClientid()
    