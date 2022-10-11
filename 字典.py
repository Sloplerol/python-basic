Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = {"spring","summer"}
type(x)
<class 'set'>
x = {"spring:春","summer:夏天"}
type(x)
<class 'set'>
x = {"spring":"春","summer":"夏"}
type(x)
<class 'dict'>
x["autumn"] = "秋"
x
{'spring': '春', 'summer': '夏', 'autumn': '秋'}
x = {'spring': '春', 'summer': '夏', 'autumn': '秋'}
x
{'spring': '春', 'summer': '夏', 'autumn': '秋'}
x = dict(spring = "春",summmer = "夏",autumn = "秋")
x
{'spring': '春', 'summmer': '夏', 'autumn': '秋'}
x = dict(("spring","春"),("summer","夏"),("autumn","秋"))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x = dict(("spring","春"),("summer","夏"),("autumn","秋"))
TypeError: dict expected at most 1 argument, got 3
x = dict([("spring","春"),("summer","夏"),("autumn","秋")])
x
{'spring': '春', 'summer': '夏', 'autumn': '秋'}
x = dict({'spring': '春', 'summer': '夏', 'autumn': '秋'})
x
{'spring': '春', 'summer': '夏', 'autumn': '秋'}
x = dict({'spring': '春', 'summer': '夏'},autumn = "秋")
x
{'spring': '春', 'summer': '夏', 'autumn': '秋'}
x = dict(zip(["spring","summer","autumn"],["春","夏","秋"]))
x
{'spring': '春', 'summer': '夏', 'autumn': '秋'}
a = dict.fromkeys("Miracle",250)
a
{'M': 250, 'i': 250, 'r': 250, 'a': 250, 'c': 250, 'l': 250, 'e': 250}
a['i'] = 55
a
{'M': 250, 'i': 55, 'r': 250, 'a': 250, 'c': 250, 'l': 250, 'e': 250}
a['h'] = 22
a
{'M': 250, 'i': 55, 'r': 250, 'a': 250, 'c': 250, 'l': 250, 'e': 250, 'h': 22}
a.pop('M')
250
a
{'i': 55, 'r': 250, 'a': 250, 'c': 250, 'l': 250, 'e': 250, 'h': 22}
a.pop("hey")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.pop("hey")
KeyError: 'hey'
a.pop("hey","没有这个数")
'没有这个数'
a.popitem()
('h', 22)
a
{'i': 55, 'r': 250, 'a': 250, 'c': 250, 'l': 250, 'e': 250}
del a['r']
a
{'i': 55, 'a': 250, 'c': 250, 'l': 250, 'e': 250}
del a
a
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a
NameError: name 'a' is not defined
a = dict.fromkeys("Miracle",250)
a
{'M': 250, 'i': 250, 'r': 250, 'a': 250, 'c': 250, 'l': 250, 'e': 250}
a.clear()
a
{}
C = dict.fromkeys ("Miracle")
C
{'M': None, 'i': None, 'r': None, 'a': None, 'c': None, 'l': None, 'e': None}
C['M']=10
C
{'M': 10, 'i': None, 'r': None, 'a': None, 'c': None, 'l': None, 'e': None}
C.update({'i'=20})
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
C.update({'i':20})
C
{'M': 10, 'i': 20, 'r': None, 'a': None, 'c': None, 'l': None, 'e': None}
C.update({'i':'30'})
C
{'M': 10, 'i': '30', 'r': None, 'a': None, 'c': None, 'l': None, 'e': None}
C.update(r=30)
C
{'M': 10, 'i': '30', 'r': 30, 'a': None, 'c': None, 'l': None, 'e': None}
C['r']
30
C['R']
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    C['R']
KeyError: 'R'
C.get('R',"此处无R")
'此处无R'
C.setdefault("r","code")
30
C.setdefault("R","code")
'code'
C
{'M': 10, 'i': '30', 'r': 30, 'a': None, 'c': None, 'l': None, 'e': None, 'R': 'code'}
keys = C.keys()
values = C.values()
items = C.items()
items
dict_items([('M', 10), ('i', '30'), ('r', 30), ('a', None), ('c', None), ('l', None), ('e', None), ('R', 'code')])
keys
dict_keys(['M', 'i', 'r', 'a', 'c', 'l', 'e', 'R'])
values
dict_values([10, '30', 30, None, None, None, None, 'code'])
C.pop('M')
10
items
dict_items([('i', '30'), ('r', 30), ('a', None), ('c', None), ('l', None), ('e', None), ('R', 'code')])
e = C.copy()
e
{'i': '30', 'r': 30, 'a': None, 'c': None, 'l': None, 'e': None, 'R': 'code'}
'c' in e
True
'C' in e
False
'C' not in e
True
list(C)
['i', 'r', 'a', 'c', 'l', 'e', 'R']
list(C.keys())
['i', 'r', 'a', 'c', 'l', 'e', 'R']
list(C.values())
['30', 30, None, None, None, None, 'code']
e = iter(d)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    e = iter(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
e = iter(C)
next(e)
'i'
next(e)
'r'
next(e)
'a'
next(e)
'c'
next(e)
'l'
next(e)
'e'
next(e)
'R'
next(e)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    next(e)
StopIteration
a = {"lbw":{"数学":10,"语文":20},"ppd":{"数学":20,"语文":49}}
a["lbw"]["语文"]
20
a = {"lbw":[10,20],"ppd":[20,30]}
a["ppd"][1]
30
d = {'M':22,'K':2818,'p':392}
type(d)
<class 'dict'>
{k:v for v,k in d.items()}
{22: 'M', 2818: 'K', 392: 'p'}
{k:v for v,k in d.items() if k>100}
{2818: 'K', 392: 'p'}
d = {x:y for x in [1,2,3] for y in (4,5,6)}
d
{1: 6, 2: 6, 3: 6}
