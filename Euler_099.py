import math

def run():
    pairs = []
    currentmax = 0
    FILE = open("99base_exp.txt")
    for row in FILE: pairs.append([int(i) for i in row.split(",")])
    for i in range(len(pairs)-1):
        current = pairs[i][1]*math.log(pairs[i][0])
        if currentmax < current:
            currentmax = current
            print(pairs[i],i)
    

if __name__ == "__main__":
    print(run())