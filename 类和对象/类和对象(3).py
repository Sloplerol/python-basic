Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class C:
    def get_self(self):
        print(self)

        
c = C()
c.get_self()
<__main__.C object at 0x1076593c0>
c
<__main__.C object at 0x1076593c0>
C.get_self(c)
<__main__.C object at 0x1076593c0>
c.x
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c.x
AttributeError: 'C' object has no attribute 'x'
c.x = 20
c.x
20
c.__dict__
{'x': 20}
c.y = 59
c.__dict__
{'x': 20, 'y': 59}
class A:
    def set_x(self,v):
        self.x = v

        
set_x(20)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set_x(20)
NameError: name 'set_x' is not defined
a = A()
a.set_x(250)
a
<__main__.A object at 0x10765a470>
a__dict__
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a__dict__
NameError: name 'a__dict__' is not defined. Did you mean: '__doc__'?
a.__dict__
{'x': 250}
a.x
250
class C:
    x = 100
    def get_x(self,v):
        x = v

        
c = C()
c.get_x(100)
c.x
100
c.__dict__
{}
C.x
100
C.__dict__
mappingproxy({'__module__': '__main__', 'x': 100, 'get_x': <function C.get_x at 0x107693010>, '__dict__': <attribute '__dict__' of 'C' objects>, '__weakref__': <attribute '__weakref__' of 'C' objects>, '__doc__': None})
C.x = 20
c.x
20
c.__dict__
{}
class C:
    pass

C.x = 250
C.y = "666"
C.z = [1,2,3]
print(C.x)
250
print(C.y)
666
d = {}
d['x'] = 250
d['y'] = 22
d['z'] = 66
d
{'x': 250, 'y': 22, 'z': 66}
print(['x'])
['x']
print(d['x'])
250
class A:
    pass

a = A()
a.x = 20
a.y = "243"
a.z = [1,2,3]
a.__dict__
{'x': 20, 'y': '243', 'z': [1, 2, 3]}
print(a.x)
20
a = {}
a['x'] = 20
a['y'] = '222'
a['z'] = [1,2,3]
print(a['x'])
20
