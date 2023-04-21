# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f2/formiga/
# nota: 40/100

S, T, P = [int(i) for i in input().split()]
ALTURAS = [int(i) for i in input().split()]
tuneis = [[] for _ in range(S)] 
for _ in range(T):
    i,j = [int(i) for i in input().split()]
    if ALTURAS[i-1] > ALTURAS[j-1]:
        tuneis[i-1].append(j)
    elif ALTURAS[i-1] < ALTURAS[j-1]:
        tuneis[j-1].append(i)

maximo = [0]
pilha = [(0,tuneis[P-1].copy())]

while pilha:
    contador, proximo = pilha[-1]
    if proximo:
        proximo = proximo.pop()
        pilha.append((contador+1,tuneis[proximo-1].copy()))
    else:
        pilha.pop()
        maximo.append(contador)

print(max(maximo))