def rational_to_contfrac(x, y):
    '''
    change x/y en une list de quotients [a0, ..., an]
    '''
    a = x // y
    pquotients = [a]
    while a * y != x:
        x, y = y, x - a * y
        a = x // y
        pquotients.append(a)
    return pquotients


def convergents_from_contfrac(frac):
    '''
    calcule la list des convergents
    '''

    def contfrac_to_rational(frac):
        '''
            change [a0, ..., an] en x/y.
        '''
        if len(frac) == 0:
            return 0, 1
        num = frac[-1]
        denom = 1
        for _ in range(-2, -len(frac) - 1, -1):
            num, denom = frac[_] * num + denom, num
        return num, denom

    conv = []
    for i in range(len(frac)):
        conv.append(contfrac_to_rational(frac[0:i]))
    return conv
