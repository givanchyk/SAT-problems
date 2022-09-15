with open('input.txt', 'r') as f:
    f_rdl = f.readlines()
n, m = map(int, f_rdl[0].split())
adj_matrix = [[0 for i in range(n)] for j in range(n)]
for i in range(1, m+1):
    x, y = map(lambda x: int(x)-1, f_rdl[i].split())
    adj_matrix[x][y] = 1
    adj_matrix[y][x] = 1
print(adj_matrix)
num_propositions = n + n*n + n*(n-1) / 2
def f(x):
    return x + 1
def g(x, y):
    return n + x*n + y + 1
def h(x, y):
    return n + n*n + x*n-x*(x-1)//2 + y + 1
clauses = []
#1) there's a bijection between 0 and 1 (they're the same size)
for i in range(n):
    new_clause = [g(i, j) for j in range(n)]
    clauses.append(new_clause)
for j in range(n):
    new_clause = [g(i, j) for i in range(n)]
    clauses.append(new_clause)
for i in range(n):
    for j in range(n):
        for k in range(j+1, n):
            new_clause = [-g(i, j), -g(i, k)]
            clauses.append(new_clause)
for i in range(n):
    for j in range(n):
        for k in range(j+1, n):
            new_clause = [-g(j, i), -g(k, i)]
            clauses.append(new_clause)
#2) - create clauses which correspond to edges between clusters
for i in range(n): 
    for j in range(i+1, n):
        clauses.append([-h(i, j), adj_matrix[i][j]])
        clauses.append([-h(i, j), f(i), f(i)])
        clauses.append([h(i, j), int(not adj_matrix[i][j]), f(i), f(i)])
        clauses.append([h(i, j), int(not adj_matrix[i][j]), f(j), f(j)])
m = len(clauses)
with open('output.txt', 'w') as f:
    f.write('p cnf %d %d\n' % (num_propositions, m))
    for i in range(m):
        f.write(' '.join(map(str, clauses[i])) + ' 0\n')
