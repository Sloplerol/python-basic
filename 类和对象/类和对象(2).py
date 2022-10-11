Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class A:
    x = 92
    def funA(self):
        print("i'm A")

        
class B(A):
    pass

b = B()
b.x
92
b.funA()
i'm A
class B(A):
    x = 22
    def funB(self):
        print("i'm B")

        
b = B()
b.x
22
b.funB()
i'm B
isinstance(b,B)
True
isinstance(b,A)
True
issubclass(A,B)
False
issubclass(B,A)
True
class B:
    x = 50
    def funB(self):
        print("i'm A")

        
class C(A,B):
    pass

c = C()
c.x
92
c.funB()
i'm A
class Apple:
    def peach(self):
        print("666")

        
class Banana:
    def peach(self):
        print("777")

        
class Lemon:
    def peach(self)
    
SyntaxError: expected ':'
class Lemon:
    def peach(self):
        print("888")

        
class Fruit:
    a = Apple()
    b = Banana()
    l = Lemon()
    def peach(self):
        self.a.peach()
        self.b.peach()
        self.c.peach()

        
f = Fruit()
f.peach()
666
777
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    f.peach()
  File "<pyshell#56>", line 8, in peach
    self.c.peach()
AttributeError: 'Fruit' object has no attribute 'c'
class Fruit:
    a = Apple()
    b = Banana()
    l = Lemon()
    def peach(self):
        self.a.peach()
        self.b.peach()
        self.l.peach()

        
f = Fruit()
f.peach()
666
777
888
