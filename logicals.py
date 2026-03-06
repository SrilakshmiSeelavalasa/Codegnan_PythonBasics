#if-condition by using Logical Operators

'''a=3
b=6
if a<b and b>a:
    print("True")'''

'''a=3
b=6
if a<=b and b>=a:
    print("True")'''

''''a=3
b=6
if a>b or b>a:
    print("True")'''

'''a=3
b=6
if a>b and b<a:
    print("True")'''

'''a=3
b=6
if not b<a:
    print("True")'''


'''a=3
b=6
if not a>b and b>a:
    print("True")'''

'''a=3
b=6
if not a>=b or a==b:
    print("True")'''

#run-time inputs

'''a=int(input("Enter a value"))
if a>20:
    print("yes")'''

'''a=int(input("Enter a value"))
b=int(input("Enter b value"))
if a>20 and b<20:
    print("yes")'''

'''a=int(input("Enter a value"))
b=int(input("Enter b value"))
if a>b and a==b:
    print("Equal")'''


'''a=input("Data1")
b=input("Data2")
if a=="Python" and b=="Java":
    print("True")'''


'''fname=input("First Name")
lname=input("Last Name")
if fname=="Tabitha" and lname=="Dorcas":
    print("Its Her Name")'''

#if-condition by using Identify Operators
#is is not

'''a=5
if type(a) is int:
    print("Its Integer")'''

'''a=60
if type(a) is not int:
    print("Its not Integer")'''

'''a=5.4
if type(a) is not int:
    print("Its not Integer")'''

'''a=5.6
if type(a) is float:
    print("Its Float")'''

'''a=60
if type(a) is str:
    print("Its String")'''

'''name="Dorcas"
if type(name) is str:
    print("Its her name")'''


'''Data=str(input("Enter Her Name"))
if type(Data) is str:
    print("Her Name")'''

'''Data=str(input("Enter Her Name"))
if type(Data) is complex:
    print("Her Name")'''

'''a=input("Data")
if type(a) is str:
    print("String")'''

'''a=input("Enter a value")
if type(a) is complex:
    print("Its complex")'''

'''a=3+4j
if type(a) is complex:
    print("yes")'''

#if-condition by using Membership Operators
#in not in

'''a=2,4,6,8,10,12,14,16,18,20
if 14 in a:
    print("yes")'''

'''a=2,4,6,8,10,12,14,16,18,20
if 16 not in a:
    print("yes")'''

#run-time input

'''a=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=int(input("Enter a value"))
if b in a:
    print("Yes")'''

'''a=2,3,4,5,6,7,8,9,10,11,12,13,14,15
b=int(input("Enter a value"))
if b in a:
    print("Yes")'''

#if-else conditions by using Logical Operators

'''a=3
b=4
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=3
b=4
if a>=b and b>=a:
    print("true")
else:
    print("false")'''

'''a=3
b=4
if a==b or b>=a:
    print("true")
else:
    print("false")'''

'''a=3
b=4
if a==b or b<=a:
    print("true")
else:
    print("false")'''

'''a=5
b=8
if not a>=b and b>=a:
    print("true")
else:
    print("false")'''

'''a=3
b=4
if a>=b or b==a:
    print("true")
else:
    print("false")'''

#if-else with Identify Operators

'''a=4
if type(a) is int:
    print("true")
else:
    print("false")'''

'''a=4.0
if type(a) is int:
    print("true")
else:
    print("false")'''

'''a="sri"
if type(a) is int:
    print("true")
else:
    print("false")'''

'''a="sri"
if type(a) is not int:
    print("true")
else:
    print("false")'''

#if-else with Membership Operators

'''a=2,3,4,5,6,7
if 7 in a:
    print("true")
else:
    print("false")'''

'''a=2,3,4,5,6,7
if 12 in a:
    print("true")
else:
    print("false")'''

'''a=2,3,4,5,6,7
if 7 not in a:
    print("true")
else:
    print("false")'''

'''a=2,3,4,5,6,7
if 12 not in a:
    print("true")
else:
    print("false")'''

#if-elif condition using Logical Operators
#and or not

'''a=4
b=6
if a>b:
    print("Greater")
elif a==b:
    print("Not Equal")'''

'''a=4
b=6
if a<b:
    print("Greater")
elif a==b:
    print("Not Equal")'''

'''a=4
b=6
if a>=b:
    print("Greater")
elif a==b:
    print("Not Equal")
elif a>b:
    print("True")'''

'''a=4
b=6
if a>=b:
    print("Greater")
elif a==b:
    print("Not Equal")
elif a<b:
    print("True")'''

'''a=4
b=6
if not a>=b:
    print("Greater")
elif a==b:
    print("Not Equal")
elif a>b:
    print("True")'''

'''a=4
b=6
if a>=b:
    print("Greater")
elif not a==b:
    print("Not Equal")
elif a>b:
    print("True")'''

#if-elif using Identify Operators
#is is not

'''a=45
if type(a) is int:
    print("True")
elif type(a) is not int:
    print("False")'''

'''a=45
if type(a) is float:
    print("True")
elif type(a) is not float:
    print("False")'''

#run-time input
'''a=int(input("Enter a value"))
if type(a) is int:
    print("Integer")
elif type(a) is float:
    print("Float")'''

#if-elif using Membership Operator
# in not in

'''a=4,2,3,6,7,8
if 9 not in a:
    print("present")
elif 3 not in a:
    print("Not Present")'''

'''a=5,10,15,20,25,30,35,40,45
if 25 in a:
    print("present")
elif 33 in a:
    print("Not Present")'''

#run-time input

'''a=5,10,15,20,25,30,35,40
b=int(input("Enter a value"))
if 15 in a:
    print("Present")
elif 22 in a:
    print("Not Present")'''

'''a=5,10,15,20,25,30,35,40
b=int(input("Enter a value"))
if 11 in a:
    print("Present")
elif 25 in a:
    print("Not Present")'''


#if-elif-else using Logical Operators
#and or not

'''a=10
b=20
if a>b:
    print("Greater")
elif b>a:
    print("Yes Greater")
else:
    print("No")'''

'''a=10
b=20
if a>b:
    print("Greater")
elif b==a:
    print("Yes Greater")
else:
    print("No")'''

'''a=10
b=20
if a>b and b<a:
    print("Greater")
elif b>a and b==a:
    print("Yes Greater")
else:
    print("No")'''

'''a=10
b=20
if a>b or a<b:
    print("Greater")
elif b>a:
    print("Yes Greater")
else:
    print("No")'''

'''a=10
b=20
if a>b:
    print("Greater")
elif not b==a:
    print("Yes Greater")
else:
    print("No")'''

#run-time input

'''a=int(input("Enter a value"))
b=int(input("Enter b value"))
if a>b:
    print("Greater")
elif b>a:
    print("Yes Greater")
else:
    print("No")'''

'''name=str(input("Enter Fname"))
if name=="Tabitha":
    print("Fname")
elif name=="Dorcas":
    print("Lname")
else:
    print("No")'''


'''name=str(input("Enter Fname"))
if name=="Tabitha":
    print("Fname")
elif name=="Dorcas":
    print("Lname")
else:
    print("No")'''

#if-elif-else using Identify Operators
#is is not
'''name="Tabitha"
if type(name) is str:
     print("Hi Tabitha")
elif type(name) is int:
    print("Hi Int")
else:
    print("Wrong")'''

#if-elif-else using Membership Operators
#in not in

'''a=2,3,4,5,6,7
if 3 in a:
    print("True")
elif 4 in a:
    print("Present")
else:
    print("No")'''

'''a=2,3,4,5,6,7
if 8 in a:
    print("True")
elif 4 in a:
    print("Present")
else:
    print("No")'''

'''a=2,3,4,5,6,7
if 9 in a:
    print("True")
elif 12 in a:
    print("Present")
else:
    print("No")'''

'''a=2,3,4,5,6,7
if 3 not in a:
    print("True")
elif 4 in a:
    print("Present")
else:
    print("No")'''


#multiple-if using Logical Operators
#and or not

'''a=9
b=12
if a<b:
    print("less")
if b>a:
    print("Greater")
if a!=b:
    print("Not Equal")'''


#multiple-if using Identify Operators
#is is not

'''a=3
b=5
if a>b:
    print("true")
if a==b:
    print("not true")
if a<b:
    print("true true")'''

'''a=3
b=5
if a<b:
    print("true")
if a!=b:
    print("not true")
if a==b:
    print("true true")'''

#multiple-if using Membership Operators
#in not in

'''a=12,13,14,15,16,17,18,19,20
if 12 in a:
    print("Yes")
if 14 in a:
    print("Yes Yes")
if 16 in a:
    print("Yes Yes Yes")'''

'''a=12,13,14,15,16,17,18,19,20
if 12 not in a:
    print("Yes")
if 14 in a:
    print("Yes Yes")
if 16 in a:
    print("Yes Yes Yes")'''

a=12,13,14,15,16,17,18,19,20
if 24 not in a:
    print("Yes")
if 14 not in a:
    print("Yes Yes")
if 16 in a:
    print("Yes Yes Yes")





    

    
    


