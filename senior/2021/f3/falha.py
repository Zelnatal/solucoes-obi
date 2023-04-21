# questões: https://olimpiada.ic.unicamp.br/pratique/ps/2021/f3/falha/
# notas: 70/100
N = int(input())
entradas = [input() for _ in range(N)]
contado = 0
for i in range(N):
    elemento = entradas.pop(i)
    for j in entradas:
        if elemento in j:
            contado += 1
    entradas.insert(i,elemento)
    
print(contado)
