# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

def run():
    nums = []
    for i in range(math.factorial(9)*10):
        j = sum(math.factorial(int(str(i)[k])) for k in range(len(str(i))))
        if i == j:
            print i
            nums.append(i)
    return(sum(nums))
if __name__ == "__main__":
    print(run())