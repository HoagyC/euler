import math
def run(x):
    count=[0]*(int(x))
    for i in range(int(x/2)):
        for j in range(i):
            k = math.sqrt((i**2)+(j**2))
            if k.is_integer() and i+j+k < 1000:
                count[int(i+j+k)]+=1
    return count.index(max(count))
    


print(run(1000))
