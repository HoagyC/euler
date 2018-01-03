# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def run():
    nums = []
    FILE = open("13longnum.txt")
    for row in FILE: nums.append(int(row))
    nums = [int(x[0:15]) for x in nums]
    return(sum(nums))
    

if __name__ == "__main__":
    print(run())