# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def run():
    fac = str(2**1000)
    dig = [int(fac[x]) for x in range(len(fac))]
    return(sum(dig))

if __name__ == "__main__":
    print(run())