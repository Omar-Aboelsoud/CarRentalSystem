# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:05:18 2019

@author: oaboe
"""
import pymysql as db
class RentalCarCommonDatabase:
    
    def __init__(self):
        self.initializeConnection()

    def initializeConnection(self):
        try:
          self.connection = db.connect(user='root',password='admin', database='carrent')
          self.cursor = self.connection.cursor()
          
        except db.Error as err:
            print("Something went wrong: {}".format(err))


    def convertImageToBinaryData(self,filename):
    # Convert digital data to binary format
        if(filename!=''):
            with open(filename, 'rb') as file:
                binaryData = file.read()
            return binaryData
        else:
            return filename
    
    def convertNoneToEmptyString(self, values):
        for i in range (len(values)):
            if values[i]==None:
                values[i]=''
        return values
    
#    
#    def AddVehicleToClient(self):
#        insertionQuary="Select idcleint from 
    
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
          finally:
#                   if (self.connection.is_connected()):
                       self.connection.close()
                       self.cursor.close()
                       print("MySQL connection is closed")
    def loadCaptainNames(self):
        self.initializeConnection()  
        try:
            captainNames=[]
            searchQuary="Select captainName from captain"
            self.cursor.execute(searchQuary)
            captainNames=[Name[0] for Name in self.cursor.fetchall()]    
            return captainNames
        except db.Error as err:
                print("Something went wrong: {}".format(err))
        finally:
#                   if (self.connection.is_connected()):
                       self.connection.close()
                       self.cursor.close()
                       print("MySQL connection is closed")
    
    def insertDataIntoVehicleTable(self,Values):
# =============================================================================
#         Check if CarPlate Number is already exsis in the recored before insertion
#           if the the recored is exist , fetch the recored and display it 
# =============================================================================
       #   ['CarPlateNumber', 'CarPlateNumberExpiryDate', 'VehilceType', 'PerodicalMaintaince', 'OwnerName', 'LicenseNumberImage', 'CarImage', 'OwnerIDImage',
#    'InitialValue', 'DepreciationPeriod', 'FinalValue', 'Phone', 'Email', 'ContractType', 'ContractImage', 'ContractStartDate', 'ContractExpiryDate', 
#   'DateOfStartService', 'KMAtServiceStart', 'InsurancePolicyImage', 'InsuranceExpiryDate', 'ArchiveData']       
# =============================================================================
           self.initializeConnection()
           CarPlateNumber=Values[0]
           CarPlateNumberExpiryDate=Values[1]
           VehilceType=Values[2]
           PerodicalMaintaince=Values[3]
           OwnerName=Values[4]
           LicenseNumberImage=self.convertImageToBinaryData(Values[5])
           CarImage=self.convertImageToBinaryData(Values[6])
           if (Values[7] !=''):
               OwnerIDImage=self.convertImageToBinaryData(Values[7])
           else:
               OwnerIDImage=Values[7]
           InitialValue=Values[8]
           DepreciationPeriod=Values[9]
           FinalValue=Values[10]
           Phone=Values[11]
           Email=Values[12]
           ContractType=Values[13]
           ContractImage=self.convertImageToBinaryData(Values[14])
           ContractStartDate=Values[15]
           ContractExpiryDate=Values[16]
           DateOfStartService=Values[17]
           KMAtServiceStart=Values[18]
           InsurancePolicyImage=self.convertImageToBinaryData(Values[19])
           InsuranceExpiryDate=Values[20]
           
           
           try:
              insertQuary=""" INSERT INTO vehicle
                                  (CarPlateNumber,CarPlateNumberExpiryDate,VehilceType,PerodicalMaintaince,OwnerName,CarPlateImage,CarImage,OwnerIDImage,InitialValue,DepreciationPeriod,FinalValue,Phone,Email,ContractType,ContractImage,ContractStartDate,ContractExpiryDate,DateOfStartService,KMAtServiceStart,InsurancePolicyImage,InsuranceExpiryDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
              insertionValues=(CarPlateNumber,CarPlateNumberExpiryDate,VehilceType,PerodicalMaintaince,OwnerName,LicenseNumberImage,CarImage,OwnerIDImage,InitialValue,DepreciationPeriod,FinalValue
                             ,Phone,Email,ContractType,ContractImage,ContractStartDate,ContractExpiryDate,DateOfStartService,KMAtServiceStart,InsurancePolicyImage
                             ,InsuranceExpiryDate)
               
              self.cursor.execute(insertQuary, insertionValues)
              self.connection.commit()
           except db.Error as err:
                print("Something went wrong: {}".format(err))
           finally:
#                   if (self.connection.is_connected()):
                       self.connection.close()
                       self.cursor.close()
                       print("MySQL connection is closed")
           
    
    


    def getLatestidInsertedfromClientTable(self):
        
        try:
            
            query="select idcilent from client Order By idcilent DESC Limit 1"
            self.cursor.execute(query)
            latestidinserted=self.cursor.fetchall()
            return latestidinserted
        except db.Error as err:
                print("Something went wrong: {}".format(err))
        finally:
                self.connection.close()
                self.cursor.close()
                print("MySQL connection is closed")
                
    def getLatestidInsertedfromVehicleTable(self):
        
        self.initializeConnection()
        try:
            
            query="select idVehicle from vehicle Order By idVehicle DESC Limit 1"
            self.cursor.execute(query)
            latestidinserted=self.cursor.fetchall()
            return latestidinserted
        except db.Error as err:
                print("Something went wrong: {}".format(err))
#        finally:
#                self.connection.close()
#                self.cursor.close()
#                print("MySQL connection is closed")            
                
    def getCurrentClientid(self):
        currentClientid=self.getLatestidInsertedfromClientTable()
        if (len(currentClientid)==0 or currentClientid==None):
            currentClientid=0
        else:
            currentClientid[0]=+1
            
        return currentClientid
    
    def isClient_VehicleTableEmpty(self):
        
        self.initializeConnection()
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
#        finally:
#                self.connection.close()
#                self.cursor.close()
#                print("MySQL connection is closed")
                

#        finally:
#                self.connection.close()
#                self.cursor.close()
#                print("MySQL connection is closed")    
                
    

#                    
#        
#    def insertIntoClientTable(self,Values):
## =============================================================================
##       ['idcilent', 'ClientName', 'ContantName', 'Phone', 'Email', 'ContractType', 
##        'ContractImage', 'ContractStartDate', 'ContractExpiryDate', 'Fees']
## =============================================================================
#        self.initializeConnection()
#        idcilent=self.getCurrentClientid()
#        ClientName=Values[0]
#        ContantName=Values[1]
#        Phone=Values[2]
#        Email=Values[3]
#        ContractType=Values[4]
#        ContractImage=self.convertImageToBinaryData(Values[5])
#        ContractStartDate=Values[6]
#        ContractExpiryDate=Values[7]
#        Fees=Values[8]
#        VehiclesApproved=Values[9]
#        CaptainApproved=Values[10]
#        
#      
#        
#        insertIntoClientQuery="""INSERT INTO client (idcilent, ClientName, ContantName, Phone, Email, ContractType, 
#        ContractImage, ContractStartDate, ContractExpiryDate, Fees) VALUES 
#                                                                    ( %s ,  %s ,  %s ,  %s ,  %s ,  %s ,  %s ,  %s ,  %s ,  %s )"""
#        
#        Clientvalues=[ idcilent ,  ClientName ,  ContantName ,  Phone ,  Email ,  ContractType ,  ContractImage ,  ContractStartDate ,  ContractExpiryDate ,  Fees ]
#        try:
#             self.initializeConnection()
#             self.cursor.execute(insertIntoClientQuery,Clientvalues)
#             self.insertIntoClientVehicleTable(VehiclesApproved,idcilent) #closeConnection
#             self.insertIntoClientCaptainTable(CaptainApproved,idcilent)
#        except db.Error as err:
#            print("Something went wrong in inserting Client: {}".format(err))
##        finally:
##                self.connection.close()
##                self.cursor.close()
##                print("MySQL connection is closed")    
##                        
#                
                
       
        
    def DescribeTable(self):
        self.cursor.execute("SHOW columns FROM client_captian")
        print ([column[0] for column in self.cursor.fetchall()])
        
    def IsRecoredExistVehicle(self,value):
        if(value!=''):
              try:
                quary="SELECT * from vehicle where CarPlateNumber=%s"
                fieldText=value
                self.cursor.execute(quary,fieldText)
                self.connection.commit()
                record=self.cursor.fetchone()
                return True,record 
              except db.Error as err:
                   print("Something went wrong: {}".format(err))
                   return False,None
               
    

               
            
                     
                       
                      
        
        
    def printAllDatainVehicleTable(self):
    
        searchQuary=("SELECT * FROM client")
        self.cursor.execute(searchQuary)
        records = self.cursor.fetchall()
        print(records)
        
    
        
        
if __name__ == "__main__":
    x=RentalCarCommonDatabase()
#    x.printAllDatainVehicleTable()
#    _id=x.getCurrentClientid()
#    print(_id)
    
    
     
#    x.insertDataIntoVehicleTable(z)
        