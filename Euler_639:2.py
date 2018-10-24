print('initiating')
import math
import time 

def run(n,p):
    t = time.clock()
    count=0
    # only need primes up to sqrt(n)
    primes=getPrimes(math.floor(math.sqrt(n)))
    i = 2
    pl=len(primes)-1
    # goes through from i = 0 to 1e12 (no for loop cause the range is too large)
    while i < n+1:
        k=i
        j=0
        factors=[]
        while True:
            # goes through the list of primes for divisors
            # when it finds one it appends it to factors
            if k%primes[j]==0:
                factors.append(primes[j])
            while k%primes[j]==0:
                # keeps dividing by the found factor as long as possible
                k/=primes[j]
            if k < (primes[j]**2-1) or j==pl:
                break
            j+=1
        if k>1:
            # primes can only have one prime factor above sqrt(n)
            # after removing all lower prime factors, this is what remains
            factors.append(int(k))
        for m in range(1,p+1):
            # add calculates the multiplicative function for power m, s.t. modulo
            add=1
            for j in range(len(factors)):
                add*=((factors[j]**p)%1000000007)
            count+=add%1000000007
        if math.log10(i)%1==0:
            print(i,(count+1)%1000000007,time.clock()-t)
        i+=1
    print((count+1)%1000000007)
    
def getPrimes(n):
    # prime sieve up to n
    numbers = list(range(2,n+1))
    for i in range(len(numbers)):
        if numbers[i] != 0:
            for j in range(numbers[i]+i,len(numbers),numbers[i]):
                numbers[j] = 0
    return(list(filter(lambda x: x,numbers)))
    
run(100,1)
