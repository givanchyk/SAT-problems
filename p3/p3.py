with open('input.txt', 'r') as f:
    f_rdl = f.readlines()
n, m, k = map(int, f_rdl[0].split()[2:])
clauses = [list(map(int, f_rdl[i].split()[:-1])) for i in range(1, m+1)]
def x(i):
    return i+1
def r(i, j):
    return n + j*n + i + 1
for i in range(n-1):
    clauses.append([-x(i), r(i, 0)])
for j in range(1, k):
    clauses.append([-r(0, j)])
for i in range(1, n-1):
    for j in range(k):
        clauses.append([-r(i-1, j), r(i, j)])
for i in range(1, n-1):
    for j in range(1, k):
        clauses.append([-x(i), -r(i-1, j-1), r(i, j)])
for i in range(n):
    clauses.append([-x(i), r(i-1, k-1)])
n += n*k
m = len(clauses)
with open('output.txt', 'w') as f:
    f.write('p cnf %d %d\n' % (n, m))
    for i in range(m):
        f.write(' '.join(map(str, clauses[i])) + ' 0\n')
