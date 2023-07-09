# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/sanduiche/
# nota: 70/100

from itertools import combinations

encontrado = {}

def fatorial(n):
    if n in encontrado:
        return encontrado[n]
    if n <2:
        return 1
    c = n * fatorial(n-1)
    encontrado[n] = c
    return c
    
n,m = map(int,input().split())
numbers = list(range(1,n+1))
quant = n
ncomb = []

for _ in range(m): 
    ncomb.append(list(map(int,input().split())))

def combinacao(p):
    return fatorial(n)//(fatorial(p)*fatorial(n-p))

if m == 0:
    quant += 1
    for i in range(2,n):
        quant += combinacao(i)
    print(quant)
else:
    quant += combinacao(2) - m
    for i in range(3,n):
        combs = combinations(numbers,i)
        for comb in combs:
            for p,s in ncomb:
                if p in comb and s in comb:
                    break
            else:
                quant += 1
    print(quant)
