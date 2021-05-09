def gcd(a, b):
    """
    return seulement le dernier element du epgdc
    """
    a, b = (b, a) if a < b else (a, b)
    while b:
        a, b = b, a % b
    return a


def egcd(a, b):
    """
    Algo d'Euclidean
    ax + by = gcd(a,b)
    """
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q = a // b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return u, v, a


def mod_inverse(e, n):
    """
    trouve d tel que
    d such that d * e = 1 (mod n)
    """
    return egcd(e, n)[0] % n


def bitlength(x):
    """
    trouve la taille en bit de x
    """
    assert x >= 0
    n = 0
    while x > 0:
        n = n + 1
        x = x >> 1
    return n


def totient(p, q):
    """
    totient de pq
    """
    return (p - 1) * (q - 1)


def isqrt(n):
    """
    Calcule la racine carrée d'un nombre entier
    pour des grands nombres entiers non négatifs arbitraires
    """
    if n < 0:
        raise ValueError('N doit être positif !!')

    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def is_perfect_square(n):
    """
    Return la racine de N si N est une racine parfaire
    Retoune -1 sinon
    """
    h = n & 0xF  # Récupère le dernier chiffre hexa

    if h > 9:
        return -1

    # Tirer parti de l'évaluation booléenne des courts-circuits
    if h not in [2, 3, 5, 6, 7, 8]:
        t = isqrt(n)
        if t * t == n:
            return t
    return -1
