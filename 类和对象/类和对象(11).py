Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class C:
    def __getitem__(self,index):
        print(index)

        
c = C()
c[2]
2
c[2:8]
slice(2, 8, None)
b = "i love the world"
b[2:8]
'love t'
b[slice(2,8)]
'love t'
b[4:]
've the world'
b[slice(4,None)]
've the world'
b[::2]
'ilv h ol'
b[slice(None,None,2)]
'ilv h ol'
class C:
    def __init__(self,data):
        self.data = data
    def __getitem__(self,index):
        return self.data[index]
    def __setitem__(self,index,value):
        self.__dict__[index] = value

        
c = C("Jackrolin")
c.data
'Jackrolin'
c[2]
'c'
c[2]=1
c
<__main__.C object at 0x103b09510>
c.date
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    c.date
AttributeError: 'C' object has no attribute 'date'
c.data
'Jackrolin'
c[2] = 'b'
c.data
'Jackrolin'
c[2]
'c'
c =C([1,2,3,4,5])
c[1]
2
c[2] = 2
c[2]
3
class C:
    def __init__(self,data):
        self.data = data
    def __getitem__(self,index):
        return self.data[index]
    def __setitem__(self,index,value):
        self.data[index] = value

        
c = C([1,2,3,4,5])
c[2] = 2
c[2]
2
class C:
    def __init__(self,data):
        self.data = data
    def __getitem__(self,index):
        return self.data[index]*2

    
c = C([1,2,3,4,5])
for i in c:
    print(i,end=' ')

    
2 4 6 8 10 
x = [1,2,3,4,5]
for i in x:
    print(x,end=' ')

    
[1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [1, 2, 3, 4, 5] 
x = 12345
for i in x:
    print(x,end=' ')

    
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    for i in x:
TypeError: 'int' object is not iterable
x = [1,2,3,4,5]
for i in x:
    print(i,end = ' ')

    
1 2 3 4 5 
_ = iter(x)
while True:
    try:
        i = _.__next__()
    except StopIteration:
        break
    print(i)

    
1
2
3
4
5
class Double:
    def __init__(start,end):
        self.start = start-1
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start = self.end:
            
SyntaxError: cannot assign to attribute here. Maybe you meant '==' instead of '='?
class Double:
    def __init__(self,start,end):
        self.start = start-1
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start == self.end:
            raise StopIteration
        self.start+=1
        return self.start*2

    
d = D(1,8)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    d = D(1,8)
NameError: name 'D' is not defined
d = Double(1,8)
for i in d:
    print(i.end=' ')
    
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
for i in d:
    print(i,end=' ')

    
2 4 6 8 10 12 14 16 
