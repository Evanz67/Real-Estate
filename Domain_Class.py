from Persistent_Class import *
import os

class LoginSystem:

    userDetails = []

    def login(self, username, password):
        for i in range(len(AccountBroker().deserializeAccount())):
            if AccountBroker().deserializeAccount()[i]["username"] == username:
                if AccountBroker().deserializeAccount()[i]["password"] == password:
                    return 1
        return 0
        
                    
    def adminLogin(self):
        pass

    def register(self, username, password, email):
        if os.path.exists(str(os.getcwd()) + "\\user.json"):
    
            self.userDetails = AccountBroker().deserializeAccount()

        self.userDetails.append(NewAccountCreation(username, password, email).__dict__)
        AccountBroker().serializeAccount(self.userDetails)

class ApartmentList:

    apartmentDetails = []

    def fetchApartment(self):
        for i in range(len(ApartmentBroker().deserializeAccount())):
            self.apartmentDetails.append(ApartmentBroker().deserializeAccount()[i])
        
        for i in range(len(self.apartmentDetails)):
            print(self.apartmentDetails[i])
        
        


class NewAccountCreation:

    username = None
    password = None
    email = None

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email



class ApartmentData:

    unitArea = None
    unitAvailable = None
    numOfBedroom = None
    numOfBath = None
    balconyAvailable = None
    inSuiteLaundry = None

    def __init__(self, unitArea, unitAvailable, numOfBedroom, numOfBath, balconyAvailable, inSuiteLaundry):
        self.unitArea = unitArea
        self.unitAvailable = unitAvailable
        self.numOfBedroom = numOfBedroom
        self.numOfBath = numOfBath
        self.balconyAvailable = balconyAvailable
        self.inSuiteLaundry = inSuiteLaundry

class BuildingData:

    gym = None
    bbqArea = None
    outdoorPool = None
    bikeStorage = None #This is optional
    parking = None #This is optional

    def __init__(self, gym, bbqArea, outdoorPool, bikeStorage, parking):
        self.gym = gym
        self.bbqArea = bbqArea
        self.outdoorPool = outdoorPool
        self.bikeStorage = bikeStorage
        self.parking = parking




        