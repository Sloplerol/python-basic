Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
age = 16
if age <18:
    print("未成年")
else:
    print("欢迎使用")

    
未成年
print("未成年") if age<18 else print("欢迎使用")
未成年
score = 69
if 0<score<=30:
    print("D")
elif 30<score<=60:
    print("C")
elif 60<score<=80:
    print("B")
elif 80<score<=90:
    print("A")
elif 90<score<=100:
    print("S")
else:
    print("请输入100以内的数字")

    
B
level = ("D" if 0<score<=30 else
         "C" if 30<score<=60 else
         "B" if 60<score<=80 else
         "A" if 80<score<=90 else
         "S" if 90<score<=100 else
         "请输入100以内数字")
print(level)
B
study = "yes"
study = input("你爱学习吗?")
你爱学习吗?yes
print(study)
yes
study = "yes"
while study = "yes":
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
while study == "yes":
    study = input("你爱学习啊")

    
你爱学习啊yes
你爱学习啊yes
你爱学习啊yes
你爱学习啊no
i = 1
sum = sum + i
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    sum = sum + i
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'int'
i = 1
sum = 0
while i<=100:
    sum += i
    i +=1

    
print(sum)
5050
while 1<2:
    print("6666")

    
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    print("6666")
KeyboardInterrupt
while True:
    answer = input("是否要退出循环")
    if answer = "yes":
        
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
while True:
    answer = input("是否要退出循环")
    if answer == "yes":
        break
    print("累了...")

    
是否要退出循环不
累了...
是否要退出循环不
累了...
是否要退出循环yes
i = 0
while i<=10:
    i+=1
    if i % 2==0:
        continue

    
i
11
while i<=10:
    i+=1
    if i % 2==0:
        continue
    print(i)

    
i
11
i = 0
while i<10:
    i+=1
    if i %2 == 0:
        continue
    print(i)

    
1
3
5
7
9
day = 0
while day<7
SyntaxError: expected ':'
while day<7:
    answer = input("study?")
    if answer == "no":
        break
    day+=1
    else:
        
SyntaxError: invalid syntax
while day<7:
    answer = input("study?")
    if answer == "no":
        break
    day+=1
else:
    print("congratulation")

    
study?yes
study?yes
study?yes
study?yes
study?yes
study?yes
study?yes
congratulation
while day<7:
    answer = input("study?")
    if answer == "no":
        break
    day+=1
else:
    print("congratulation")

congratulation
day = 0
while day<7:
    answer = input("study?")
    if answer != "yes":
        break
    day+=1
else:
    print("congratulation")

study?yes
study?no
i = 1
while i<10:
    j = 1
    while j<=i:
        print(i,"*",j,"=",i*j,end = " ")
        j+=1
    print()
    i+=1

    
1 * 1 = 1 
2 * 1 = 2 2 * 2 = 4 
3 * 1 = 3 3 * 2 = 6 3 * 3 = 9 
4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16 
5 * 1 = 5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25 
6 * 1 = 6 6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36 
7 * 1 = 7 7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49 
8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 
9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81 
while i<10:
    j = 1
    while j<=i:
        print(i,"*",j,"=",i*j)
        j+=1
    print()
    i+=1

    
print(i*j)
100
i = 0
for i in len("What"):
    print("What"[i])
    i+=1

    
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    for i in len("What"):
TypeError: 'int' object is not iterable
while i<len("What")
    print("What"[i])
    i+=1
    
SyntaxError: expected ':'
while i<len("What"):
    print("What"[i])
    i+=1

    
W
h
a
t
sum = 0
for i in range(10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
for i in range(5,10)
SyntaxError: expected ':'
for i in range(5,10):
    print(i)

    
5
6
7
8
9
for i in range(4,10,2):
    print(i)

    
4
6
8
sum = 0
for i in range(11):
    sum+=i

    
print(sum)
55
for x in range(2,11):
    for n in x:
        if x%n == 0:
            print(x,"=",n,"*",x//n)
            break
    else:
        print("素数")

        
Traceback (most recent call last):
  File "<pyshell#133>", line 2, in <module>
    for n in x:
TypeError: 'int' object is not iterable
for x in range(2,11):
    for n in range(2,x):
        if x%n == 0:
            print(x,"=",n,"*",x//n)
            break
    else:
        print("素数")

        
素数
素数
4 = 2 * 2
素数
6 = 2 * 3
素数
8 = 2 * 4
9 = 3 * 3
10 = 2 * 5
for x in range(2,11):
    for n in range(2,x):
        if x%n == 0:
            print(x,"=",n,"*",x//n)
            break
    else:
        print(x,"素数")

        
2 素数
3 素数
4 = 2 * 2
5 素数
6 = 2 * 3
7 素数
8 = 2 * 4
9 = 3 * 3
10 = 2 * 5
for x in range(2,11):
    for n in range(2,x):
        if x%n == 0:
            print(x,"=",n,"*",x//n)
            break
        else:
            print(x,"素数")

            
3 素数
4 = 2 * 2
5 素数
5 素数
5 素数
6 = 2 * 3
7 素数
7 素数
7 素数
7 素数
7 素数
8 = 2 * 4
9 素数
9 = 3 * 3
10 = 2 * 5
