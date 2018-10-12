import math
def getseq(n):
    a = []
    for i in range(1,n+1):
        b = 0
        for j in range(11):
            b += ((-1*i)**j)
        a.append(b)
    print (a)
    return a
    
def getCoeff(x,seq):
    # takes the first x of the sequence, takes x-1 differences, returns the final difference
    difs = [seq[0:x]]
    while len(difs[-1])>1:
        difs.append([j-i for i, j in zip(difs[-1][:-1], difs[-1][1:])])
    coeff = difs[-1][0]/(math.factorial(x-1))
    return coeff

def findbest(x,seq):
    print (seq)
    currentseq = seq[:]
    for i in range(x):
        b = getCoeff(x-i,currentseq)
        for j in range(len(seq)):
            currentseq[j] -= b*((j+1)**(x-i-1))

    prediction = [i-j for i,j in zip(seq,currentseq)]
    return (prediction[x])

def run(n):
    total = 0
    seq = []
    # seq = getseq(n)
    for j in range(n):
        seq.append((j+1)**3)
    print(seq)
    for i in range(1,n):
        add = findbest(i,seq)
        total += add
    return (total)
print(run(10))
