// The first known prime found to exceed one million digits was discovered in 1999,
// and is a Mersenne prime of the form 2^6972593 - 1; it contains exactly 2,098,960 digits.
// Subsequently other Mersenne primes, of the form 2^p - 1, have been found which contain more digits.
//
// However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits:
// 28433 * 2^7830457 + 1.
//
// Find the last ten digits of this prime number.

#include <stdio.h>
#include <time.h>

int main() {
    clock_t start = clock();

    long long mod = 10000000000LL;

    // Modular exponentiation: 2^7830457 mod 10^10
    long long base = 2;
    long long exp = 7830457;
    long long result = 1;

    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (__int128)result * base % mod;
        }
        exp /= 2;
        base = (__int128)base * base % mod;
    }

    result = ((__int128)28433 * result + 1) % mod;

    double elapsed = (double)(clock() - start) / CLOCKS_PER_SEC;
    printf("%010lld\n", result);
    printf("Process finished --- %f seconds ---\n", elapsed);

    return 0;
}
