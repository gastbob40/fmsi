import random, miller, arith


def get_prime_pair(bits=512):
    """
    Genere une paire de clef qui respect:
    p < q < 2p
    """
    p = miller.gen_prime(bits)
    q = miller.gen_prime_range(p + 1, 2 * p)
    return p, q


def generate_keys(nbits=1024):
    """
    Genere une pair de clef privée / publique
    de n bits de long
    """

    p, q = get_prime_pair(nbits // 2)
    n = p * q
    phi = arith.totient(p, q)

    # genere une clef avec d ^ n = 1
    while True:
        d = random.getrandbits(nbits // 4)
        if arith.gcd(d, phi) == 1 and 36 * pow(d, 4) < n:
            return arith.mod_inverse(d, phi), n, d
    return None
