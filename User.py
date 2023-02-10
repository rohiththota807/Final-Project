import sys
import random
import json
import time


class User:
    def __init__(self) :
        
        self.register = {}
        self.id = "B_01"
    def Registered(self):
        name  = input("Enter Your Name :")
        mobile = int(input("Enter Your Mobile Num :"))
        email = input("Enter Your Mail ID :")
        address = input("Enter Your Address :")
        password = (input("Enter Your Password :"))
        self.d={"Name":name,"Mobile":mobile,"Email ID":email,"Address":address,"Password":password}
        self.register[self.id] = self.d
        with open("user_details.json","w") as f:
            json.dump(self.register,f,indent=4)
            print("Registered Sucessfully")
            time.sleep(2)
            print()
            print(self.register)
            print("Your Email ID and Password is Your Login ID and Password")
            return "Now Login"
    
    def login(self,email,password):
        with open("user_details.json","r") as f:
            self.tem = json.load(f)    
        if email == self.tem[self.id]["Email ID"]:
            if password == self.tem[self.id]["Password"]:
                return "Login Sucessfully"
            else:
                 return "Invalid Password Login Again"
        else:
            print("You are Not our exiting coustomer\n")
            time.sleep(2)
            print("You have to Registerd First")
            return ""
    
    def update_profile(self):
        print("*"*140)
        print("------->>>Press 1 for Update Name")
        print("------->>>Press 2 for Update Mobile Number")
        print("------->>>Press 3 for Update Email ")
        print("------->>>Press 4 for Update Address")
        print("------->>>Press 5 for Update Password")
        print("------->>>>Press 0 for exit")
        print("*"*140)
        press = input("Please Enter a Button :")

        if press == "1":
            ename = input("Enter Your Update Name :")
            self.tem[self.id]['Name']=ename
            with open("user_details.json","w") as f:
                json.dump(self.tem,f,indent=4)
            print("Your Updated Profile is",self.tem[self.id])
        
        if press == "2":
            emobile = input("Enter Your Update Mobile :")
            self.tem[self.id]['Mobile']=emobile
            with open("user_details.json","w") as f:
                json.dump(self.tem,f,indent=4)
            print("Your Updated Profile is",self.tem[self.id])

        if press == "3":
            email = input("Enter Your Update Mobile :")
            self.tem[self.id]['Mobile']=email
            with open("user_details.json","w") as f:
                json.dump(self.tem,f,indent=4)
            print("Your Updated Profile is",self.tem[self.id])
    
        if press == "4":
            address = input("Enter Your Update Mobile :")
            self.tem[self.id]['Mobile']=address
            with open("user_details.json","w") as f:
                json.dump(self.tem,f,indent=4)
            print("Your Updated Profile is",self.tem[self.id])

        if press == "5":
            passw = input("Enter Your Update Mobile :")
            self.tem[self.id]['Mobile']=passw
            with open("user_details.json","w") as f:
                json.dump(self.tem,f,indent=4)
            print("Your Updated Profile is",self.tem[self.id])
        
        if press=="0":
            time.sleep(2)
            print("Your Profile Got Update ")
            sys.exit()

