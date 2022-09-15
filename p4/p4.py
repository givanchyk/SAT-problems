with open('input1.txt', 'r') as f1:
    f1_rdl = f1.readlines()
with open('input2.txt', 'r') as f2:
    f2_rdl = f2.readlines()
n1, m1 = map(int, f1_rdl[0].split())
n2, m2 = map(int, f2_rdl[0].split())
adj_matrix1 = [[0 for i in range(n1)] for j in range(n1)]
adj_matrix2 = [[0 for i in range(n2)] for j in range(n2)]
for i in range(1, m1+1):
    x, y = map(lambda x: int(x)-1, f1_rdl[i].split())
    adj_matrix1[x][y] = 1
    adj_matrix1[y][x] = 1
for i in range(1, m2+1):
    x, y = map(lambda x: int(x)-1, f2_rdl[i].split())
    adj_matrix2[x][y] = 1
    adj_matrix2[y][x] = 1 
print(adj_matrix1)
print(adj_matrix2)

num_propositions = n2*n1 

# Each proposition is of kind "Is vertex i in G2 mapped to vertex j in G1?"
# First n1 propositions correspond to mappings 1-->i for every i in G1
def f(i, j):
    return i*n1 + j + 1 #mapping (i, G2) to (j, G1) is a clause number i*n1+j+1
clauses = []
for i in range(n2):
    new_clause = [f(i, j) for j in range(n1)] # "For each vertex in G2, it must be mapped to some vertex in G1"
    clauses.append(new_clause)
for i in range(n2):
    for j1 in range(n1):
        for j2 in range(j1+1, n1):
            new_clause = [-f(i, j1), -f(i, j2)] # "For each vertex in G2, it must not be mapped to two verteces at once"
            clauses.append(new_clause)
for j in range(n1):
    for i1 in range(n2):
        for i2 in range(i1+1, n2):
            new_clause = [-f(i1, j), -f(i2, j)] # "For each vertex in G1, it must not be mapped to two verteces at once"
            clauses.append(new_clause)
for i1 in range(n2):
    for i2 in range(i1+1, n2):
        for j1 in range(n2):
            for j2 in range(j1+1, n2):
                # "If i1 is mapped to j1 and i2 mapped to j2, or i1 is mapped to j2 and i2 mapped to j1,
                # then edges G2[i1][i2] and G1[j1][j2] must be equivalent
                new_clause = [-f(i1, j1), -f(i2, j2), int(adj_matrix1[i1][i2]==adj_matrix1[j1][j2])]
                clauses.append(new_clause)
                new_clause = [-f(i1, j2), -f(i2, j1), int(adj_matrix1[i1][i2]==adj_matrix1[j1][j2])]
                clauses.append(new_clause)
                # Either one of f(i1, j1) or f(i2, j2) is false, or entries in adj_m are equal, same for (i1, j2) and (i2, j1)
n = num_propositions
m = len(clauses)
with open('output.txt', 'w') as f:
    f.write('p cnf %d %d\n' % (n, m))
    for i in range(m):
        f.write(' '.join(map(str, clauses[i])) + ' 0\n')