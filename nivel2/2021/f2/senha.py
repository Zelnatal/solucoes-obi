# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/senha/
# nota: 50/100

from itertools import cycle

n,m,k = map(int,input().split())
n_array = list(input())
m_array = [cycle(sorted(input()*(k**i))) for i in range(m-1,-1,-1)]
p =  int(input()) 
valores = [None]*m

for _ in range(p):
    for i,a in enumerate(m_array):
        valores[i] = next(a)
        
for i in valores:
    n_array[n_array.index('#')] = i
    
print(''.join(n_array))
        
