def sieve_of_eratosthenes_3(n):
    c = [True] * (n + 1)
    c[1] = False
    prime = []
    i = 2
    while i <= n:
        if c[i]:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1
    # for p in range(2, n + 1):
    #     if c[p]:
    #         prime.append(p)
    # print(prime)
    return c
