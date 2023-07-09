# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/ralouim/
# nota: 90/100

N = int(input())
pontos = [tuple(map(int, input().split())) for _ in range(N)]
pontos.insert(0,(0,0))
distancias = []
for i in range(N+1):
    for j in range(i+1,N+1):
        distancias.append(((pontos[i][0]-pontos[j][0])**2 + (pontos[i][1]-pontos[j][1])**2,i,j))
distancias.sort()
pontos = [[0,0,0] for _ in range(N+1)]
for d,i,j in distancias:
    if d != pontos[i][0]:
        pontos[i][0] = d
        pontos[i][1] = pontos[i][2]
    if d != pontos[j][0]:
        pontos[j][0] = d
        pontos[j][1] = pontos[j][2]
    if i == 0:
        pontos[i][2] = max(pontos[i][2],pontos[j][1]+1)
    else:
        pontos[i][2] = max(pontos[i][2],pontos[j][1] +1)
        pontos[j][2] = max(pontos[j][2],pontos[i][1] +1)
        
print(pontos[0][2])



