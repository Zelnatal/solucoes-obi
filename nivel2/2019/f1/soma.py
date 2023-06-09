# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/soma/
# nota: 25/100
from array import array
N, K = map(int, input().split())
prefix=array('i',[0])
for i in map(int, input().split()):
    prefix.append(prefix[-1] + i)
    
count = 0
for i in range(N+1):
    for j in range(i+1,N+1):
        sub = prefix[j] - prefix[i]
        if sub > K:
            break
        if sub == K:
            count += 1

print(count)
