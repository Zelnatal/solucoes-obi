# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/ralouim/
# nota: -/100
# incompleto

N = int(input())
pontos = [tuple(map(int, input().split())) for _ in range(N)]
pontos.insert(0,(0,0))
distancias = [[0]*(N+1) for _ in range(N+1)]
pares = [[] for _ in range(N+1)]
for i in range(N+1):
    for j in range(i+1,N+1):
        distancia = (pontos[i][0]-pontos[j][0])**2 + (pontos[i][1]-pontos[j][1])**2
        distancias[i][j] = distancias[j][i] = distancia

