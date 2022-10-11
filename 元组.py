Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
rhy = (1,2,3,4,5)
rhy
(1, 2, 3, 4, 5)
rhy = 1,2,3,4,5
rhy
(1, 2, 3, 4, 5)
rhy[0]
1
rhy[0]=2
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    rhy[0]=2
TypeError: 'tuple' object does not support item assignment
rhy[:3]
(1, 2, 3)
rhy[3:]
(4, 5)
rhy[:]
(1, 2, 3, 4, 5)
rhy[::2]
(1, 3, 5)
rhy[2::]
(3, 4, 5)
rhy[::-1]
(5, 4, 3, 2, 1)
num = (1,2,3,4,2,5,3)
num.count(3)
2
num.index(5)
5
s = (1,2,3)
t = (4,5,6)
s+t
(1, 2, 3, 4, 5, 6)
s*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
for i in s:
    print(i)

    
1
2
3
s,t
((1, 2, 3), (4, 5, 6))
h = s,t
for i in h:
    for w in i:
        print(w)

        
1
2
3
4
5
6
w = (w for i in h for w in i)
w
<generator object <genexpr> at 0x1056329d0>
a = [w for i in h for w in i]
a
[1, 2, 3, 4, 5, 6]
c = (1,2,3,4,5)
[i*2 for i in c]
[2, 4, 6, 8, 10]
(i*2 for i in c)
<generator object <genexpr> at 0x105632960>
x = (520)
type(x)
<class 'int'>
x = (520,)
type(x)
<class 'tuple'>
s = (5,6,7)
x,y,z = s
x
5
y
6
z

z
7
(x,y,z)=s
x
5
s = "Matrol"
x,y,z = s
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x,y,z = s
ValueError: too many values to unpack (expected 3)
x,y,z=s
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    x,y,z=s
ValueError: too many values to unpack (expected 3)
a,b,c,d,e,f = s
a
'M'
b
'a'
c
't'
d
'r'
e
'o'
f
'l'
s = [1,2,3]
x,y,z = s
x
1
y
2
z
3
s = (1,2,3,4,5)
x,y,*z=s
x
1
y
2
z
[3, 4, 5]
_ = (10,20)
x,y = _
x
10
y
20
s = [1,2,3]
d = [4,5,6]
s,d
([1, 2, 3], [4, 5, 6])
s,d[0][0]=2
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s,d[0][0]=2
TypeError: cannot unpack non-iterable int object
t = s,d
t[0][0] = 2
s,d
([2, 2, 3], [4, 5, 6])
