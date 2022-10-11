Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class opo:
    def __init__(self,name):
        self.name = name
    def area:
        
SyntaxError: invalid syntax
class opo:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass

    
class Square:
    def __init__(self,length):
        super().__init__("正方形")
        self.length = length
    def area(self)
    
SyntaxError: expected ':'
class Square:
    def __init__(self,length):
        super().__init__("正方形")
        self.length = length
    def area(self):
        return self.length*self.length

    
class Circle:
    def __init__(self,radius):
        super().__init__("圆")
        self.radius = radius
    def area(self):
        return self.raius*self.radius*3.14

    
s = Square()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s = Square()
TypeError: Square.__init__() missing 1 required positional argument: 'length'
s = Square(length)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s = Square(length)
NameError: name 'length' is not defined
s = Square(5)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s = Square(5)
  File "<pyshell#14>", line 3, in __init__
    super().__init__("正方形")
TypeError: object.__init__() takes exactly one argument (the instance to initialize)
class Square(opo):
    def __init__(self,length):
        super().__init__("正方形")
        self.length = length
    def area(self):
        return self.length*self.length

    
s = Square(5)
s.name
'正方形'
s.area()
25
class Circle(opo):
    def __init__(self,radius):
        super().__init__("圆")
        self.radius = radius
    def area(self):
        return self.raius*self.radius*3.14

    
c = Circle(4)
c.name
'圆'
c.area
<bound method Circle.area of <__main__.Circle object at 0x1050c55a0>>
c.area()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    c.area()
  File "<pyshell#31>", line 6, in area
    return self.raius*self.radius*3.14
AttributeError: 'Circle' object has no attribute 'raius'. Did you mean: 'radius'?
c = Circle(4)
c.area()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    c.area()
  File "<pyshell#31>", line 6, in area
    return self.raius*self.radius*3.14
AttributeError: 'Circle' object has no attribute 'raius'. Did you mean: 'radius'?
class Circle(opo):
    def __init__(self,radius):
        super().__init__("圆")
        self.radius = radius
    def area(self):
        return self.radius*self.radius*3.14

    
c = Circle(3)
c.area()
28.26
class Apple:
    def __init__(self,name,say):
        self.name = name
        self.age = age
    def introduce(self):
        print("我叫{name},今年{age}岁")
    def say(self):
        print("贼香")

        
class Banana:
    def __init__(self,name,say):
        self.name = name
        self.age = age
    def introduce(self):
        print("我叫{name},今年{age}岁")
    def say(self):
        print("贼黄")

        
class Peach:
    def __init__(self,name,say):
        self.name = name
        self.age = age
    def introduce(self):
        print("我叫{name},今年{age}岁")
    def say(self):
        print("贼润")

        
a = Apple"(苹果",10)
SyntaxError: unmatched ')'
a = Apple("苹果",10)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a = Apple("苹果",10)
  File "<pyshell#50>", line 4, in __init__
    self.age = age
NameError: name 'age' is not defined
class Apple:
    def __init__(self,name,say):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫{name},今年{age}岁")
    def say(self):
        print("贼香")

        
class Banana:
    def __init__(self,name,say):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫{name},今年{age}岁")
    def say(self):
        print("贼黄")

        
class Peach:
    def __init__(self,name,say):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫{name},今年{age}岁")
    def say(self):
        print("贼润")

        
a = Apple("苹果",5)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a = Apple("苹果",5)
  File "<pyshell#58>", line 4, in __init__
    self.age = age
NameError: name 'age' is not defined
class Apple:
    def __init__(self,name,say):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫{self.name},今年{self.age}岁")
    def say(self):
        print("贼香")

        
class Banana:
    def __init__(self,name,say):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫{self.name},今年{self.age}岁")
    def say(self):
        print("贼黄")

        
class Peach:
    def __init__(self,name,say):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫{self.name},今年{self.age}岁")
    def say(self):
        print("贼润")

        
a = Apple("苹果",5)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a = Apple("苹果",5)
  File "<pyshell#65>", line 4, in __init__
    self.age = age
NameError: name 'age' is not defined
class Apple:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫{self.name},今年{self.age}岁")
    def say(self):
        print("贼香")

        
class Banana:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫{self.name},今年{self.age}岁")
    def say(self):
        print("贼黄")

        
class Peach:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫{self.name},今年{self.age}岁")
    def say(self):
        print("贼润")

        
a = Apple("苹果",3)
b = Banana("香蕉",5)
p = Peach("桃",7)
def fruit(x):
    x.inrtoduce()
    x.say()

    
fruit(a)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    fruit(a)
  File "<pyshell#83>", line 2, in fruit
    x.inrtoduce()
AttributeError: 'Apple' object has no attribute 'inrtoduce'. Did you mean: 'introduce'?
def fruit(x):
    x.introduce()
    x.say()

    
fruit(a)
我叫苹果,今年3岁
贼香
fruit(b)
我叫香蕉,今年5岁
贼黄
fruit(p)
我叫桃,今年7岁
贼润
