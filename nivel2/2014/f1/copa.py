# questões: https://olimpiada.ic.unicamp.br/pratique/p2/2014/f1/copa/
# nota: 100/100

from itertools import repeat

n, f, r = map(int,input().split())

par = list(range(n+1))
rank = list(repeat(1,n+1))

def find(n1):
    while n1 != par[n1]:
        par[n1] = par[par[n1]]
        n1 = par[n1]
    return n1

def union(n1,n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        return False
    if rank[p1] > rank[p2]:
        p1, p2 = p2, p1
    rank[p2] += rank[p1]
    par[p1] = p2
    return True

reforma = []
for _ in range(f):
    reforma.append(tuple(tuple(list(map(int,input().split()))+[0])))
    
for _ in range(r):
    reforma.append(tuple(tuple(list(map(int,input().split()))+[1])))
    
reforma.sort(key=lambda x: (x[3],x[2]))
c_total = 0
for (a,b,c,_) in reforma:
    if union(a,b):
        c_total += c

print(c_total)