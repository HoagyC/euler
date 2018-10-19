import bisect
import time
def run():
    t = time.clock()
    h=[1]
    p=1
    for n in range(1,100000):
        h.append((h[-1]+4*n+1))
        p=p+3*n+1
        if p in h:
            print(p,time.clock()-t)
        del(h[:bisect.bisect_left(h,p)])
    return(time.clock()-t)
print(run(),"seconds")
