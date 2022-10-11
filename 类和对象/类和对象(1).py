Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class C:
    def hill():
        print("山丘")

        
c = C()
c()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c()
TypeError: 'C' object is not callable
c.hill()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    c.hill()
TypeError: C.hill() takes 0 positional arguments but 1 was given
c.hill
<bound method C.hill of <__main__.C object at 0x103d818d0>>
class C:
    def hill(self):
        print("山丘")


c = C()
c.hill()
山丘
class C:
    def hill(self):
        print(self)

        
c = C()
c.hill()
<__main__.C object at 0x103d82380>
c
<__main__.C object at 0x103d82380>
