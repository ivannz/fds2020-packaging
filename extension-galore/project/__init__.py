from .primes import primes as py
from .pyx import primes as pyx
from .cpp import primes as cpp


def test(n_primes):
    n_primes = min(n_primes, 10000)

    result = py(n_primes)
    for fn in [pyx, cpp]:
        assert result == fn(n_primes)
