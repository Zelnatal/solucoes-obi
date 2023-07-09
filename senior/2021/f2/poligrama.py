# questão: https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/poligrama/
# notas: 40/100

n = int(input())
p = input()

res=['*']

def div(n):
    for i in range(n-1,0,-1):
        if n % i ==0:
            yield i

for t in div(n):
    sub = []
    for i in range(0,n,t):
        sub.append(frozenset(p[i:i+t])) 
    if all(x == sub[0] for x in sub[1:]):
        res.append(p[0:t])
    
print(res[-1]) 