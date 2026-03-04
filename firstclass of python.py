Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Variables
print(7+8)
15
a=3
print(a)
3
b=10
print(b)
10
#=10
a2=10
print(a2)
10
b=7
c=9
print(b+c)
16
x=10
print(X)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
Z=100
print(Z)
100
a012345=200
print(a012345)
200
10X=400
SyntaxError: invalid decimal literal
@=10
SyntaxError: invalid syntax
name="sri"
print(name)
sri
city="Viy"
print(city)
Viy
Country="india"
print(Country)
india
a=6,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=6;b=9
print(a+b)
15
a,b=5,6
print(a+b)
11
 a=20
 
SyntaxError: unexpected indent
_=30
print(_)
30
_a=30
print(_a)
30
mail=sri@codegnan.com
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    mail=sri@codegnan.com
NameError: name 'sri' is not defined
mail="sri@codegnan.com"
print(mail)
sri@codegnan.com
data="sri@123#123"
print(data)
sri@123#123
first name="sri"
SyntaxError: invalid syntax
first_name="sri"
print(first_name)
sri
firstname="sri"
print(firstname)
sri
fname="sri"
lname="lakshmi"
print(fname+lname)
srilakshmi
print(fname+" "+lname)
sri lakshmi
print(fname,lname)
sri lakshmi


#del

a=8
print(a)
8
del a
print(a)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a2'?
Name="sri"
print(Name)
sri
NAME="sri"
print(NAME)
sri
name="sri"
print(Name)
sri
if=80
SyntaxError: invalid syntax

 

#datatypes

#datatype conversions

int(4)
4
int(7.8)
7
int("sri")
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    int("sri")
ValueError: invalid literal for int() with base 10: 'sri'
int(5+5j)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    int(5+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

 
#float conversion

float(4)
4.0
float(5.6)
5.6
FLOAT(5.6)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    FLOAT(5.6)
NameError: name 'FLOAT' is not defined
float("sri")
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    float("sri")
ValueError: could not convert string to float: 'sri'
float(5+6j)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    float(5+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0


#strtype conversion

str(4)
'4'
str(5.6)
'5.6'
str("Sri")
'Sri'
str("5+6j)
    
SyntaxError: unterminated string literal (detected at line 1)
str(5+6j)
    
'(5+6j)'
str(True)
    
'True'
str(False)
    
'False'

#complextype conversion
    
complex(4)
    
(4+0j)
complex(5.6)
    
(5.6+0j)
complex("Sri")
    
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    complex("Sri")
ValueError: complex() arg is a malformed string
complex(5+6j)
    
(5+6j)
complex(True)
    
(1+0j)
complex(False)
    
0j


#booltype coversion
    

bool(4)
    
True
bool(5.6)
    
True
bool("sri")
    
True
bool(5+6j)
    
True
>>> bool(True)
...     
True
>>> bool(False)
...     
False
>>> 
>>> 
>>> #datatypes
...     
>>> a=4
...     
>>> type(a)
...     
<class 'int'>
>>> b=5.6
...     
>>> type(b)
...     
<class 'float'>
>>> c="Sri"
...     
>>> type(c)
...     
<class 'str'>
>>> d=5+6j
...     
>>> type(d)
...     
<class 'complex'>
>>> e='True'
...     
>>> type(e)
...     
<class 'str'>
>>> e=True
...     
>>> type(e)
...     
<class 'bool'>
>>> f=False
...     
>>> type(f)
...     
<class 'bool'>
