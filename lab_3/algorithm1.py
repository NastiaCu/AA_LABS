def sieve_of_eratosthenes_1(n):
    c = [True] * (n + 1)
    c[1] = False
    prime = []
    i = 2
    while i <= n:
        if c[i]:
            j = 2 * i
            while j <= n:
                c[j] = False
                j += i
        i += 1
    # for p in range(2, n + 1):
    #     if c[p]:
    #         prime.append(p)
    # print(prime)
    return c
