# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/senha/
# nota: 30/100
n,m,k = map(int,input().split())
n_array = list(input())
m_array = [list(sorted(input())) for _ in range(m)]
p = int(input()) 
ma = 0
while p > 0:
    if k < p:
        n_array[n_array.index('#')] = m_array[ma][-1]
    else:
        n_array[n_array.index('#')] = m_array[ma][p-1]
    ma += 1
    p -= k
for i in range(ma,m):
    n_array[n_array.index('#')] = m_array[i][0]

print(''.join(n_array))
        
