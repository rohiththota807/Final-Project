import sys
import time
import json
from Admin import Admin
from User import User
print("Welcome to Bhojan App\n")
time.sleep(5)
demo1 = User()
print(demo1.login("rohiththota807@gmail.com","Rohith807"))


while True:
    l = []
    rs = 0
    order_history = {}
    print("+="*70)
    print("Press P For Place New Order")
    print("Press U For Update Profile")
    print("Press H For Get History From App")
    print("Press E For Exit From App")
    print("=+"*70)
    user_input = input("Press Button :")
    if user_input ==  "P" or user_input =="p":
        with open("Admin.json","r") as f:
            temp = json.load(f)
        print("1. ",temp["B_001"]["Quentity "] ," ",temp["B_001"]["Name"],"..........................",temp["B_001"]["Price "],"Rupee")
        print("2. ",temp["B_002"]["Quentity "] ," ",temp["B_002"]["Name"],"..........................",temp["B_002"]["Price "],"Rupee")
        print("3. ",temp["B_003"]["Quentity "] ," ",temp["B_003"]["Name"],"..........................",temp["B_003"]["Price "],"Rupee")
        print("4. ",temp["B_004"]["Quentity "] ," ",temp["B_004"]["Name"],"..........................",temp["B_004"]["Price "],"Rupee")
        print("5. ",temp["B_005"]["Quentity "] ," ",temp["B_005"]["Name"],"..........................",temp["B_005"]["Price "],"Rupee")
        print("6. ",temp["B_006"]["Quentity "] ," ",temp["B_006"]["Name"],"..........................",temp["B_006"]["Price "],"Rupee")
        print("7. ",temp["B_007"]["Quentity "] ," ",temp["B_007"]["Name"],"..........................",temp["B_007"]["Price "],"Rupee")
        print("8. ",temp["B_008"]["Quentity "] ," ",temp["B_008"]["Name"],"..........................",temp["B_008"]["Price "],"Rupee")
        print("9. ",temp["B_009"]["Quentity "] ," ",temp["B_009"]["Name"],"..........................",temp["B_009"]["Price "],"Rupee")
        print("10. ",temp["B_010"]["Quentity "] ," ",temp["B_010"]["Name"],"..........................",temp["B_010"]["Price "],"Rupee")
        print("11. ",temp["B_011"]["Quentity "] ," ",temp["B_011"]["Name"],"..........................",temp["B_011"]["Price "],"Rupee")
        print("12. ",temp["B_012"]["Quentity "] ," ",temp["B_012"]["Name"],"..........................",temp["B_012"]["Price "],"Rupee")
        print("Press 0 for End ")
        print()
        print(">>>>>Press 999 For Place Your Order <<<<")
        ch = 1
        while ch!=0:
            ch = int(input(" Press Button For Order----> "))
            if ch==1 :
                rs+=240
                l.append(temp["B_001"]["Name"])

            elif ch==2:
                rs+=320
                l.append(temp["B_002"]["Name"])
                
            elif ch==3:
                rs+=14
                l.append(temp["B_003"]["Name"])   
            
            elif ch==4:
                rs+=12
                l.append(temp["B_004"]["Name"])
            
            elif ch==5:
                rs+=120
                l.append(temp["B_005"]["Name"])
            
            elif ch==6:
                rs+=25
                l.append(temp["B_006"]["Name"])
          
            elif ch==7:
                rs+=30
                l.append(temp["B_007"]["Name"])

            elif ch==8:
                rs+=140
                l.append(temp["B_008"]["Name"])
            
            elif ch==9:
                rs+=20
                l.append(temp["B_009"]["Name"])
            
            elif ch==10:
                rs+=25
                l.append(temp["B_010"]["Name"])
            
            elif ch==11:
                rs+=40
                l.append(temp["B_011"]["Name"])
            
            elif ch==12:
                rs+=50
                l.append(temp["B_012"]["Name"])
                        
            elif ch==999:
                print(l)
                order_history={"Order History":l,"Total Bill":rs}
                with open("history.json","w") as f:
                    json.dump(order_history,f,indent=4)
                time.sleep(2)
                print("Total Bill : - ",rs)
                print("Your Order Got Placed")
                print("You'll Get Your Order Soon")
                print()
                print("Thanks For Using App")
                break

    elif user_input=="h" or user_input=="H":
        with open("history.json","r")  as f:
            temp =json.load(f)
            print(temp)            

    elif user_input=="U" or user_input=="u":
        demo1.update_profile()

    elif user_input=="E" or user_input=="e":
        time.sleep(3)
        print("Thanks You")
        sys.exit()    
        