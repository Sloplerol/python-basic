Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def square():
    return x*x

square(3)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    square(3)
TypeError: square() takes 0 positional arguments but 1 was given
def square(x):
    return x*x

square(3)
9
square = lambda x : x*x
square(3)
9
square = [lambda(x:x*x),2,3]
SyntaxError: invalid syntax
square = [lambda x:x*x,2,3]
square[0][1]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    square[0][1]
TypeError: 'function' object is not subscriptable
square[0](1)
1
square[0](y[1])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    square[0](y[1])
NameError: name 'y' is not defined
square[0](square[1])
4
mapped = map(lambda x:ord(x)+10 , "magic")
list(mapped)
[119, 107, 113, 115, 109]
def mapped(x):
    return ord(x)+10

list(mapped("magic"))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list(mapped("magic"))
  File "<pyshell#19>", line 2, in mapped
    return ord(x)+10
TypeError: ord() expected a character, but string of length 5 found
list(map(mapped("magic")))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list(map(mapped("magic")))
  File "<pyshell#19>", line 2, in mapped
    return ord(x)+10
TypeError: ord() expected a character, but string of length 5 found
list(map(mapped,"magic"))
[119, 107, 113, 115, 109]
list(filter(lambda x:x%2,range(10)))
[1, 3, 5, 7, 9]
def counter():
    i = 0
    while i<=5:
        yield i
        i+=1

        
counter()
<generator object counter at 0x10510e960>
c = counter()
c
<generator object counter at 0x10510c510>
next(c)
0
next(c)
1
next(c)
2
next(c)
3
next(c)
4
next(c)
5
next(c)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    next(c)
StopIteration
for i in c:
    print(i)

    
def counter():
    i = 0
    while i<=5:
        yield i
        i+=1

        
for i in counter():
    print(i)

    
0
1
2
3
4
5
c = counter()
c
<generator object counter at 0x10510e9d0>
c[1]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    c[1]
TypeError: 'generator' object is not subscriptable
def fib():
    num1 = 0
    num2 = 1
    while True:
        yield num1
        num1,num2 = num2,num1+num2

        
f = fib()
next(f)
0
next(f)
1
next(f)
1
next(f)
2
next(f)
3
for i in fib():
    print(i)

    
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
121393
196418
317811
514229
832040
1346269
2178309
3524578
5702887
9227465
14930352
24157817
39088169
63245986
102334155
165580141
267914296
433494437
701408733
1134903170
1836311903
2971215073
4807526976
7778742049
12586269025
20365011074
32951280099
53316291173
86267571272
139583862445
225851433717
365435296162
591286729879
956722026041
1548008755920
2504730781961
4052739537881
6557470319842
10610209857723
17167680177565
27777890035288
44945570212853
72723460248141
117669030460994
190392490709135
308061521170129
498454011879264
806515533049393
1304969544928657
2111485077978050
3416454622906707
5527939700884757
8944394323791464
14472334024676221
23416728348467685
37889062373143906
61305790721611591
99194853094755497
160500643816367088
259695496911122585
420196140727489673
679891637638612258
1100087778366101931
1779979416004714189
2880067194370816120
4660046610375530309
7540113804746346429
12200160415121876738
19740274219868223167
31940434634990099905
51680708854858323072
83621143489848422977
135301852344706746049
218922995834555169026
354224848179261915075
573147844013817084101
927372692193078999176
1500520536206896083277
2427893228399975082453
3928413764606871165730
6356306993006846248183
10284720757613717413913
16641027750620563662096
26925748508234281076009
43566776258854844738105
70492524767089125814114
114059301025943970552219
184551825793033096366333
298611126818977066918552
483162952612010163284885
781774079430987230203437
1264937032042997393488322
2046711111473984623691759
3311648143516982017180081
5358359254990966640871840
8670007398507948658051921
14028366653498915298923761
22698374052006863956975682
36726740705505779255899443
59425114757512643212875125
96151855463018422468774568
155576970220531065681649693
251728825683549488150424261
407305795904080553832073954
659034621587630041982498215Traceback (most recent call last):
  File "<pyshell#10>", line 2, in <module>
    print(i)
KeyboardInterrupt
(i**2 for i in range(10))
<generator object <genexpr> at 0x107ec0510>
t = (i**2 for i in range(10))
for i in t:
    print(t)

    
<generator object <genexpr> at 0x107f05bd0>
<generator object <genexpr> at 0x107f05bd0>
<generator object <genexpr> at 0x107f05bd0>
<generator object <genexpr> at 0x107f05bd0>
<generator object <genexpr> at 0x107f05bd0>
<generator object <genexpr> at 0x107f05bd0>
<generator object <genexpr> at 0x107f05bd0>
<generator object <genexpr> at 0x107f05bd0>
<generator object <genexpr> at 0x107f05bd0>
<generator object <genexpr> at 0x107f05bd0>
next(t)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    next(t)
StopIteration
t = (i**2 for i in range(10))
next(t)
0
next(t)
1
next(t)
4
for i in t:
    print(i)

    
9
16
25
36
49
64
81
print(i)
81
