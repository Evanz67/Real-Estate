from Domain_Class import *

class LoginScreen:

    def start(self):

        decision = int(input("Choose 1 for login, 2 for admin login, 3 for register: "))

        if decision == 1:
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            return LoginSystem().login(username, password) #If account is verified, return 1 if not return 0
                       
        elif decision == 2:
            return 2

        elif decision == 3:
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            email = input("Enter an email: ")       
            LoginSystem().register(username, password, email)
            return 3       

        else:
            print("Choose only 1, 2, and 3")


class Dashboard:

    def lookApartment(self):
        ApartmentList().fetchApartment()


class AdminDashboard:

    pass