import math
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    returns
    
def length(x):
    return(len(str(x)))
def run(n):
    count = 0
    x=1
    y=2
    for i in range(n):
        x,y=y,2*y+x
        if length(x+y)>length(y):
            count+=1
    return(count)


print(run(1000))
