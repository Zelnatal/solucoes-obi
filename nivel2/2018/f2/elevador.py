# questões: https://olimpiada.ic.unicamp.br/pratique/p2/2018/f2/elevador/
# nota: 100/100

N = int(input())
pesos = [int(x) for x in input().split()]
pesos.sort()
atual = 0
retorno = "N"
for i in pesos:
    if i - atual > 8:
        break
    atual = i
else:
    retorno = "S"

print(retorno)