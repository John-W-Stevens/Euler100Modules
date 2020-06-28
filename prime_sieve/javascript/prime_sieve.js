const { range, compress } = require("./utils")

module.exports = {
    primeSieve: function(n){
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
}