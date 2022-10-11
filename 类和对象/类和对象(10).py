Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class C
SyntaxError: expected ':'
class C:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

        
c = C("Dk",20)
hasattr(c,name)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    hasattr(c,name)
NameError: name 'name' is not defined
hasattr(c,"name")
True
getattr(c,"name")
'Dk'
getattr(c,age)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    getattr(c,age)
NameError: name 'age' is not defined
getattr(c,"age")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    getattr(c,"age")
AttributeError: 'C' object has no attribute 'age'
getattr(c,"_C__age")
20
setattr(c,"_C__age",10)
getattr(c,"_C__age")
10
delattr(c,"name")
getattr(c,"name")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    getattr(c,"name")
AttributeError: 'C' object has no attribute 'name'
class C:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __getattribute__(self,attrname)
    
SyntaxError: expected ':'
class C:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __getattribute__(self,attrname):
        print("666")
        return super().__getattribute__(attrname)

    
c = C("天",16)
666
666
KeyboardInterrupt
getattr(c,"name")
666
'天'
getattr(c,"age")
666
16
c.name
666
'天'
c.fill
666
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c.fill
  File "<pyshell#25>", line 7, in __getattribute__
    return super().__getattribute__(attrname)
666
666
AttributeError: 'C' object has no attribute 'fill'
class C:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __getattribute__(self,attrname):
        print("666")
        return super().__getattribute__(attrname)
    def __getattr__(self):
        if attrname == "fill"
        
SyntaxError: expected ':'
class C:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __getattribute__(self,attrname):
        print("666")
        return super().__getattribute__(attrname)
    def __getattr__(self):
        if attrname == "fill":
            print("i love you")
        else:
            raise AttributeError(attrname)

        
c = C("天",16)
666
666
KeyboardInterrupt
666
666
KeyboardInterrupt
c.fill
666
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    c.fill
TypeError: C.__getattr__() takes 1 positional argument but 2 were given
class C:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __getattribute__(self,attrname):
        print("666")
        return super().__getattribute__(attrname)
    def __getattr__(self,attrname):
        if attrname == "fill":
            print("i love you")
        else:
            raise AttributeError(attrname)

        
c = C("天",16)
c.fill
666
i love you
c.hill
666
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    c.hill
  File "<pyshell#41>", line 12, in __getattr__
    raise AttributeError(attrname)
666
666
AttributeError: hill
class C:
    def __setattr__(self,name,value):
        self.name = value

        
c = C()
c.name = "god"
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    c.name = "god"
  File "<pyshell#48>", line 3, in __setattr__
    self.name = value
  File "<pyshell#48>", line 3, in __setattr__
    self.name = value
  File "<pyshell#48>", line 3, in __setattr__
    self.name = value
  [Previous line repeated 1022 more times]
RecursionError: maximum recursion depth exceeded
class C:
    def __setattr__(self,name,value):
        self.__dict__[name] = value

        
c = C()
c.name = "god"
c.name
'god'
class C:
    def __setattr__(self,name,value):
        self.__dict__[name] = value
    def __delattr__(self,name):
        del self.__dict__[name]

        
c = C()
c.name = "god"
c.__dict__
{'name': 'god'}
del c.name
c.__dict__
{}
