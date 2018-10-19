import time
import math
def run():
    count=0
    t = time.clock()
    for i in range(1,101):
        j=(math.factorial(i+8)/((math.factorial(8))*math.factorial(i))) #increasing numbers
        k=(math.factorial(i+9)/((math.factorial(9))*math.factorial(i))) #decreasing numbers
        count = count+j+k-10 #add new non-bouncy to count, minus 9 duplicates (1111.. etc) and special case 0
    print(count)
    return(time.clock()-t)
print(run(),"seconds")
