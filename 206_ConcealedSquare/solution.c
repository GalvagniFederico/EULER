// Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
// where each "_" is a single digit.

#include <stdio.h>
#include <time.h>
#include <stdbool.h>
#include <math.h>

bool check(long long n) {
    // Expected digits at positions 0,2,4,...,18 (from the right after removing trailing 0)
    // Pattern: 1_2_3_4_5_6_7_8_9_0
    // Check from right to left using modulo
    int expected[] = {0, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    long long sq = n * n;
    for (int i = 0; i < 10; i++) {
        int digit = sq % 10;
        if (digit != expected[i]) return false;
        sq /= 100; // skip the wildcard digit
    }
    return true;
}

int main() {
    clock_t start = clock();

    long long n_min = (long long)sqrt(1e18);
    long long n_max = (long long)sqrt(1.9293949596979899e18) + 1;

    // Round n_min down to multiple of 100
    n_min -= n_min % 100;

    for (long long i = n_min; i <= n_max; i += 100) {
        if (check(i + 30)) { printf("%lld\n", i + 30); break; }
        if (check(i + 70)) { printf("%lld\n", i + 70); break; }
    }

    double elapsed = (double)(clock() - start) / CLOCKS_PER_SEC;
    printf("Process finished --- %f seconds ---\n", elapsed);

    return 0;
}
