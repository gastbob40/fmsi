import time

import fractions, arith, key_generator


def rsa_hack(e, n):
    """
    applique Wiener continued fraction attack
    """
    frac = fractions.rational_to_contfrac(e, n)
    convergents = fractions.convergents_from_contfrac(frac)

    for (k, d) in convergents:

        # si d est la clef recherché
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1

            # check x^2 - s*x + n = 0
            discs = s * s - 4 * n
            if discs >= 0:
                t = arith.is_perfect_square(discs)
                if t != -1 and (s + t) % 2 == 0:
                    print("Hacked!")
                    return d


# TEST functions
def benchmark(nb_times=2, key_size=1024):
    work = 0
    creation_time = 0
    total_time = 0

    print("Test de l'attaque de Wiener avec la clé de", key_size, "bits\n")

    for times in range(nb_times):
        t = time.time()
        print("Création de la clef en cours ...")

        e, n, d = key_generator.generate_keys(key_size)
        current_creation_time = time.time() - t
        creation_time += current_creation_time
        print("terminer en", current_creation_time)
        t = time.time()
        print("Clef publique:")
        print("e = ", e)
        print("n = ", n)

        print("Début du hack ...")
        hacked_d = rsa_hack(e, n)

        print("Clef privé:")
        print("Attendu :", d)
        print("Recu :", hacked_d)

        if d == hacked_d:
            print("Hacking réussi")
            work += 1
        else:
            print("Hacking non réussi")
        current_time = time.time() - t
        total_time += current_time
        print("Temps de décryption:", current_time, " secondes.")

        print("-------------------------\n")
    print("Résumé :")
    print("Wiener lancé", nb_times, "fois.")
    print("Avec", work, "réussites and", nb_times - work, "échecs.")
    print("Temps moyen de création :", creation_time / nb_times, "secondes par hack.")
    print("Temps moyen de hacking :", total_time / nb_times, "secondes par hack.")


if __name__ == "__main__":
    benchmark()
