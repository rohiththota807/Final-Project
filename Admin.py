#print("----------------------------------------------->>>>>>>>>This is our Admin File<<<<<<<<<--------------------------------------------\n")
from datetime import datetime
import random
import time
import json
import sys


class Admin:
    def __init__(self) :
        # print("=+"*70)
        # print()
        #print("-------------------------------------------------->>>>>Welcome to Bojan App<<<<<----------------------------------------------\n")
        time.sleep(5) # This is for show the user my app logo
        self.food_id = str("B_"+"".join(random.sample('012346789',3)))
        self.add_items = {}
        self.order_list = []


    def new_food_items(self):
        self.Name = input("Enter Your food Name :")
        self.Quentity = (input("Enter Your Quentity :"))
        self.price = int(input("Enter Your Prices Here :"))
        self.Discount = int(input("Enter Your Discount Prices Here :"))
        self.stock_left = int(input("Enter Your Stock :"))
        self.d = {"Name":self.Name,"Quentity ":self.Quentity,"Price ":self.price,"Discount ":self.Discount,"Stock Left":self.stock_left}
        self.food_id = str("B_"+"".join(random.sample('012346789',3)))
        self.add_items[self.food_id]=self.d
        #self.order_list.append(self.food_id)
        with open("admin.json","w") as f:
            json.dump(self.add_items,f,indent=4)
        print()
        return "Now Call the Watch items to see your food"
    
    def order_ids(self):
        with open("admin.json",'r') as f:
            tem = json.load(f)
        for i in tem.keys():
            self.order_list.append(i)
        return self.order_list
    
    def watch_items(self):
        with open("admin.json","r") as f:
           tem = json.load(f)
        for i in tem.items():
            print(i) 
        return ""  
        
    
    def remove_items(self):
        try:
            food_key = input("Enter Your Food Id to delete the Food Items :")
        except :
            print("Invalid Food ID ❌")
        if food_key in self.add_items :
            del self.add_items[food_key]
            print("Remaining Food Items :\n",self.add_items)
            with open("admin.json","w") as f:
                json.dump(self.add_items, f,indent=4)
        else:
            print("Invalid Food ID ❌") 
            sys.exit()
        
        
    def edit_food_items(self):
        with open("admin.json","r") as f:
            self.file = json.load(f)
        try:
            food_id = input("Enter Your Food_ID Which You Want to Edit : ")
        except:
            print("Please Enter a Correct Food_ID")
        if food_id in self.file:
            print(self.file[food_id])
            print()
            print("Which Thing You Want to edit ❓❔\n")
            print("Name","           ","Quentity\n","Price","           ","Discount\n","Stock Left")
            while True:
                print("+-"*55)
                print("-------->>>>>1 for Name")
                print("-------->>>>>2 for Quentity")
                print("-------->>>>>3 for Price")
                print("-------->>>>>4 for Discount")
                print("-------->>>>>>5 for Stock Left")
                print("-------->>>>>>0 for exit")
                print("+-"*55)

                tem = int(input("Enter Number : "))
                if tem ==1:
                    ename = input("Enter Your New food Name :")
                    self.file[food_id]['Name'] = ename
                    with open("admin.json","w") as f:
                        json.dump(self.file, f,indent=4)
                    print("Your Update Items is \n",self.file[food_id])   

                if tem ==2:
                    eqty = (input("Enter Your Qty :"))
                    self.file[food_id]['Quentity '] = eqty
                    with open("admin.json","w") as f:
                        json.dump(self.file, f,indent=4)
                    print("Your Update Items is \n",self.file[food_id]) 

                if tem ==3:
                    eprice = int(input("Enter Your New Price :"))
                    self.file[food_id]["Price "] = eprice
                    with open("admin.json","w") as f:
                        json.dump(self.file, f,indent=4)
                    print("Your Update Items is \n",self.file[food_id])
                
                if tem ==4:
                    ediscount= int(input("Enter Your Discount Prices :"))
                    self.file[food_id]["Discount "] = ediscount
                    with open("admin.json","w") as f:
                        json.dump(self.file, f,indent=4)
                    print("Your Update Food Items is \n",self.file[food_id])

                
                if tem ==5:
                    estock = int(input("Enter New Stock :"))
                    self.file[food_id]["Stock Left"] = estock
                    with open("admin.json","w") as f:
                        json.dump(self.file,f,indent=4)
                    print("Your Updated Food Items is \n",self.file[food_id])
                
                if tem ==0:
                    print("Your Food Items Got Updated")
                    sys.exit()