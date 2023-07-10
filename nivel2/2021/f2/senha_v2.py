# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/senha/
# nota: 50/100

from itertools import cycle

n,m,k = map(int,input().split())
n_array = list(input())
m_array = [cycle(sorted(input())) for _ in range(m)]
p =  int(input()) 
for j,i in enumerate(range(m-1,-1,-1)):
    c = max(i*k,1)
    pa = p
    while pa > 0:
        e = next(m_array[j])
        pa -= c
    n_array[n_array.index('#')] = e
print(''.join(n_array))