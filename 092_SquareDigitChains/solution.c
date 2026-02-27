#include <stdio.h>
#include <time.h>
#include <stdbool.h>

int main() {
    clock_t start = clock();

    // Precompute square digit sums for 0-999
    int sds[1000] = {0};
    for (int i = 0; i < 1000; i++) {
        int n = i, s = 0;
        while (n > 0) {
            int d = n % 10;
            s += d * d;
            n /= 10;
        }
        sds[i] = s;
    }

    // Determine which numbers 1-567 end at 89
    bool ends_at_89[568] = {false};
    for (int i = 1; i < 568; i++) {
        int n = i;
        while (n != 1 && n != 89) {
            n = sds[n];
        }
        ends_at_89[i] = (n == 89);
    }

    // Count numbers below 10M that end at 89
    int count = 0;
    for (int i = 1; i < 10000000; i++) {
        int s = sds[i % 1000] + sds[i / 1000 % 1000] + sds[i / 1000000];
        if (ends_at_89[s]) {
            count++;
        }
    }

    double elapsed = (double)(clock() - start) / CLOCKS_PER_SEC;
    printf("%d\n", count);
    printf("Process finished --- %f seconds ---\n", elapsed);

    return 0;
}
