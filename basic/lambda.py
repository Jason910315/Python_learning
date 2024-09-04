def square(x,y):
    return x**y

a = square(2,3)
b = lambda x,y:x**y
#print(a)
#print(b(2,3))

def abs_number(x):
    if x > 0:
        return x
    else:
        return -x
    
abs = lambda x:x if x > 0 else -x
#print(abs_number(-5))
#print(abs(-5))

list1 = lambda n :[i  for i in range(n)]
print(list1(5))