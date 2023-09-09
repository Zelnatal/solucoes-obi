# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2017/f3/imperio/
# nota: 100/100

from functools import cache
from collections import defaultdict
import sys

sys.setrecursionlimit(((2**32)//2)-1)


n = int(input())


liga = defaultdict(list)
ligas = []
for _ in range(n-1):
    a,b = map(int,input().split())
    liga[a].append(b)
    liga[b].append(a)
    ligas.append((a,b))

@cache
def dfs(indo,anterior):
    res = 1
    for proximo in liga[indo]:
        if proximo != anterior:
            res += dfs(proximo,indo)
    return res

mini = float('inf')

for a,b in ligas:
    mini = min(mini,abs(dfs(a,b) - dfs(b,a)))

print(mini)
