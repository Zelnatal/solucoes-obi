# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/ralouim/
# nota: 20/100
import math

def calcular_todas_distancias():
    lista_pos = ENTRADAS
    lista_pos.append((0,0))
    retorno = []
    for _ in range(N):
        i = lista_pos.pop()
        for j in lista_pos:
            # (i[0]-j[0])**2+(i[1]-j[1])**2
            retorno.append([math.dist(i,j),i,j])
    retorno.sort(reverse=True)
    return retorno

N = int(input())
ENTRADAS = [tuple(map(int,input().split())) for _ in range(N)]
DISTANCIAS = calcular_todas_distancias()
contador = []
anterio = []
distancia = []
for percurso in DISTANCIAS:
    distancia_atual = percurso[0]
    local1 = percurso[1]
    local2 = percurso[2]
    if local1 == (0,0):
        contador.append(1)
        distancia.append(distancia_atual)
        anterio.append(local2)
    elif local2 == (0,0):
        contador.append(1)
        distancia.append(distancia_atual)
        anterio.append(local1)
    else:
        utilizar = anterio[-N*10:]
        if local1 in utilizar:
            quat = utilizar.count(local1)
            indexes = []
            index=-N*10-1
            for _ in range(quat):
                index = anterio.index(local1,index+1)
                indexes.append(index)
            #indexes = [x for x,y in enumerate(anterio) if y == local1]
            for index in indexes:
                if distancia_atual != distancia[index]:
                    contador.append(contador[index]+1)
                    distancia.append(distancia_atual)
                    anterio.append(local2)

        if local2 in utilizar:
            quat = utilizar.count(local2)
            indexes = []
            index=-N*10-1
            for _ in range(quat):
                index = anterio.index(local2,index+1)
                indexes.append(index)
            #indexes = [x for x,y in enumerate(anterio) if y == local2]
            for index in indexes:
               if distancia_atual != distancia[index]:
                    contador.append(contador[index]+1)
                    distancia.append(distancia_atual)
                    anterio.append(local1)
print(max(contador))