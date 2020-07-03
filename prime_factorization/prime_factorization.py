def prime_factorization(n, primes=False, num_divisors=False):
    """
    Input is an integer
    Returns a dictionary {base:exp} for prime factors of n
    If num_divisors is selected: returns the total number of divisor of n
    """
    factors = {}
    if not primes:
        primes = prime_sieve(n)
    for p in primes:
        if n % p == 0:
            factors[p] = 1
    for p in factors.keys():
        base = p
        exp = 2
        while n % (base ** exp) == 0:
            factors[p] = exp
            exp += 1
    if num_divisors:
        divisors = 1
        for exp in factors.values():
            divisors *= exp + 1
        return divisors
    else:
        return factors