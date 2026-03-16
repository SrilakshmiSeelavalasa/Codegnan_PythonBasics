Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary

details={"name":"Tabitha","month":10}
print(details)
{'name': 'Tabitha', 'month': 10}

type(details)
<class 'dict'>

print(type(details))
<class 'dict'>

details["name"]
'Tabitha'

details["month"]
10

details.keys()
dict_keys(['name', 'month'])

details.values()
dict_values(['Tabitha', 10])

details.items()
dict_items([('name', 'Tabitha'), ('month', 10)])

details.update({"date":25})
details
{'name': 'Tabitha', 'month': 10, 'date': 25}

details.remove({"date":25})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    details.remove({"date":25})
AttributeError: 'dict' object has no attribute 'remove'

details.update({"date":25},{"time":9})
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    details.update({"date":25},{"time":9})
TypeError: update expected at most 1 argument, got 2

details.update({"date":25,"time":9})
details
{'name': 'Tabitha', 'month': 10, 'date': 25, 'time': 9}


#setdefault

things={"colour":"White","vehicle":"car"}
things.setdefault("fruit","kiwi")
'kiwi'
things
{'colour': 'White', 'vehicle': 'car', 'fruit': 'kiwi'}

things.setdefault(2026,"year")
'year'
things
{'colour': 'White', 'vehicle': 'car', 'fruit': 'kiwi', 2026: 'year'}

#pop

a={"user":"Sri","mobileno":9000,"mailid":"sri@gmail.com"}
a.pop()
SyntaxError: multiple statements found while compiling a single statement
a={"user":"Sri","mobileno":9000,"mailid":"sri@gmail.com"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0

a.pop("mobileno")
9000
a
{'user': 'Sri', 'mailid': 'sri@gmail.com'}

a.popitem()
('mailid', 'sri@gmail.com')
a
{'user': 'Sri'}


a={"time":2,"hour":3,"sec":5}
a.copy()
{'time': 2, 'hour': 3, 'sec': 5}
a
{'time': 2, 'hour': 3, 'sec': 5}

a.get()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.get()
TypeError: get expected at least 1 argument, got 0

a.get('time')
2


a={"name":"sri","city":"tanuku"}
len(a)
2

b={"name":"sri","city":"tanuku","name":"lakshmi"}
print(b)
{'name': 'lakshmi', 'city': 'tanuku'}
>>> 
>>> a.count("name")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
>>> 
>>> a.index("city")
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.index("city")
AttributeError: 'dict' object has no attribute 'index'
>>> 
>>> b
{'name': 'lakshmi', 'city': 'tanuku'}
>>> 
>>> c={"name":"sri","city":"tanuku","name1":"lakshmi"}
>>> print(c)
{'name': 'sri', 'city': 'tanuku', 'name1': 'lakshmi'}
>>> 
>>> a.keys()
dict_keys(['name', 'city'])
>>> 
>>> c.keys()
dict_keys(['name', 'city', 'name1'])
>>> 
>>> c.values()
dict_values(['sri', 'tanuku', 'lakshmi'])
>>> 
>>> c.items()
dict_items([('name', 'sri'), ('city', 'tanuku'), ('name1', 'lakshmi')])
