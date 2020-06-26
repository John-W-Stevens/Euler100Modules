
const now = require("performance-now");
const {range, compress} = require("./utils");

const primeSieve = n => {
   // Returns a list of primes < n for n > 2
   let sieve = new Array( Math.floor(n / 2) ).fill(1)
   for (var i = 3; i < parseInt(n**0.5, 10) + 1; i += 2 ){
      if (sieve[Math.floor(i / 2)]){
         for (var j = Math.floor(i*i/2); j < sieve.length; j += i){
            sieve[j] = 0;
         }      
      }
   }
   return [2].concat(compress(range(3, n, 2), sieve.slice(1,)))
}

let start = now();
let primes = primeSieve(30000000)
console.log(`${primes.length} primes found in ${(now() - start) / 1000} seconds.`) 
// 1857859 primes found in 3.299167571 seconds. With an input of 30 million
