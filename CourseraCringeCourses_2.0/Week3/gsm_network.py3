import itertools

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]

clauses = []
colors = range(1, 4)

def varnum(i, k):
    return 3 * (i - 1) + k

def exactly_one_of(literals):
    clauses.append(literals)
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def adjacent(i, j):
    for k in colors:
        clauses.append([-varnum(i, k), -varnum(j, k)])

for i in range(1, n + 1):
    literals = [varnum(i, k) for k in colors]
    exactly_one_of(literals)

for i, j in edges:
    adjacent(i, j)

num_clauses = len(clauses)
num_variables = n * 3

print(num_clauses, num_variables)
for c in clauses:
    c.append(0)
    print(' '.join(map(str, c)))

