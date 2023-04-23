# questão: https://olimpiada.ic.unicamp.br/pratique/p1/2017/f1/cofre/
# nota: 40/100

from collections import Counter

N, M = map(int, input().split())
COMB = [int(x) for x in input().split()]
POS = [int(x)-1 for x in input().split()]
temp = [COMB[0]]
atual = 0
for i in POS[1:]:
    temp.extend(COMB[atual+1:i+1] if i > atual else COMB[i:atual])
    atual = i
quat = Counter(temp)
resposta = [quat.get(x,0) for x in range(10)]
print(*resposta)    
