# coding=utf-8

#Consider quadratic Diophantine equations of the form:

# x2 – Dy2 = 1

# For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

# It can be assumed that there are no solutions in positive integers when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1

# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


# D = 11
# a^2(d+2) = (x+1)(x-1)
# multiples of d x (d+/-2) are one away from sq
# dxa(d+2) = 11*169

# 1690
# 0169
# 1859

# D + 2

# Dy2 = x2 - 1
# x2 - 1 = (x-1)(x+1)
# y2 = sumof y odd numbers
# b2y2 = x2 - 1
# b2 = (x2 - 1)/y2
# b = sqrt(x2-1)/y
# sqrt(x2-1) is int, but no

# D = x2 - 1/y = int
# x2 - 1 = Dy2

import math

def find(i):
    k = i
    if math.sqrt(i)%1 == 0:
        return(0)
    while True:
        if math.sqrt((k*(k-2))/i)%1 == 0.0:
            return(math.sqrt((k*(k-2)+1)))
        if math.sqrt((k*(k+2))/i)%1 == 0.0:
            return(math.sqrt((k*(k+2)+1)))
        k += i

def run(D):
    maxx = 0
    maxD = 0
    for i in range(D):
        x = find(i)
        if x > maxx:
            maxx = x
            maxD = i
            print(i,x)
    print(maxD)
    

if __name__ == "__main__":
    print(run(1000))