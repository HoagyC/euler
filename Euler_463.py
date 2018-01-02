# The function f is defined for all positive integers as follows:

# f(1)=1f(1)=1
# f(3)=3f(3)=3
# f(2n)=f(n)f(2n)=f(n)
# f(4n+1)=2f(2n+1)−f(n)f(4n+1)=2f(2n+1)−f(n)
# f(4n+3)=3f(2n+1)−2f(n)f(4n+3)=3f(2n+1)−2f(n)
# The function S(n)S(n) is defined as ∑ni=1f(i)∑i=1nf(i).

# S(8)=22S(8)=22 and S(100)=3604S(100)=3604.

# Find S(337)S(337). Give the last 9 digits of your answer.

import math

def oddtri(n):
    tri = math.floor((n+1)//2)
    total = (tri*tri+1)-1
    print(total)
    return(total)
    
def run(m):
    r = m
    count = 0
    for i in range(m.bit_length()):
        count += oddtri(r)
        r = r//2
    return(count)

if __name__ == "__main__":
    print(run(18))