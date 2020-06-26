
def prime_sieve(n):
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]*(n//2))
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2] + [ d for d,s in zip(range(3,n,2), sieve[1:]) if s ]

import time
start = time.time()
primes = prime_sieve(50000000)
print(f"{len(primes)} found in {time.time() - start} seconds.")
# 3001134 found in 1.7941629886627197 seconds. With input of 50,000,000