# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/ralouim/
# nota: 20/100
import math

def calcular_todas_distancias():
    lista_pos = list(ENTRADAS)
    retorno = {}
    for _ in range(N-1):
        i = lista_pos.pop()
        retorno[(i,i)] = INF
        for j in lista_pos:
            distancia = math.dist(i,j)
            retorno[(i,j)] = distancia
            retorno[(j,i)] = distancia
    retorno[(lista_pos[0],lista_pos[0])] = INF
    return retorno

def primeira_distancia():
    distancia_entrada = {entrada: math.dist([0,0],entrada) for entrada in ENTRADAS}
    # for entrada in ENTRADAS:
    #     distancia = math.dist([0,0],entrada)
    #     distancia_entrada[entrada] = distancia


    lista = sorted(distancia_entrada.items(),reverse=True, key=lambda x:x[1])[:2]
    resultado = {maior_distancia(i,j,1) for i,j in lista}
    # for i,j in lista:
    #     resultado.append(maior_distancia(i,j,1))
    return max(resultado)


def maior_distancia(atual, distancia_anterio, contador):
    distancia_entrada = {entrada: DISTANCIAS[(atual,entrada)] for entrada in ENTRADAS if DISTANCIAS[(atual,entrada)] < distancia_anterio}
    # for entrada in ENTRADAS:
    #     distancia = DISTANCIAS.get((atual,entrada),distancia_anterio)
    #     if distancia < distancia_anterio:
    #         distancia_entrada[entrada] = distancia
    if distancia_entrada:
        lista = sorted(distancia_entrada.items(),reverse=True, key=lambda x:x[1])[:2]
        resultado = {maior_distancia(i,j,contador+1) for i,j in lista}
        # for i, j in lista:
        #     resultado.append(maior_distancia(i,j,contador+1))
        return max(resultado)
    return contador


N = int(input())
ENTRADAS = {tuple(map(int,input().split())) for _ in range(N)}
INF = float('inf')
DISTANCIAS = calcular_todas_distancias()
print(primeira_distancia())
