Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
try:
    1/0
except:
    ("错误")

    
'错误'
try:
    1/0
except ZeroDivisionError:
    ("错误")

    
'错误'
try:
    print(“666”)
except ZeroDivisionError:
    ("错误")
    
SyntaxError: invalid character '“' (U+201C)
try:
    1/0
except ZeroDivisionError as c:
    print(c)

    
division by zero
try:
    1/0
    20+'pig'
except (TypeError,ZeroDivisionError):
    pass

try:
    1/0
    20+'pig'
except TypeError:
    print("类型不同")
except ZeroDivisionError:
    print("除数不为零")

    
除数不为零
try:
    1/0
except:
    print("错误")
else:
    print("正确")

    
错误
try:
    1/1
except:
    print("错误")
else:
    print("正确")

    
1.0
正确
try:
    1/0
except:
    print("错误")
else:
    print("正确")
finally:
    print("goodbye")

    
错误
goodbye
try:
    1/1
except:
    print("错误")
else:
    print("正确")
finally:
    print("goodbye")

    
1.0
正确
goodbye
try:
    f = open("url.txt",'w')
    f.write("你很强")
except:
    print("出错了")
finally:
    f.close()

    
3
try:
    while True:
        pass
finally:
    print("晚安玛卡巴卡")

    
晚安玛卡巴卡
Traceback (most recent call last):
  File "<pyshell#50>", line 2, in <module>
    while True:
KeyboardInterrupt
try:
    try:
        1/0
    except:
        print("内部异常")
    22+"666"
except:
    print("外部异常")
finally:
    print("程序终止")

    
内部异常
外部异常
程序终止
try:
    22+"666"
    try:
        1/0
    except:
        print("内部异常")
    
except:
    print("外部异常")
finally:
    print("程序终止")

    
外部异常
程序终止
raise ValueError("值不正确")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    raise ValueError("值不正确")
ValueError: 值不正确
try:
    1/0
except:
    raise ValueError("取代我?")

Traceback (most recent call last):
  File "<pyshell#69>", line 2, in <module>
    1/0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#69>", line 4, in <module>
    raise ValueError("取代我?")
ValueError: 取代我?
raise ValueError("666") from ZeroDivisionError
ZeroDivisionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    raise ValueError("666") from ZeroDivisionError
ValueError: 666
a = "666"
assert a=="666"
assert a!="666"
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    assert a!="666"
AssertionError
try:
    while True:
        while True:
            for i in range(10):
                if i > 3:
                    print(i)
            print("666")
        print('666')
    print("666")
except:
    print("完事")

    
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
6
7
8
9
666
4
5
完事
try:
    while True:
        while True:
            for i in range(10):
                if i < 3:
                    raise
                    print(i)
            print("666")
        print('666')
    print("666")
except:
    print("完事")

    
完事
try:
    while True:
        while True:
            for i in range(10):
                if i < 3:
                        raise
                print(i)
            print("666")
        print('666')
    print("666")
except:
    print("完事")

    
完事
try:
    while True:
        while True:
            for i in range(10):
                if i > 3:
                        raise
                print(i)
            print("666")
        print('666')
    print("666")
except:
    print("完事")

    
0
1
2
3
完事
