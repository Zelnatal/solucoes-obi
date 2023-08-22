# questões: https://olimpiada.ic.unicamp.br/pratique/p2/2017/f3/arranhaceu/
# nota: 100/100

from collections import defaultdict
n, q = map(int, input().split())
la = list(map(int, input().split()))
lq = [list(map(int,input().split())) for _ in range(q)]
ln = defaultdict(int)
for i in range(1,n+1):
    d = la[i-1]
    k = i
    while k <= n:
        ln[k] += d
        k += k & -k



for x in lq:
    
#     # match x:
#     #     case 0, k, p:
#     #         ln[k-1] = p
#     #     case 1, k:
#     #         print(sum(ln[:k]))
    
    if x[0] == 0:
        _, k, p = x
        d =  p - la[k-1]
        la[k-1] = p
        while k <= n:
            ln[k] += d
            k += k & -k
    else:
        _, k = x
        soma = 0
        while k > 0:
            soma += ln[k]
            k -= k & -k
        print(soma)