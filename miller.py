import random


def miller_rabin_pass(a, s, d, n):
    """
    check si n respect bien le miller_rabin test
    """
    a_to_power = pow(a, d, n)
    i = 0

    if a_to_power == 1:
        return True

    # a^(d*2^i) = n-1 mod n
    while i < s - 1:
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
        i += 1

    return a_to_power == n - 1


def miller_rabin(n):
    """
    Applique le MillerRabin Test
    """
    # check pour n-1 = (2^s)d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    K = 20
    i = 1
    while i <= K:
        a = random.randrange(2, n - 1)
        if not miller_rabin_pass(a, s, d, n):
            return False
        i += 1

    return True


def gen_prime(nbits):
    """
    Genere un nombre premier
    """
    while True:
        p = random.getrandbits(nbits)
        # force p to have nbits and be odd
        p |= 2 ** nbits | 1
        if miller_rabin(p):
            return p


def gen_prime_range(start, stop):
    """
    Genere un nombre premier entre deux bornes
    """
    while True:
        p = random.randrange(start, stop - 1)
        p |= 1
        if miller_rabin(p):
            return p
