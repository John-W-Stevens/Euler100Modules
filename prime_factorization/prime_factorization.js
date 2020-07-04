const { prime_sieve } = require("./prime_sieve");

module.exports = {
    primeFactorization: function(n, primes=[], numDivisors=false){
        const factors = {};
        primes === [] ? primes = prime_sieve(n) : primes;
        for (const p of primes){
            if (n % p === 0){
                factors[p] = 1;
                let base = p;
                let exp = 2;
                while (n % (base**exp) === 0){
                    factors[p] = exp;
                    exp += 1;
                }
            }
        }
        if (numDivisors !== false){
            let divisors = 1;
            for (const exp of Object.values(factors)){
                divisors *= (exp + 1);
            }
            return divisors;
        }
        else { return factors; } 
    }
}