void primes_c(int n_primes, int *primes)
{
    int n = 0;

    for(int i=2; n < n_primes; i++) {
        for(int j=0; j < n; j++) {
            if(i % primes[j] == 0)
                goto divisible;
        }

        primes[n++] = i;

        divisible:;
    }
}