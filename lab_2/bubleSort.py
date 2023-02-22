def bubbleSort(n):
    swapped = False
    for m in range(len(n) - 1, 0, -1):
        for i in range(m):
            if n[i] > n[i + 1]:
                swapped = True
                n[i], n[i + 1] = n[i + 1], n[i]
        if not swapped:
            return

