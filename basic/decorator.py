def print_fuction_name(callback):
    def wrapper():
        print("Now use function '{}'".format(callback.__name__))
        callback()
    return wrapper

def dog_wolf():
    print("wolfwolf")

def cat_meow():
    print("meowmeow")

#定義裝飾器內容
def Dec(callback):
    def wrapper():
        print("裝飾器的程式碼")
        callback()
    return wrapper

@Dec #語法糖
def func():
    print("普通函式程式碼")

#func()  #call func()後會先執行裝飾器Dec內的程式，後呼叫原函式
'''
def print_func_name(func):
    def warp_1():
        print("Now use function '{}'".format(func.__name__))
        func()
        print("print_func_name_end")
    return warp_1

def print_time(func):
    import time
    def warp_2():
        print("Now the Unix time is {}".format(int(time.time())))
        func()
        print("print_time_end")
    return warp_2

@print_func_name
@print_time
def dog_bark():
    print("Bark !!!") 
'''

def Decorator(func):
    def print_msg(msg):
        print("現在是裝飾器內部")
        func(msg)
    return print_msg

@Decorator
def func1(msg):
    print(msg)

#func1("現在是一般函式")

#設計一個可以接收整數n的裝飾器，計算1+2+...+n
def caculate(n):
    def decorator(func):
        def wrapper():
            result = 0
            for i in range(n):
                result += n
            print(result)
            func()
        return wrapper
    return decorator

@caculate(n = 50)
def print_result():
    print("This is result")

#print_result()
import time
def showTimer(title):
    def timer(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            elapsed_time = (time.time() - start_time) * 1000
            print(f"\n{title} {elapsed_time:.06f} ms")
        return wrapper
    return timer

@showTimer("運行時間為:")
def print_list(start,end,step):
    list1 = []
    for i in range(start,end,step):
        list1.append(i)
    print(list1)

#print_list(1,100,10)

class Test:
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)

@Test
def calling(a,b):
    print("calling function with",a,"and",b)

calling(3,4)


