print("Replit Login System")
import getpass
real_user = "Ritwik"
real_password = "password"

def login():
  
  while True:
    username = input("What is your username? ")
    password = getpass.getpass(prompt= "What is your password? ")
    if username == real_user and password == real_password:
      print("Welcome to Replit! You are logged in!")
      print("You are being taken away from login screen now")
      break
    else:
      print("Try again! Username and password not recognised")
      continue

login()


  