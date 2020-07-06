using System;
using System.Collections.Generic;
using System.Linq;
using System.Diagnostics;

namespace PrimeFacorization
{
    // Array Extension Method from PrimeSieve

    class Program
    {
       // Range, Compress, & PrimeSieve Methods from PrimeSieve

        public static Dictionary<int, int> PrimeFacorization(int n, int[] Primes)
        {
            Dictionary<int, int> PrimeFactors = new Dictionary<int, int>();
            
            foreach (int prime in Primes)
            {
                if (n % prime == 0)
                {
                    PrimeFactors[prime] = 1;
                    double p = prime;
                    double exp = 2;
                    while (n % Convert.ToInt64(Math.Pow(p, exp)) == 0)
                    {
                        PrimeFactors[prime] += 1;
                        exp += 1;
                    }
                }
            }
            return PrimeFactors;
        }
        public static long NumDivisors(Dictionary<int, int> PrimeFactors)
        {
            long Divisors = 1;
            foreach (KeyValuePair<int, int> entry in PrimeFactors)
            {
                Divisors *= entry.Value + 1;
            }
            return Divisors;
        }
        static void Main(string[] args)
        {
            Console.WriteLine("This is my C# PrimeFacorization Method");
        }
    }
}
