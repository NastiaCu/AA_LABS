import decimal


def nth_decimal_pi_chudnovsky(n):
    decimal.getcontext().prec = n + 10
    decimal.getcontext().Emax = 999999999

    C = 426880 * decimal.Decimal(10005).sqrt()
    M = decimal.Decimal(1)
    X = decimal.Decimal(1)
    L = decimal.Decimal(13591409)
    S = L

    for i in range(1, n + 10):
        M = decimal.Decimal(M * ((1728 * i * i * i) - (2592 * i * i) + (1104 * i) - 120) / (i * i * i))
        L = decimal.Decimal(545140134 + L)
        X = decimal.Decimal(-262537412640768000 * X)
        S += decimal.Decimal((M * L) / X)

    pi = C / S
    pi_str = str(pi)[n+1]

    return pi_str

