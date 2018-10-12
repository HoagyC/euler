import math
def getseq(n):
    # produces the sequence 1-n+n^2-n^3....
    a = []
    for i in range(1,n+1):
        b = 0
        for j in range(11):
            b += ((-1*i)**j)
        a.append(b)
    print (a)
    return a
    
def getCoeff(x,seq):
    # takes the first x of the sequence, finds the differences x-1 times then divides by (x-1)! to find the x-1 coefficient. 
    difs = [seq[0:x]]
    while len(difs[-1])>1:
        difs.append([j-i for i, j in zip(difs[-1][:-1], difs[-1][1:])])
    coeff = difs[-1][0]/(math.factorial(x-1))
    return coeff

def findbest(x,seq):
    currentseq = seq[:]
    for i in range(x):
        # for an estimate of power x-1, parses the sequence through x times to estimate the coefficient of x-1 to the constant
        b = getCoeff(x-i,currentseq)
        for j in range(len(seq)):
            # subtracts the estimate for the higher power before estimating the next coefficient
            currentseq[j] -= b*((j+1)**(x-i-1))

    prediction = [i-j for i,j in zip(seq,currentseq)]
    print(prediction)
    return (prediction[x])

def run(n):
    total = 0
    seq = []
    seq = getseq(n)
    for i in range(1,n):
        # runs the estimating function n-1 times
        add = findbest(i,seq)
        if seq[i] != add:
            total += add
    return (total)
print(run(15))
