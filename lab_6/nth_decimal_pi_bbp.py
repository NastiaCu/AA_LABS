import decimal


def nth_decimal_pi_bbp(n):
    decimal.getcontext().prec = n + 1

    pi = decimal.Decimal(0)
    for k in range(n):
        pi += decimal.Decimal((1 / 16**k) * ((4 / (8*k + 1)) - (2 / (8*k + 4)) - (1 / (8*k + 5)) - (1 / (8*k + 6))))

    return int(str(pi)[n])

