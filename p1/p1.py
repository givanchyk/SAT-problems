with open('input.txt', 'r') as f:
    f_rdl = f.readlines()
n, m = map(int, f_rdl[0].split()[2:])
clauses = [list(map(int, f_rdl[i].split()[:-1])) for i in range(1, m+1)]
m += 1 
clauses.append([i+1 for i in range(n)])
with open('output.txt', 'w') as f:
    f.write('p cnf %d %d\n' % (n, m))
    for i in range(m):
        f.write(' '.join(map(str, clauses[i])) + ' 0\n')
    