import time
import math

def run(a,b):
    print('ahh')
    t=time.clock()
    numbers = list(range(2,a+1))
    for i in range(len(numbers)):
        if numbers[i] != 0:
            for j in range(numbers[i]+i,len(numbers),numbers[i]):
                numbers[j] = 0
    primes = filter(lambda x: x,numbers)
    factors = [[] for _ in range(a+1)]
    factors[1]=[1]
    for i in range(2,a+1):
        if numbers[i-2]!=0:
            for j in range(i,len(factors),i):
                factors[j].append(i)
    count=0
    print('ooo')
    for i in range(1,a+1):
        add=1
        for j in range(len(factors[i])):
            add*=factors[i][j]**b
        count+=add
    return(count%(1e9+1),time.clock()-t)
for i in range(5):   
    print(run(int(1e6),i+1))
