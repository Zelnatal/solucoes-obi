# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/ralouim/
# 10/100
def calcular_distancia(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def primeira_distancia():
    distancia_entrada = {}
    entradas = ENTRADAS.copy()
    for entrada in entradas:
        distancia = calcular_distancia(0, 0, *entrada)
        distancia_entrada[entrada] = distancia

    resultado =[]
    for i,j in distancia_entrada.items():
        resultado.append(maior_distancia(i,(0,0),j,1))
    return max(resultado)


def maior_distancia(atual, anterio, distancia_anterio, contador):
    distancia_entrada = {}
    entradas = ENTRADAS.copy()
    entradas.remove(atual)
    if anterio in entradas:
        entradas.remove(anterio)

    for entrada in entradas:
        distancia = calcular_distancia(*atual, *entrada)
        if distancia < distancia_anterio:
            distancia_entrada[entrada] = distancia

    if distancia_entrada:
        resultado =[]
        for i, j in distancia_entrada.items():
            resultado.append(maior_distancia(i,atual,j,contador+1))
        return max(resultado)
    return contador


n = int(input())
ENTRADAS = [input().split() for _ in range(n)]
ENTRADAS = [(int(x),int(y)) for x,y in ENTRADAS]
print(primeira_distancia())
