print('initiating')
import math
import time 

def run(n,p):
    t = time.clock()
    count=0
    primes=getPrimes(math.floor(math.sqrt(n)))
    i = 2
    pl=len(primes)-1
    while i < n+1:
        k=i
        j=0
        factors=[]
        while True:
            if k%primes[j]==0:
                factors.append(primes[j])
            while k%primes[j]==0:
                k/=primes[j]
            if k < (primes[j]**2-1) or j==pl:
                break
            j+=1
        if k>1:
            factors.append(int(k))
        for m in range(2,p+1):
            add=1
            for j in range(len(factors)):
                add*=((factors[j]**p)%1000000007)
            count+=add%1000000007
        if math.log10(i)%1==0:
            print(i,(count+1)%1000000007,time.clock()-t)
        i+=1
    print((count+1)%1000000007)
    
def getPrimes(n):
    numbers = list(range(2,n+1))
    for i in range(len(numbers)):
        if numbers[i] != 0:
            for j in range(numbers[i]+i,len(numbers),numbers[i]):
                numbers[j] = 0
    print('got primes')
    return(list(filter(lambda x: x,numbers)))
    
run(int(1e12),50)
