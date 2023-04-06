def sieve_of_eratosthenes_4(n):
    c = [True] * (n + 1)
    c[1] = False
    prime = []
    i = 2
    while i <= n:
        j = 1
        while j < i:
            if i % j == 0 and j != 1:
                c[i] = False
            j += 1
        i += 1
    # for p in range(2, n + 1):
    #     if c[p]:
    #         prime.append(p)
    # print(prime)
    return c

