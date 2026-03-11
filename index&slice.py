Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="Vijayawada"
a[2]
'j'
a[8]
'd'
a[0]
'V'
a[0]+a[1]+a[2]+a[3]+a[4]=a[5]
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'Vijaya'
a=I am in Class
SyntaxError: invalid syntax
a = I am in Class
SyntaxError: invalid syntax
a="I am in Class"
a[0]
'I'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[8]+a[9]+a[10]+a[11]+a[12]
'Class'
a[1]+a[4]+a[7]
'   '

a[-1]
's'

a="Simple is Better than Complex"
a[9]+a[10]+a[11]+a[12]+[13]+a[14]+a[15]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a[9]+a[10]+a[11]+a[12]+[13]+a[14]+a[15]
TypeError: can only concatenate str (not "list") to str
a[9]+a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
' Better'
a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'Complex'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'Simple'

a="I am Learning Python"
a[5]+a[6]+a[7]+a[8]+a[9]
'Learn'
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'Python'
a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]
'nohtyP'
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'Python'


a="Vijayawada is a royal city"
a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
a[-4]+a[-3]+a[-2]+a[-1]
'city'
a[-15]+a[-14]
'is'


a="Vizag is a city of Destiny"
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'Destiny'
a[-15]+a[-14]+a[-13]+a[-12]
'city'
a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'Vizag'

place="Tabitha Lives in Joppa"
place="Tabitha Lives in Joppa"

place[0:7]
'Tabitha'
place[:7]
'Tabitha'
place[7:]
' Lives in Joppa'

a="Codegnan"
a[0:4]
'Code'
a[4:7]
'gna'
a[4:8]
'gnan'
a[:4]
'Code'
a[4:]
'gnan'

' Lives in Joppa'
' Lives in Joppa'

place="Tabitha Lives in Joppa"
place[6:]
'a Lives in Joppa'
place[8:]
'Lives in Joppa'


a="Codegnan IT Solutions"
a[8:11]
' IT'
a[9:11]
'IT'
>>> a[4:8]
'gnan'
>>> a[12:20]
'Solution'
>>> 
>>> b=Python Full Stack Course
SyntaxError: invalid syntax
>>> b="Python Full Stack Course
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> b'Python Full Stack Course'
b'Python Full Stack Course'
>>> 
>>> b="Python Full Stack Course"
>>> b[7:11]
'Full'
>>> b[0:6]
'Python'
>>> b[18:24]
'Course'
>>> b[:24]
'Python Full Stack Course'
>>> 
>>> a="Work Hard Until you Succeed"
>>> a[-17:-12]
'Until'
>>> a[-12:-18]
''
>>> a[-22:-18]
'Hard'
>>> a[-27:-23]
'Work'
a[-7:-0]
''
a[-7:-1]
'Succee'
a[-7:0]
''
a[-7:1]
''

a[-7:]
'Succeed'

b="Time is very precious"
b[-13:-9]
'very'
b[-21:-17]
'Time'
b[-8:]
'precious'
