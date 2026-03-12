Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple()
a=(2,4.5,"Python",7+9j,True,False)
print(a)
(2, 4.5, 'Python', (7+9j), True, False)

type(a)
<class 'tuple'>

len(a)
6

a.index(True)
4
a.index(False)
5

a.count(4.5)
1

#sets{}

a={2,5.7,"Sri",6+7j,True,False}
print(a)
{False, True, 2, 'Sri', 5.7, (6+7j)}

b={5,7,0,4,3,1,2,6,7}
print(b)
{0, 1, 2, 3, 4, 5, 6, 7}

type(a)
<class 'set'>


type(b)
<class 'set'>

a={1,2,3,4,5,6}
b={4,5,6}
a.add(7)
a
{1, 2, 3, 4, 5, 6, 7}
b.add(7)
b
{4, 5, 6, 7}

a.issuper(b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.issuper(b)
AttributeError: 'set' object has no attribute 'issuper'. Did you mean: 'issubset'?

a.issupset(b)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.issupset(b)
AttributeError: 'set' object has no attribute 'issupset'. Did you mean: 'issubset'?
a.issuperset(b)
True
b.issubset(a)
True

a={3,4,5,6,7,8}
b={1,2,3,4,5}
a.issuperset(b)
False
b.superset(a)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    b.superset(a)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
b.issuperset(a)
False
b.issubset(a)
False

#union()

a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}

a={12,13,14,15,16,17}
b={15,16,17,18,19,20}
a.union(b)
{12, 13, 14, 15, 16, 17, 18, 19, 20}
b.union(a)
{12, 13, 14, 15, 16, 17, 18, 19, 20}


#intersection()
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
a.intersection(b)
{4, 5, 6}
b.intersection(a)
{4, 5, 6}

#difference()
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
a.difference(b)
{1, 2, 3}
b.difference(a)
{8, 9, 7}

a={12,13,14,15,16,17}
b={16,17,18,19,20}
a.difference(b)
{12, 13, 14, 15}
b.difference(a)
{18, 19, 20}

#update()
a={8,9,10,11,12,13,14,15}
b={1,2,3,4,5,6,7,8}
a
{8, 9, 10, 11, 12, 13, 14, 15}
b
{1, 2, 3, 4, 5, 6, 7, 8}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
b
{1, 2, 3, 4, 5, 6, 7, 8}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

#intersection_update()

a={4,5,6,7,8,9}
b={7,8,9,10,11,12}
a
{4, 5, 6, 7, 8, 9}
a.intersection_update(b)
a
{8, 9, 7}
a
{8, 9, 7}
b
{7, 8, 9, 10, 11, 12}
b.intersection_update(a)
b
{8, 9, 7}
b
{8, 9, 7}

#difference_update()

a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
a
{1, 2, 3, 4, 5, 6}
a.difference_update(b)
a
{1, 2, 3}
a
{1, 2, 3}
b
{4, 5, 6, 7, 8, 9}
b.difference_update(a)
b
{4, 5, 6, 7, 8, 9}

b
{4, 5, 6, 7, 8, 9}

a={2,3,4,5,6,7}
b={1,2,3,4,5,6,7,8,9}
a
{2, 3, 4, 5, 6, 7}
a.difference_update(a)
a
set()
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#symmetric difference()
a={3,4,5,6,7,8}
b={1,2,3,4,5,6,7}
a.symmetric_difference(b)
{1, 2, 8}
a
{3, 4, 5, 6, 7, 8}
b.symmetric_differnce(a)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    b.symmetric_differnce(a)
AttributeError: 'set' object has no attribute 'symmetric_differnce'. Did you mean: 'symmetric_difference'?
b.symmetric_difference(a)
{1, 2, 8}

b
{1, 2, 3, 4, 5, 6, 7}

#symmetric difference update()
a={10,20,30,40,50,60}
b={30,40,50,60,70,80,90}
a.symmetric_differnce_update(b)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    a.symmetric_differnce_update(b)
AttributeError: 'set' object has no attribute 'symmetric_differnce_update'. Did you mean: 'symmetric_difference_update'?


#symmetric_difference_update()
a={10,20,30,40,50,60}
b={30,40,50,60,70,80,90}
a.symmetric_difference_update(b)
a
{70, 10, 80, 20, 90}
a
{70, 10, 80, 20, 90}
b
{80, 50, 70, 40, 90, 60, 30}
b.symmetric_difference_update(a)
b
{40, 10, 50, 20, 60, 30}


#pop and remove

a={1,2,3,4,5,6,7}
b={3,4,5,6,7,8,9}
a.pop()
1
a.pop(4)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    a.pop(4)
TypeError: set.pop() takes no arguments (1 given)
a
{2, 3, 4, 5, 6, 7}
a.remove(4)
a
{2, 3, 5, 6, 7}
a.remove(2,6)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    a.remove(2,6)
TypeError: set.remove() takes exactly one argument (2 given)

a
{2, 3, 5, 6, 7}

#copy and clear
a={1,2,3,4,5,6}
a.copy()
{1, 2, 3, 4, 5, 6}
a.clear()
a
set()
b=set()
b={30}
>>> b
{30}
>>> 
>>> a={1,2,3,4,5,6}
>>> a.discard(3)
>>> a
{1, 2, 4, 5, 6}
>>> 
>>> #disjoint()
>>> a={6,7}
>>> b={7,8}
>>> a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> a.isdisjoint(b)
False
>>> 
>>> a={1,2,3}
>>> b={4,5,6}
>>> a.isdisjoint(b)
True
>>> b.isdisjoiont(a)
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    b.isdisjoiont(a)
AttributeError: 'set' object has no attribute 'isdisjoiont'. Did you mean: 'isdisjoint'?
>>> b.isdisjoint(a)
True
>>> 
