#By using if condition
'''user_no=34
if user_no>0:
    print("Positive Num")'''


#By using if-else condition
'''age=int(input("Enter Age of Person"))
if age>=18:
        print("Eligible for Voting")
else:
    print("Not Eligible")'''


'''n=int(input())
if n%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible")'''


'''n=int(input())
if n%2==0:
    print("Even")
else:
    print("Odd")'''


'''marks=int(input("Enter Marks"))
if marks>=35:
    print("Pass")
else:
    print("Fail")'''


#By using if-elif condition
'''marks=int(input("Enter Marks"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks<60:
    print("Grade D")'''


'''color=str(input("Enter Color"))
if color=="Red":
    print("Stop")
elif color=="Yellow":
    print("Get Ready")
elif color=="Green":
    print("Go")'''

#By using if-elif-else condition

'''a=30;b=40;c=60
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)'''

'''a=int(input("Enter A"))
b=int(input("Enter B"))
c=int(input("Enter C"))
if a>b and a>c:
    print(a)
elif b>a or b>c:
    print(b)
else:
    print(c)'''

'''a=int(input("Enter A"))
b=int(input("Enter B"))
c=int(input("Enter C"))
if a>=b and a>=c:
    print(a)
elif b>a or b>c:
    print(b)
else:
    print(c)'''

#By using multiple-if

'''a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if a%3==0:
    print("Divisible by 3")
if b%5==0:
    print("Divisible by 5")
if c%7==0:
    print("Divisible by 7")'''

'''username=str(input("Enter Username"))
password=int(input("Enter Password"))
if username=="admin":
    print("Login Successfull")
elif password==1234:
    print("Succesfull")
else:
    print("Invalid")'''

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
elif username != "admin":
    print("Invalid Username")
else:
    print("Invalid Password")






