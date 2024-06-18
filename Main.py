from Presentation_Layer import *


cardType = input("Card type: ")
cardHolderName = input("Name: ")
cardNumber = input("Card number: ")
ccv = input("CCV: ")
dateExpiry = input("Date Expiry: ")

Man().test(cardType, cardHolderName, cardNumber, ccv, dateExpiry)