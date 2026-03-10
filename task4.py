#BMI Calculator

'''weight=int(input("Enter Weight :"))
height=int(input("Enter Height :"))
BMI=weight/height**2
print("BMI Calculator :",BMI)'''


#Average of Three Numbers

'''a=int(input("Enter a value :"))
b=int(input("Enter b value :"))
c=int(input("Enter c value :"))
Average=(a+b+c)/3
print("Average of Three Numbers :",Average)'''

#Swapping two numbers

'''a=int(input("Enter A value :"))
b=int(input("Enter B value :"))
a,b=b,a
print("After Swapping")
print("A =",a)
print("B =",b)'''

'''a=int(input("Enter A value :"))
b=int(input("Enter B value :"))
temp=a
a=b
b=temp
print("After Swapping :")
print("A =",a)
print("B =",b)'''

#Positive/Negative/Zero

'''a=int(input("Enter a value :"))
if a>=0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Not exist")'''

#Largest of Three Numbers

'''a=int(input("Enter a value :"))
b=int(input("Enter b value :"))
c=int(input("Enter c value :"))
if a>b and b<a:
    print("Largest number is ",a)
elif b>a and b<c:
    print("Largest number is ",b)
else:
    print("Largest number is ",c)'''

#ATM Machine Program

'''pin=9999
balance=50000
user_pin=int(input("Enter the pin: "))
if user_pin==pin:
    print("Show ATM Menu")

    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")

    print("Choose Option")

    Option=int(input("Enter Option: "))
    if Option==1:
        print("Your Balance is: ",balance)

    elif Option==2:
        amount=int(input("Enter Withdraw Money: "))

        if amount<=balance:
            amount=balance-amount
            print("Withdraw was Successfull")
            print("Remaining Balance is: ",balance)

        else:
            print("Insufficient Balance")
            
    elif Option==3:
        amount=int(input("Enter Deposit amount: "))
        balance=balance+amount
        print("Deposited Successfully")
        print("Updated Balance is: ",balance)

else:
    print("Invalid Option")'''

#Student Grade System

'''marks=int(input("Enter Marks of the Student: "))
if marks>=90:
    print("Grade A: ")
elif marks>=75:
    print("Grade B: ")
elif marks>=60:
    print("Grade C: ")
elif marks>=40:
    print("Grade D: ")
else:
    print("Student Failed")'''

#Electricity Bill Calculator

'''units=int(input("Enter Electricity Units Consumed: "))
if units<=100:
    print("$2 per unit")
elif units<=200:
    print("$3 per unit")
elif units<=300:
    print("$5 per unit")
elif units>300:
    print("$7 per unit")'''

#Restaurant Order System

'''print("Welcome to Dorcas Restaurant")
print("----Restaurant Menu----")
print("1. Pizza - 200")
print("2. Burger - 120")
print("3. Sandwich - 100")
print("4. Biryani - 250")

Choice=int(input("Enter Your Choice: "))
Quantity=int(input("Enter Quantity: "))

if Choice==1:
    bill=200*Quantity
    print("Total Bill: ",bill)

elif Choice==2:
    bill=100*Quantity
    print("Total Bill :",bill)

elif Choice==3:
    bill=100*Quantity
    print("Total Bill :",bill)

elif Choice==4:
    bill=250*Quantity
    print("Total Bill :",bill)

else:
    print("Invalid Order")'''



        
                
            
        



