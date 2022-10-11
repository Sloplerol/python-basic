Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def myfuc():
    print("过载中...")

    
def mid(what):
    print("启动完毕")
    what()
    print("boom")

    
mid(myfuc)
启动完毕
过载中...
boom
import time():
    
SyntaxError: invalid syntax
import time
def time_c(fuc):
    print("开始执行程序")
    start = time.time()
    fuc()
    end = time.time()
    print("程序结束")
    print(f"共花费了{(end-start):.2f}秒")

    
def myfuc():
    sleep(2)
    print("calculating")

    
time_c(myfuc)
开始执行程序
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    time_c(myfuc)
  File "<pyshell#18>", line 4, in time_c
    fuc()
  File "<pyshell#22>", line 2, in myfuc
    sleep(2)
NameError: name 'sleep' is not defined
def myfuc():
    time.sleep(2)
    print("calculating")

    
time_c(myfuc)
开始执行程序
calculating
程序结束
共花费了2.07秒
def time_c(fuc):
    def time_b:
        print("开始执行程序")
        start = time.time()
        fuc()
        end = time.time()
        print("程序结束")
        print(f"共花费了{(end-start):.2f}秒")
        
SyntaxError: invalid syntax
def time_c(fuc):
    def time_b():
        print("开始执行程序")
        start = time.time()
        fuc()
        end = time.time()
        print("程序结束")
    return time_b

def myfuc():
    time.sleep(2)
    print("calculating")

    
med = time_c()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    med = time_c()
TypeError: time_c() missing 1 required positional argument: 'fuc'
med = time_c(myfuc)
med()
开始执行程序
calculating
程序结束
def time_c(fuc):
    def time_b():
        print("开始执行程序")
        start = time.time()
        fuc()
        end = time.time()
        print("程序结束")
        print(f"共花费了{(end-start):.2f}秒")

        
@time_c
def myfuc():
    time.sleep(2)
    print("calculating")
def game(arg):
    def main(mine):
        def satrol():
            print("开始执行")
            start = time.time()
            mine()
            end = time.time()
            print(f"{[arg]}一共耗费了{(end-start)}秒")
        return satrol
    return main

def funA():
    time.sleep(2)
    print("Hello,world")

    
funA = game(arg='A')(funA)
funA()
开始执行
Hello,world
['A']一共耗费了2.092097759246826秒
def funB():
    time.sleep(2)
    print("Hello,world")

    
funB = game(arg = 'B')(funB)
funB
<function game.<locals>.main.<locals>.satrol at 0x10332f2e0>
funB()
开始执行
Hello,world
['B']一共耗费了2.0921871662139893秒

    
