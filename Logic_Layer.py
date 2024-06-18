from Persistence_Layer import *
from tkinter import *
import os

class LoginSystem:

    userDetails = []

    def login(self, username, password):
        for i in range(len(AccountBroker().deserializeAccount())):
            if AccountBroker().deserializeAccount()[i]["username"] == username:
                if AccountBroker().deserializeAccount()[i]["password"] == password:
                    return True
        return False
        
                    
    def adminLogin(self):
        pass

    def register(self, username, password, email):
        if os.path.exists(str(os.getcwd()) + "\\user.json"):
    
            self.userDetails = AccountBroker().deserializeAccount()

        self.userDetails.append(NewAccountCreation(username, password, email).__dict__)
        AccountBroker().serializeAccount(self.userDetails)

class ApartmentList:

    apartmentList = []

    def fetchApartment(self, apartmentListBox):
        for i in range(len(ApartmentBroker().deserializeApartmentData())):
            self.apartmentList.append(ApartmentBroker().deserializeApartmentData()[i])
        
        for apartmentDetails in self.apartmentList:

            apartmentListBox.insert(END, "Apartment: " + str(apartmentDetails["apartmentNum"]))

            if apartmentDetails["unitAvailable"] == True:
                apartmentListBox.insert(END, "Apartment: Available")
            else:
                apartmentListBox.insert(END, "Apartment: Not available")

            apartmentListBox.insert(END, "Unit Area: " + str(apartmentDetails["unitArea"]))
            apartmentListBox.insert(END, "Number of Bedroom: " + str(apartmentDetails["numOfBedroom"]))
            apartmentListBox.insert(END, "Number of Bath: " + str(apartmentDetails["numOfBath"]))

            if apartmentDetails["balconyAvailable"] == True:
                apartmentListBox.insert(END, "Balcony: Available")
            else:
                apartmentListBox.insert(END, "Balcony: Not Available")

            if apartmentDetails["inSuiteLaundry"] == True:
                apartmentListBox.insert(END, "In Suite Laundry: Available")
            else:
                apartmentListBox.insert(END, "In Suite Laundry: Not Available")
            apartmentListBox.insert(END, " ")
                        
class Payment:
    pass
       
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




        