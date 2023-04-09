# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/ralouim/
# nota: 10/100
import math

def calcular_todas_distancias():
    lista_pos = ENTRADAS
    lista_pos.append((0,0))
    retorno = []
    retorno2 = {}
    retorno3 = {}
    retorno4 = {}
    for _ in range(N):
        i = lista_pos.pop(0)
        retorno2[i] = []
        retorno3[i] = []
        retorno4[i] = 0
        for j in lista_pos:
            # (i[0]-j[0])**2+(i[1]-j[1])**2
            retorno.append([math.dist(i,j),i,j])
    retorno.sort(reverse=True)
    return retorno, retorno2, retorno3, retorno4

N = int(input())
ENTRADAS = [tuple(map(int,input().split())) for _ in range(N)]
DISTANCIAS, contador, distancia, quantidade = calcular_todas_distancias()
resultado = [1]
for percurso in DISTANCIAS:
    distancia_atual = percurso[0]
    local1 = percurso[1]
    local2 = percurso[2]
    if local1 == (0,0):
        contador[local2].append(1)
        distancia[local2].append(distancia_atual)
        quantidade[local2] += 1
    elif local2 == (0,0):
        contador[local1].append(1)
        distancia[local1].append(distancia_atual)
        quantidade[local1] += 1
    else:
            for index in range(quantidade[local1]):
                if distancia_atual != distancia[local1][index]:
                    c = contador[local1][index]+1
                    contador[local2].append(c)
                    resultado.append(c)
                    distancia[local2].append(distancia_atual)
                    quantidade[local2] += 1

            for index in range(quantidade[local2]):
                if distancia_atual != distancia[local2][index]:
                    c = contador[local2][index]+1
                    contador[local1].append(c)
                    resultado.append(c)
                    distancia[local1].append(distancia_atual)
                    quantidade[local1] += 1
print(max(resultado))
