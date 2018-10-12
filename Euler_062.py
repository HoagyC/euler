import math
def represent(n):
    a = n**3
    b = []
    while a:
        b.append(a%10)
        a = a//10
    return (sorted(b))
    
def run(k):
    i = 0
    rlist = []
    count = []
    while True:
        count.append(1)
        c = represent(i)
        if c in rlist:
            count[rlist.index(c)] += 1
            if count[rlist.index(c)] == k:
                final = []
                for b in range(1,k+1):
                    print(b,count.index(b))
                    final.append(count.index(b))
                return final
        rlist.append(c)
        i += 1
d = run(5)
print(d,(d[-1]**3))
