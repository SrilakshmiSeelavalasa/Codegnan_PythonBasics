#Difference b/w break, continue and pass

#Def - The break statement is used to terminate the entire loop
#Def - The continue statement is used to skips the current iteration and rest of the code will continue
#Def - A pass statement is a null statement, it does nothing but syntatically we need

#break

'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a,end=" ")'''

'''for i in range(25):
    if i==15:
        break
    print(i,end=" ")'''


'''course="python"
if course=="t":
    break
print("course")'''#error, break not possible for conditions


'''course="Python"
for i in course:
    if i=="o":
        break
    print(i,end=" ")'''


#continue

'''a=20
while a>1:
    print(a)
    a=a-1
    if a==10:
        continue'''#its not correct

'''a=20
while a>1:
    a=a-1
    if a==10:
        continue
    print(a)'''

'''a=20
while a>1:
    a=a-1
    if a==10:
        continue
    print(a)
    break'''

'''for i in range(15):
    if i==12:
        continue
    print(i,end=" ")'''

'''a="Python"
for i in a:
    if i=="t":
        continue
    print(i,end=" ")'''


#pass

'''a=20
while a>2:
    print(a)
    a=a-1
    if a==10:
        pass'''

'''for i in range(15):
    if i==5:
        pass
    print(i)'''


'''course="python"
for i in course:
    if i=="o":
        pass
    print(i)'''
    
    
