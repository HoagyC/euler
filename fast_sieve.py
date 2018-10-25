import numpy
import math
def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(int(n/2), dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1


print(primesfrom3to(int(1e9)))
