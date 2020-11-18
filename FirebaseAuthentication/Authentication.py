

import pyrebase
from getpass import getpass

firebaseConfig = {
  # Put your project's data.

  # Project->Settings->General->Firebase SDK snippet(config)->copy
};

# print(firebaseConfig)
firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

def SignUp():
  email=input("Enter Email:")
  password=getpass("Enter password:")
  try:
    auth.create_user_with_email_and_password(email,password)
    print("Signed up successfully\n")
    askUser=input("Want to login?[Y/N]").lower()
    if(askUser=='y'):
      Login()
  except:
    print("User already exists!")


def Login():
  email=input("Enter Email:")
  password=getpass("Enter password:")
  try:
    auth.sign_in_with_email_and_password(email,password)
    print("Logged in Successfully\n")
  except:
    print("Invalid credentials!")


def ResetPassword():
  email=input("Enter email:")
  auth.send_password_reset_email(email)
  print("Password reset successfully\n")

temp=input("Enter\n1.To SignUp\n2.Login\n3.Reset Password\n")

if(temp=='1'):
  SignUp()
elif temp=='2':
  Login()
elif temp=='3':
  ResetPassword()
else:
  print("Enter Valid optiion!\n")