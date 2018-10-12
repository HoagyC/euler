def run(n,k):
    a=[0]
    s=[0]
    for i in range (1,n+1):
        a.append(bin(i & (i << 1)).count("1"))
    print('done a')
    for i in range(1,n+1):
        s.append(s[i-1]+((-1)**a[i]))
    print('done s')
    seq=[1,1]
    for i in range(k):
        seq.append(seq[-1]+seq[-2])
    print('done seq')
    GF=[]
    for i in range(2,k):
        print(seq[i],seq[i-1])
        GF.append([j for j, n in enumerate(s) if n == seq[i]][seq[i-1]-1])
    return(sum(GF))
    
print(run(10000000,4))
