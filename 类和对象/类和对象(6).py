Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class C:
    def __init__(self,x)
    
SyntaxError: expected ':'
class C:
    def __init__(self,x):
        self.__x = x
    def set_x(self,x):
        self.__x = x
    def get_x(self):
        print(self.__x)

        
c = C(20)
c.get_x()
20
c.set_x(50)
c.get_x()
50
c.__x
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c.__x
AttributeError: 'C' object has no attribute '__x'
c.__dict__
{'_C__x': 50}
c._C__x
50
class D:
    def __fun(self):
        print("666")

        
d = D()
d.__fun()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d.__fun()
AttributeError: 'D' object has no attribute '__fun'. Did you mean: '_D__fun'?
d.__dict__
{}
d._D__fun
<bound method D.__fun of <__main__.D object at 0x103aae950>>
d._D__fun()
666
c.__y = 10
c.__dict__
{'_C__x': 50, '__y': 10}
c.__dict__['z'] = 21
c.__dict__
{'_C__x': 50, '__y': 10, 'z': 21}
class C;
SyntaxError: expected ':'
class C:
    __slots__ = ['x','y']
    def __init__(self,x)
    
SyntaxError: expected ':'
class C:
    __slots__ = ['x','y']
    def __init__(self,x):
        self.x = x

        
c = C(20)
c.x
20
c.y
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    c.y
AttributeError: 'C' object has no attribute 'y'
c.y = 10
c.y
10
c.__dict__
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c.__dict__
AttributeError: 'C' object has no attribute '__dict__'. Did you mean: '__dir__'?
c.__slots__
['x', 'y']
class D:
    __slots__['x']
    def __init__(self,x,y)
    
SyntaxError: expected ':'
class D:
    __slots__['x']
    def __init__(self,x,y):
        self.x = x
        self.y = y

        
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    class D:
  File "<pyshell#51>", line 2, in D
    __slots__['x']
NameError: name '__slots__' is not defined
class D:
    __slots__ = ['x']
    def __init__(self,x,y):
        self.x = x
        self.y = y

        
d = D(10,20)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    d = D(10,20)
  File "<pyshell#53>", line 5, in __init__
    self.y = y
AttributeError: 'D' object has no attribute 'y'
d = D(10)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    d = D(10)
TypeError: D.__init__() missing 1 required positional argument: 'y'
class E(C):
    pass

e = E(250)
e.x
250
e.y = 10
e.z = 20
e.__dict__
{'z': 20}
