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

    apartmentList = []

    def fetchApartment(self):
        for i in range(len(ApartmentBroker().deserializeAccount())):
            self.apartmentList.append(ApartmentBroker().deserializeAccount()[i])
        
        for apartment in self.apartmentList:     

            if apartment["unitAvailable"] == True:

                print("Apartment: " + str(apartment["apartmentNum"]))
                print("Unit Area: " + str(apartment["unitArea"]))
                print("Number of Bedrooms: " + str(apartment["numOfBedroom"]))
                print("Number of Baths: " + str(apartment["numOfBath"]))

                if apartment["balconyAvailable"] == True:
                    print("Balcony: Available")
                else:
                    print("Balcony: Not Available")

                if apartment["inSuiteLaundry"] == True:
                    print("In Suite Laundry: Available\n")
                else:
                    print("In Suite Laundry: Not Available\n")
                

            
class NewAccountCreation:

    username = None
    password = None
    email = None

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

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




        