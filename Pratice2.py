Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Operators
#Arithmetic Operators
a=78
b=52
print(a+b)
130
a+b
130
a-b
26
b-a
-26
a*b
4056
a//b
1
a/b
1.5
a**b
244860842756831203896798793038363593764863637715027581243662187665028113084218676375430402110652416
a%b
26
a=8
b=4
a//b
2
a=4
b=2
a/b
2.0

#Assignment Operators
a=36
b=24
a+=b
a
60
a-=b
a
36
a*=b
a
864
a//=b
a
36
a/=b
a
1.5
a**=b
a
16834.112196028233
a%=b
a
10.112196028232574
b+=a
b
34.112196028232574
a=12
b=24
b+=a
b
36
b-=a
b
24
b*=a
b
288
b//=a

b
b//=a
b
2
b/=a
b
0.16666666666666666
a=12
b=24
b**=a
b
36520347436056576
a=12
b=24
b%=a
b
0

#Comparision Operators
a=14
b=16
a<b
True
a>b
False
a==b
False
a!=b
True
a<=b
True
a>=b
False
b>a
True
b<a
False
b==a
False
b!=a
True
b>=a
True
b<=a
False

#Logical Operators
a=4
b=5
a<b and b>a
True
a>b and b>a
False
a<b and b<a
False
a!=b and b!=a
True
a!=b and b==a
False
a==b and b==a
False

a<b or b>a
True
a<b or b<a
True
a>b or b<a
False
a==b or b!=a
True
a<=b or b==a
True
a!=b or b<a
True

not True
False
not False
True

#Identify Operators
a=46
if type(a) is int:
    print('Yes')

    
Yes
if type(a) is float:
    print('Yes')

    
a=6.4
if type(a) is int:
    print('It is int')

    
if type(a) is float:
    print('Yes its float)
          
SyntaxError: unterminated string literal (detected at line 2)
if type(a) is float:
          print('Yes its float')

          
Yes its float

#Membership Operators
          
a=20,21,22,23,24,25,26,27,28,29,30
          
if 24 in a:
          print('Present')

          
Present
if 32 in a:
          print('Present')

          
if 32 not in a:
          print('Not Present')

          
Not Present
if 24 not in a:
          print('Not Present')

          
if 42 not in a:
          print('Not Present')

          
Not Present

#Bitwise Operators
          
a=14
          
b=16
          
a&b
          
0
bin(a)
          
'0b1110'
bin(b)
          
'0b10000'
a=3
          
b=5
          
a&b
          
1
bin(a)
          
'0b11'
bin(b)
          
'0b101'
a=4
          
b=7
          
a&b
          
4
a=4
          
b=7
          
a|b
          
7
a=5
          
b=2
          
a|b
          
7
a=6
          
b=3
          
>>> a|b
...           
7
>>> a=7
...           
>>> b=2
...           
>>> a|b
...           
7
>>> a=8
...           
>>> b=6
...           
>>> a|b
...           
14
>>> a=14
...           
>>> ~a
...           
-15
>>> 
>>> a=4
...           
>>> b=6
...           
>>> a^b
...           
2
>>> a=5
...           
>>> b=3
...           
>>> a^b
...           
6
