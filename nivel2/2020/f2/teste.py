# https://olimpiada.ic.unicamp.br/pratique/p2/2020/f2/formiga/
# este algorimo está no gabarito da prova


def buscar_iterativo(inicio):
    if distancias[inicio] == -1:
        distancias[inicio] = 0

        pilha = [inicio]
        while pilha:
            atual = pilha.pop()
            for vizinho in grafo[atual]:
                if distancias[vizinho] == -1:
                    pilha.append(vizinho)
                    distancias[vizinho] = distancias[atual] + 1

    return max(distancias)


S, T, P = (int(i) for i in input().split())
profundidades = [int(i) for i in input().split()]

grafo = [[] for _ in range(S)]
distancias = [-1 for _ in range(S)]

for _ in range(T):
    j, i = (int(i)-1 for i in input().split())

    if profundidades[i] > profundidades[j]:
        grafo[i].append(j)
    elif profundidades[j] > profundidades[i]:
        grafo[j].append(i)

print(buscar_iterativo(P-1))