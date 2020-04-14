# cython: language_level=3, embedsignature=True
cimport cython


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
def primes(int nb_primes):
    cdef int n, i, len_p
    cdef int p[10000]

    nb_primes = min(nb_primes, 10000)

    len_p, n = 0, 2  # The current number of elements in p.
    while len_p < nb_primes:
        for i in p[:len_p]:
            if n % i == 0:
                break

        else:
            p[len_p] = n
            len_p += 1
        n += 1

    return [prime for prime in p[:len_p]]
