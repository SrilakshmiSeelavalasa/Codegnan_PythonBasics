Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String methods
#len()

a="codegnan"
len(a)
8
b="Python Course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1

#count()

a="Twinkle Twinkle Little Star"
count(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("Twinkle")
2
a.count("T")
2
a.count("t")
3
a.count("k")
2
a.count("l")
3

a.count("z")
0

#find a string

a="Python"
a[1]
'y'
a[0]
'P'
a.find(n)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.find(n)
NameError: name 'n' is not defined
a.find("n")
5
a[5]+a[7]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a[5]+a[7]
IndexError: string index out of range
b="codegnan"
a.find('n')
5
a.find("o")
4
b.find("n")
5
b.find("o")
1
b[5]+b[7]
'nn'

#Escape Sequences
# \n - new line
# \t - tab space

a="name\nmobileno\tmailid\ncity
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobileno\tmailid\ncity"
print(a)
name
mobileno	mailid
city
a="fname=Dorcas\tlname:Tabitha\nmobileno:9000\nmaildid:tabitha@codegnan.com\ncity:Joppa\tpincode:534222"
print(a)
fname=Dorcas	lname:Tabitha
mobileno:9000
maildid:tabitha@codegnan.com
city:Joppa	pincode:534222
a="fname=Dorcas\tlname:Tabitha\n\nmobileno:9000\n\nmaildid:tabitha@codegnan.com\n\ncity:Joppa\tpincode:534222"
print(a)
SyntaxError: multiple statements found while compiling a single statement

print(a)
fname=Dorcas	lname:Tabitha
mobileno:9000
maildid:tabitha@codegnan.com
city:Joppa	pincode:534222
a="fname:Dorcas\tlname:Tabitha\nmobileno:9000\nmaildid:tabitha@codegnan.com\ncity:Joppa\tpincode:534222"
print(a)
fname:Dorcas	lname:Tabitha
mobileno:9000
maildid:tabitha@codegnan.com
city:Joppa	pincode:534222

#Replace

a="Wait until you get succeed"
a.replace("Wait","Workhard")
'Workhard until you get succeed'
a="Wait wait until you get succeed"
a.replace("Wait","Workhard")
'Workhard wait until you get succeed'
a="wait wait for me"
a.replace("wait","come and")
'come and come and for me'
a.replace("wait","come and",1)
'come and wait for me'

#upper()

a="hello"
a.upper()
'HELLO'

name="sri"
name.upper()
'SRI'

#lower()

b="HI"
b.lower()
'hi'

name="LUCKY"
name.lower()
'lucky'

#capitalize()

c="Python"
c="python"
c.capitalize()
'Python'

name="tabitha"
name.capitalize()
'Tabitha'

#title()

d="python course"
d.title()
'Python Course'

name="tabitha dorcas"
name.title()
'Tabitha Dorcas'

#True or False for upper and lower

a="code"
a.islower()
True
a.isupper()
False
a.startswith("c")
True
a.endswith("e")
True
a.isalpha()
True

b="Python Course"
b.isalpha()
False
b.istitle()
True
b.iscapitalize()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    b.iscapitalize()
AttributeError: 'str' object has no attribute 'iscapitalize'. Did you mean: 'capitalize'?
b.isdigit()
False


c=1234
c.isdigit()
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    c.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'

c="1234567"
c.isdigit()
True
c.isnum()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    c.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
c.isalnum()
True
c.isalpha()
False

d="sri@9000"
d.isalnum()
False
d.isalpha()
False

e="sri1234"
e.isdigit()
False
e.isalnum()
True

#strip()
#lstrip(), rstrip()

a="        Tabitha        "
a.strip()
'Tabitha'
a.lstrip()
'Tabitha        '
a.rstrip()
'        Tabitha'

#split()

a="Python Java C C++"
a.split()
['Python', 'Java', 'C', 'C++']
b="I am Learning Python Course"
b.split()
['I', 'am', 'Learning', 'Python', 'Course']

#join()

a="python" "java" "c" "c++"
"".join(a)
'pythonjavacc++'
" ".join(a)
'p y t h o n j a v a c c + +'

a="python","java","c","c++"
" ".join(a)
'python java c c++'
"k".join(a)
'pythonkjavakckc++'

"#".join(a)
'python#java#c#c++'

#concatination

a="code"
b="gnan"
print(a+b)
codegnan

a="python"
b="course"
print(a+b)
pythoncourse

print(a+" "+b)
python course
print((a+" "+b).title())
Python Course

fname="Tabitha"
fname="tabitha"
lname="dorcas"
print(fname,lname)
tabitha dorcas
print(fname+" "+lname)
tabitha dorcas

print(fname.title()+" "+lname.title())
Tabitha Dorcas
prin
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    prin
NameError: name 'prin' is not defined. Did you mean: 'print'?

print((fname+" "+lname).title())
Tabitha Dorcas

print(fname.capitalize()+" "+lname.capitalize())
Tabitha Dorcas

#formatting

a=5
b=10
print(a+b)
15
print("The sum is",a+b)
The sum is 15

name="Tabitha Dorcas"
print("My name is",name)
My name is Tabitha Dorcas

age=20
print("I am "+ age +" old")
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    print("I am "+ age +" old")
TypeError: can only concatenate str (not "int") to str
print("My age is",age)
My age is 20

print("I am "+age+" years old")
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    print("I am "+age+" years old")
TypeError: can only concatenate str (not "int") to str

#format method

a"Motu"
SyntaxError: invalid syntax


#format method

a="Motu"
b="Patlu"
print("Hello {}{}".format())
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    print("Hello {}{}".format())
IndexError: Replacement index 0 out of range for positional args tuple
print("Hello {}{}".format(a,b))
Hello MotuPatlu

print("Hello {} {}".format(a,b))
Hello Motu Patlu

print("Hello {} Hello {}".format(a,b))
Hello Motu Hello Patlu


#fstring

fname="Tabitha"
lname="Dorcas"
print(f"Hello {a} {b}")
Hello Motu Patlu
print(f"Hello {fname} {lname}")
Hello Tabitha Dorcas
print(f"Hello {fname} Hello {lname}")
Hello Tabitha Hello Dorcas

#list[]

a=[7, 6.5, "Python", 5+7j, True, False]
print(a)
[7, 6.5, 'Python', (5+7j), True, False]
a=[7,6.5,"Python",5+7j,True,False]
print(a)
[7, 6.5, 'Python', (5+7j), True, False]

type(a)
<class 'list'>

b=7
type(b)
<class 'int'>

b=[7]
type(b)
<class 'list'>

a=["Python","DS","ML","AI"]
a.append("Java")
a
['Python', 'DS', 'ML', 'AI', 'Java']
a.append("c","c++")
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    a.append("c","c++")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["c","c++"])
a
['Python', 'DS', 'ML', 'AI', 'Java', ['c', 'c++']]

a=["Python","DS","ML","AI"]
a.extend(["Java","C"])
a
['Python', 'DS', 'ML', 'AI', 'Java', 'C']

a=["Python","DS","ML","AI"]
a.insert(1,"C")
a
['Python', 'C', 'DS', 'ML', 'AI']

a.insert(3,"c++")
a
['Python', 'C', 'DS', 'c++', 'ML', 'AI']

#index

a=["Python","DS","ML","AI"]
a.index("DS")
1

b=["apple","banana","grapes","mango"]
a.index("mango")
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    a.index("mango")
ValueError: list.index(x): x not in list

b=["apple","banana","grapes","mango"]
b.index("mango")
3

b.copy()
['apple', 'banana', 'grapes', 'mango']

b=a.copy()
b
['Python', 'DS', 'ML', 'AI']
a.clear()
a
[]
b=[]
b.append("C")
b
['C']

#pop

a=["Hi","Hello","How","Are","You"]
a.pop()
'You'
a
['Hi', 'Hello', 'How', 'Are']
a.pop(3)
'Are'
a
['Hi', 'Hello', 'How']
a.pop(2)
'How'
a
['Hi', 'Hello']

#sort

a=["Money","Books","Pen","Laptop"]
a.sort()
a
['Books', 'Laptop', 'Money', 'Pen']

b=[9,4,8,3,6,0,2,1]
b.sort()
b
[0, 1, 2, 3, 4, 6, 8, 9]

#reverse

a=["Money","Books","Pen","Laptop"]
a.reverse()
a
['Laptop', 'Pen', 'Books', 'Money']
>>> 
>>> b=[9,4,8,3,6,0,2,1]
>>> b.reverse()
>>> b
[1, 2, 0, 6, 3, 8, 4, 9]
>>> 
>>> #remove
>>> a=["Money","Books","Pen","Laptop"]
>>> a.pop("Pen")
Traceback (most recent call last):
  File "<pyshell#309>", line 1, in <module>
    a.pop("Pen")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.remove("Pen")
>>> a
['Money', 'Books', 'Laptop']
>>> 
>>> TypeError: 'str' object cannot be interpreted as an integer
SyntaxError: invalid syntax
>>> 
>>> a=["mango","kiwi","dragon"]
>>> len(a)
3
>>> b="mango"
>>> len(b)
5
>>> c=["mango"]
>>> len(c)
1
>>> a.count("dragon")
1
