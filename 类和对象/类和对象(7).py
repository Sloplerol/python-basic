Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class Cystyle(str):
    def __new__(cls,string):
        string = string.upper()
        return super().__new__(cls,string)

    
cs = Cystyle()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    cs = Cystyle()
TypeError: Cystyle.__new__() missing 1 required positional argument: 'string'
cs = Cystyle("Iloveyou")
cs
'ILOVEYOU'
cs.lower()
'iloveyou'
class Cystyle(str):
    def __new__(cls,string):
        string = string.upper()
        return __new__(cls,string)

    
cs = Cystyle("Iloveyou")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    cs = Cystyle("Iloveyou")
  File "<pyshell#10>", line 4, in __new__
    return __new__(cls,string)
NameError: name '__new__' is not defined. Did you mean: '__name__'?
class C:
    def __init__(self):
        print("我来了")
    def __del__(self):
        print("我走了")

        
c = C()
我来了
del c
我走了
c = C()
我来了
d = c
del c
del d
我走了
class A:
    def __init__(self,name):
        self.name = name
    def __del__(self):
        global x
        x = self

        
a = A("帅比")
a.name
'帅比'
del a
a
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'A'?
x
<__main__.A object at 0x103256500>
x.name
'帅比'
