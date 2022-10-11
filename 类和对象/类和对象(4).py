Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return x+y
    def mul(self):
        return x*y

    
c = C(2,2)
c.add()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    c.add()
  File "<pyshell#8>", line 6, in add
    return x+y
NameError: name 'x' is not defined
class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x+self.y
    def mul(self):
        return self.x*self.y

    
c = C(1,2)
c.add()
3
c.mul()
2
c.__dict__
{'x': 1, 'y': 2}
class B(C):
    def __init__(self,x,y,z):
        C.__init__(self,x,y)
        self.z = z
    def add(self):
        return C.add(self)+self.z
    def mul(self):
        return C.mul(self)*self.z

    
b = B()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b = B()
TypeError: B.__init__() missing 3 required positional arguments: 'x', 'y', and 'z'
b = B(2,4,5)
b.add()
11
b.mul()
40
class A:
    def __init__(self):
        print("i am a")

        
class B(A):
    def __init__(self):
        A.__init__(self)
        print("i am b")

        
class C(A):
    def __init__(self):
        A.__init__(self)
        print("i am c")

        
class D(B,C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print("i am d")

        
d = D()
i am a
i am b
i am a
i am c
i am d
class B(A):
    def __init__(self):
        super().__init__(self)
        print("i am b")

        
class C(A):
    def __init__(self):
        super().__init__(self)
        print("i am c")

        
class D(B,C):
    def __init__(self):
        super().__init__(self)
        print("i am d")

        
d = D()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    d = D()
  File "<pyshell#54>", line 3, in __init__
    super().__init__(self)
TypeError: B.__init__() takes 1 positional argument but 2 were given
class B(A):
    def __init__(self):
        super().__init__()
        print("i am b")

        
class C(A):
    def __init__(self):
        super().__init__()
        print("i am c")

        
class D(B,C):
    def __init__(self):
        super().__init__()
        print("i am d")

        
d = D()
i am a
i am c
i am b
i am d
D.mro()
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
C.mro()
[<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
