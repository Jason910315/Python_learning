list = [n ** 2 for n in range(12)]  #典型的列表推導
gen = (n ** 2 for n in range(12))  #典型的產生器表示式
#print(list)
#print(gen)
#print("This is i")
#for i in gen:
    #print(i,end=' ')
#print("\nThis is j")
#for j in gen:
    #print(j)

def print_Max(max):
    n = 0
    while n <max:
        yield n
        n = n +1
gen = print_Max(5)
a = []
for i in range(5):
    a.append(next(gen))
#print(a)

def yieldTest():
    yield 1
    yield 3
    yield 5

generator = yieldTest()
#for i in generator:
    #print(i,end = ' ')

#實作一個能查到1~N中的質數的機器
def getPrimes(N):
    primes = set()
    for n in range(2,N):
        if all(n % p > 0 for p in primes): #若現在的數字N mod前面已找到的質數，>0代表不能被整除
            primes.add(n)
            yield n
print(*getPrimes(40))