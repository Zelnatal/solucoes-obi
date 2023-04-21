# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f2/formiga/
# nota: 100/100
 
S, T, P = [int(i) for i in input().split()]
ALTURAS = [int(i) for i in input().split()]
TUNEIS = [[] for _ in range(S)] 
for _ in range(T):
    i,j = [int(i) for i in input().split()]
    if ALTURAS[i-1] > ALTURAS[j-1]:
        TUNEIS[i-1].append(j)
    elif ALTURAS[i-1] < ALTURAS[j-1]:
        TUNEIS[j-1].append(i)

DISTANCIA_CALCULADA = [-1 for _ in range(S)]

def contar(atual):
    if DISTANCIA_CALCULADA[atual-1] == -1:
        DISTANCIA_CALCULADA [atual-1] = 0
        caminhos = TUNEIS[atual-1]
        for i in caminhos:
            DISTANCIA_CALCULADA[atual-1] = max(contar(i)+1, DISTANCIA_CALCULADA[atual-1])
    return DISTANCIA_CALCULADA[atual-1]

contar(P)
print(max(DISTANCIA_CALCULADA))
            