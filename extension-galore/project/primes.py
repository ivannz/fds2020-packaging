def primes(nb_primes):
    n, p = 2, []
    while len(p) < nb_primes:
        for i in p:
            if n % i == 0:
                break

        else:
            p.append(n)

        n += 1
    return p
