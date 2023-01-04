print("WELCOME TO BRIGHTON UNIVERSITY, LOGIN WITH YOUR DETAILS")
userName=input()
password=input()
if len(userName)==0 and len(password)==0:
    print("Error: No string entered")
while len(userName)<12 and len(password)<12:
    print("Username or Password is incorrect: please re-login")
    userName=input()
    password=input()
password2=input("confirm password:  ")
while password2!=password:
    print("input type error!")
    password2=input("confirm password:  ")
print("CONGRATULATIONS! YOU CAN ACCESS BRIGHTON MATERIALS")
    
        