# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def find9(j):
    k = 1
    while True:
        if (10**k-1)%j == 0:
            return(k)
        else:
            k += 1


def run(n):
    kmax = 0
    jmax = 0
    numbers = range(2,n)
    for i in range(len(numbers)):
        if numbers[i] != 0:
            for j in range(numbers[i]+i,len(numbers),numbers[i]):
                numbers[j] = 0
    primes = filter(lambda x: x,numbers)
    del primes[0:3]
    for j in primes:
        k = find9(j)
        if k > kmax:
            # print(j,k)
            kmax = k
            jmax = j
            
    return(jmax)

if __name__ == "__main__":
    print(run(1000))