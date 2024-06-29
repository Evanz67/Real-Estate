from Logic_Layer import *
from tkinter import *




#Initialization
root = Tk()
root.title("Real Estate")
root.geometry('720x1280')
root.resizable(False, False)

#String variables
usernameLoginString = StringVar()
passwordLoginString = StringVar()

#Create a frame
frame = Frame(root)
frameButton = Frame(root)
frameEntry = Frame(root)

#Removes the initial widget
def clearScreen():
    frame.destroy()
    frameButton.destroy()
    frameEntry.destroy()

def register(username, password, email):
    LoginSystem().register(username, password, email)
    mainPage()

def login(username, password):
    verify = LoginSystem().login(username, password)
    if verify == True:
        mainPageLogin()

def mainPage():
    clearScreen()
    global frame
    global frameEntry
    global frameButton
    global usernameLoginString
    global passwordLoginString

    frame = Frame(root)
    frameButton = Frame(root)
    frameEntry = Frame(root)

    #Label text of app
    label = Label(frame, font = ("Arial", 24), text = "Apartment List")
    usernameLabel = Label(frameEntry, font = ("Arial", 12), text = "Username: ")
    passwordLabel = Label(frameEntry, font = ("Arial", 12), text = "Password: ")

    #Entry input for app
    username = Entry(frameEntry, textvariable = usernameLoginString, font = ("Arial", 12), fg = "black")
    password = Entry(frameEntry, textvariable = passwordLoginString,  font = ("Arial", 12), show = "*", fg = "black")

    #Listbox for apartment list
    apartmentListBox = Listbox(frame,
                               height=25,
                               width=40,
                               bg = "grey",
                               activestyle = 'dotbox',
                               font = ("Arial", 16),
                               fg = "white")

    #Scrollbar for app
    scrollBar = Scrollbar(frame, orient="vertical", command = apartmentListBox.yview)
    apartmentListBox.configure(yscrollcommand = scrollBar.set)

    #Button of app
    loginButton = Button(frameButton,
                         text = "Login",
                         activebackground = "black",
                         activeforeground = "white",
                         font = ("Arial", 12),
                         height=2,
                         width=10,
                         command = lambda: login(usernameLoginString.get(), passwordLoginString.get()))

    registerButton = Button(frameButton,
                            text = "Register",
                            activebackground = "black",
                            activeforeground = "white",
                            font = ("Arial", 12),
                            height=2,
                            width=10,
                            command = registerPage)

    adminLoginButton = Button(frameButton,
                              text = "Admin Login",
                              activebackground = "black",
                              activeforeground = "white",
                              font = ("Arial", 12),
                              height=2,
                              width=10)



    #Call function to fetch apartment data from the logic layer
    ApartmentList().fetchApartment(apartmentListBox)

    #Grid geometry of the app
    frame.pack(pady=50)
    frameButton.pack(pady=25)
    frameEntry.pack()
    label.pack()
    scrollBar.pack(side = RIGHT, fill = Y)
    apartmentListBox.pack()
    loginButton.pack(side = "left", padx=(0, 10))
    adminLoginButton.pack(side = "left")
    registerButton.pack(padx=(10, 10))
    usernameLabel.pack()
    username.pack(pady=(0, 10))
    passwordLabel.pack()
    password.pack()

def registerPage():
    clearScreen()
    global frame
    global frameEntry
    global frameButton

    usernameString = StringVar()
    passwordString = StringVar()
    emailString = StringVar()

    frame = Frame(root)
    frameEntry = Frame(root)
    frameButton = Frame(root)

    registerLabel = Label(frame, font = ("Arial", 26), text = "Create Account")
    usernameLabel = Label(frameEntry, font = ("Arial", 12), text = "Username: ")
    passwordLabel = Label(frameEntry, font = ("Arial", 12), text = "Password: ")
    #passwordConfirmLabel = Label(frameEntry, font = ("Arial", 12), text = "Confirm Password: ")
    emailLabel = Label(frameEntry, font = ("Arial", 12), text = "Email: ")

    username = Entry(frameEntry, textvariable = usernameString, font = ("Arial", 12), fg = "black")
    password = Entry(frameEntry, textvariable = passwordString, font = ("Arial", 12), show = "*", fg = "black")
    #passwordConfirm = Entry(frameEntry, font = ("Arial", 12), show = "*", fg = "black")
    email = Entry(frameEntry, textvariable = emailString, font = ("Arial", 12), fg = "black")

    submitButton = Button(frameButton,
                     text = "Submit",
                     activebackground = "black",
                     activeforeground = "white",
                     font = ("Arial", 12),
                     height=1,
                     width=10,
                     command = lambda: register(usernameString.get(), passwordString.get(), emailString.get()))

    frame.pack(pady=(100, 35))
    frameEntry.pack()
    frameButton.pack()
    registerLabel.pack()
    usernameLabel.pack()
    username.pack(pady=(0, 10))
    passwordLabel.pack()
    password.pack(pady=(0, 10))
    #passwordConfirmLabel.pack()
    #passwordConfirm.pack()
    emailLabel.pack()
    email.pack()
    submitButton.pack(pady=(20, 0))

def mainPageLogin():
    clearScreen()
    global frame
    global frameEntry
    global frameButton

    frame = Frame(root)
    frameButton = Frame(root)
    frameEntry = Frame(root)

    #Label text of app
    label = Label(frame, font = ("Arial", 24), text = "Apartment List")

    #Listbox for apartment list
    apartmentListBox = Listbox(frame,
                               height=25,
                               width=40,
                               bg = "grey",
                               activestyle = 'dotbox',
                               font = ("Arial", 16),
                               fg = "white")

    #Scrollbar for app
    scrollBar = Scrollbar(frame, orient="vertical", command = apartmentListBox.yview)
    apartmentListBox.configure(yscrollcommand = scrollBar.set)

    #Button of app
    paymentButton = Button(frameButton,
                         text = "Payment",
                         activebackground = "black",
                         activeforeground = "white",
                         font = ("Arial", 12),
                         height=2,
                         width=10)
    
    calendarButton = Button(frameButton,
                            text = "Calendar",
                            activebackground = "black",
                            activeforeground = "white",
                            font = ("Arial", 12),
                            height=2,
                            width=10)

    #Call function to fetch apartment data from the logic layer
    ApartmentList().fetchApartment(apartmentListBox)

    #Grid geometry of the app
    frame.pack(pady=50)
    frameButton.pack(pady=25)
    frameEntry.pack()
    label.pack()
    scrollBar.pack(side = RIGHT, fill = Y)
    apartmentListBox.pack()
    paymentButton.pack(side = "left", padx=(0, 10))
    calendarButton.pack()

def paymentPage():
    clearScreen()
    global frame
    global frameEntry
    global frameButton

    cardTypeString = StringVar()

    frame = Frame(root)
    frameButton = Frame(root)
    frameEntry = Frame(root)

    paymentLabel = Label(frame, font = ("Arial", 24), text = "Payment")
    cardTypeLabel = Label(frameEntry, font = ("Arial", 12), text = "Card Type: ")
    cardNameHolderLabel = Label(frameEntry, font = ("Arial", 12), text = "Card Name Holder: ")
    cardNumberLabel = Label(frameEntry, font = ("Arial", 12), text = "Card Number: ")
    ccvLabel = Label(frameEntry, font = ("Arial", 12), text = "CCV: ")
    dateExpiryLabel = Label(frameEntry, font = ("Arial", 12), text = "Date Expiry: ")

    cardType= Entry(frameEntry, textvariable = cardTypeString, font = ("Arial", 12), fg = "black")
    


#-----------------------------------------------------------------Code below is a starter page for initialization----------------------------------------------------------------------------#

#Label text of app
label = Label(frame, font = ("Arial", 24), text = "Apartment List")
usernameLabel = Label(frameEntry, font = ("Arial", 12), text = "Username: ")
passwordLabel = Label(frameEntry, font = ("Arial", 12), text = "Password: ")

#Entry input for app
username = Entry(frameEntry, textvariable = usernameLoginString, font = ("Arial", 12), fg = "black")
password = Entry(frameEntry, textvariable = passwordLoginString,  font = ("Arial", 12), show = "*", fg = "black")

#Listbox for apartment list
apartmentListBox = Listbox(frame,
                           height=25,
                           width=40,
                           bg = "grey",
                           activestyle = 'dotbox',
                           font = ("Arial", 16),
                           fg = "white")

#Scrollbar for app
scrollBar = Scrollbar(frame, orient="vertical", command = apartmentListBox.yview)
apartmentListBox.configure(yscrollcommand = scrollBar.set)

#Button of app
loginButton = Button(frameButton,
                     text = "Login",
                     activebackground = "black",
                     activeforeground = "white",
                     font = ("Arial", 12),
                     height=2,
                     width=10,
                     command = lambda: login(usernameLoginString.get(), passwordLoginString.get()))

registerButton = Button(frameButton,
                        text = "Register",
                        activebackground = "black",
                        activeforeground = "white",
                        font = ("Arial", 12),
                        height=2,
                        width=10,
                        command = registerPage)

adminLoginButton = Button(frameButton,
                          text = "Admin Login",
                          activebackground = "black",
                          activeforeground = "white",
                          font = ("Arial", 12),
                          height=2,
                          width=10)



#Call function to fetch apartment data from the logic layer
ApartmentList().fetchApartment(apartmentListBox)

#Grid geometry of the app
frame.pack(pady=50)
frameButton.pack(pady=25)
frameEntry.pack()
label.pack()
scrollBar.pack(side = RIGHT, fill = Y)
apartmentListBox.pack()
loginButton.pack(side = "left", padx=(0, 10))
adminLoginButton.pack(side = "left")
registerButton.pack(padx=(10, 10))
usernameLabel.pack()
username.pack(pady=(0, 10))
passwordLabel.pack()
password.pack()

  
#Event checker
root.mainloop()

class Man:

    def test(self, cardType, cardHolderName, cardNumber, ccv, dateExpiry):
        Payment().pay(cardType, cardHolderName, cardNumber, ccv, dateExpiry)