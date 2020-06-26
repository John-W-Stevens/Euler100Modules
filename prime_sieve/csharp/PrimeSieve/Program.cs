using System;
using System.Collections.Generic;
using System.Linq;
using System.Diagnostics;

namespace PrimeSieve
{
    public static class ArrayExtensions
    {
        // https://stackoverflow.com/questions/14919234/fill-an-array-in-c-sharp
        public static void Fill<T>(this T[] originalArray, T with)
        {
            for (int i = 0; i < originalArray.Length; i++) { originalArray[i] = with; }
        }
    }

    class Program
    {

        public static List<int> Range(int start, int stop, int step)
        {
            List<int> range = new List<int>();
            for (int i = start; i <= stop; i += step) { range.Add(i); }
            return range;
        }

        public static List<int> Compress(int[] arr1, int[] arr2)
        {
            List<int> CompressedList = new List<int>();
            foreach (var element in arr1.Select( (e, i) => new int[] { e, arr2[i] }))
            {
                if (element[1] == 1) { CompressedList.Add(element[0]); }
            }
            return CompressedList;
        }

        public static int[] PrimeSieve(int n)
        {
            int limit = Convert.ToInt32(Math.Floor(Convert.ToDecimal(n) / 2));
            int[] Sieve = new int[limit];
            Sieve.Fill(1);

            for (int i = 3; i < Convert.ToInt32(Math.Pow(n, 0.5) + 1); i += 2)
            {
                if (Sieve[Convert.ToInt32(Math.Floor(Convert.ToDecimal(i) / 2))] == 1)
                {
                    int start = Convert.ToInt32(Math.Floor(Math.Pow(i, 2) / 2));
                    for (int j = start; j < Sieve.Length; j += i)
                    {
                        Sieve[j] = 0;
                    }
                }
            }

            var segment = new ArraySegment<int>(Sieve, 1, Sieve.Length - 1);

            int[] x = new int[1] { 2 };
            int[] y = Compress(Range(3, n, 2).ToArray(), segment.ToArray()).ToArray();

            int[] PSieve = new int[x.Length + y.Length];
            x.CopyTo(PSieve, 0);
            y.CopyTo(PSieve, x.Length);
            return PSieve;
        }

        static void Main(string[] args)
        {
            Stopwatch Timer = new Stopwatch();
            Timer.Start();
            int[] Primes = PrimeSieve(50000000);
            Timer.Stop();
            Console.WriteLine($"{Primes.Length} primes found in {Timer.Elapsed} time.");
            // 3,001,134 primes found in 00:00:01.6058107 time. With an input of 50 miillion
        }
    }
}
