#Voting

'''age=int(input("Enter Age"))
if age>=18:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")'''

#Even or Odd

'''num=int(input("Enter the Value :"))
if num%2==0:
    print("It is Even")
else :
    print("It is Odd")'''

#Vowels

'''a=['a','e','i','o','u']
b=input("Enter word")
if b in a: 
    print("vowels")
else:
    print("consonents")'''

#leap year

'''year=int(input("Enter Year"))
if year%4==0:
    print("It is Leap Year")
else:
    print("It is not a Leap Year")'''

#Guest Code

'''name=str(input("Enter Name :"))
if name=="Tabitha":
    print("Welcome Tabitha")
else:
    print("Welcome Guest")'''

'''name=str(input("Enter Name :"))
if name=="Tabitha":
    print("Welcome",name)
else:
    print("Welcome Guest")'''

# 5 names Guest Code

'''names=['Tabitha','Dorcas','Joppa','Silas','Sirfy']
name=str(input("Enter Name :"))
if name in names:
    print("Welcome",name)
else:
    print("Welcome Guest")'''

#Social Media Login

'''username=str(input("Enter Username :"))
password=int(input("Enter Password :"))
if username=="Tabitha":
    if password==9999:
        print("Login Successfull")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")'''

'''username=str(input("Enter Username :"))
password=int(input("Enter Password :"))
if username=="Tabitha":
    if password==9999:
        print("Login Successfull")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")'''

#if we enter username wrong it should not have to go to next step

'''username=str(input("Enter Username :"))
password=int(input("Enter Password :"))
if username=="Tabitha" and password==9999:
        print("Login Successfull")
else:
        print("Invalid Credentials")'''

#Using if-elif-else Login system

'''username = "Dorcas"
password = "9999"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login Successful")
elif u != username:
    print("Invalid Username")
else:
    print("Invalid Password")'''


#Using Multiple-if Login System

'''u=str(input("Enter Username :"))
p=int(input("Enter Password :"))
if u=="Dorcas" and p==9999:
    print("Login Successfull")
if u!="Dorcas":
    print("Inavlid Username")
if u=="Dorcas" and p!=9999:
    print("Invalid Password")'''


#Using Nested-if Login System

'''u=str(input("Enter Username :"))
p=int(input("Enter Password :"))
if u=="Dorcas":
    if p==0000:
        print("Login Successfull")
    elif p!=0000:
        print("Invalid Password")
else:
    print("Invalid Username")'''

'''u=str(input("Enter Username"))
p=int(input("Enter Password"))
if u=="Tabitha":
    if p==0000:
        print("Login Successfull")
    elif p!=0000:
        print("Invalid Password")
    else:
        print("Check Password")
elif u!="Tabitha":
    print("Invalid Username")
else:
    print("Login Failed")'''

#Positive and Negative Numbers

'''num=int(input("Enter Num"))
if num>=0:
    print("Positive")
elif num==0:
    print("Equal")
elif num<0:
    print("Negative")
else:
    print("Not Equal")'''

#Bakery Cake and its Prices using if-elif

'''print("Welcome to Bakery")
price=int(input("Enter Price :"))
if price==1200:
    print("Red Velvet")
elif price==1000:
    print("Choco Almond")
elif price==800:
    print("Butter Scotch")
elif price==600:
    print("Normal Cake")
else:
    print("Sorry Cake is not Available")'''

#Pizzas and Price

print("Welcome to Hungry")
pizza=str(input("What type of pizza :"))
if pizza=="Crispy Chicken Pizza":
    print("Its Price is 250")
elif pizza=="Panner Pizza":
    print("Its Price is 200")
elif pizza=="Popcorn Pizza":
    print("Its Price is 150")
elif pizza=="Cheese Pizza":
    print("Its Price is 130")
else:
    print("Not Available")





    
         
        





           
          






