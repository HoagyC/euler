import time
import math
def run(n):
    print("going")
    t = time.clock()
    a = 0
    fact=1
    for i in range(n):
        if i%1e7==0:
            print(i)
        if i != 0:
            fact=(fact*i)%1008691207
        a = (a + (n-3-i)*fact)%1008691207 #total is n! less all possible permutations including a NW-SE line of pawns across the board
    a += (fact*n)%1008691207
    print((a+1)%1008691207)
    return(time.clock()-t)

print(run(int(1e8)),"seconds")
