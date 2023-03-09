def sieve_of_eratosthenes_2(n):
    c = [True] * (n + 1)
    c[1] = False
    prime2 = []
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1
    # for p in range(2, n + 1):
    #     if c[p]:
    #         prime2.append(p)
    # print(prime2)
    return c
