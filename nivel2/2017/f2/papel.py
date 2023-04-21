# questões: https://olimpiada.ic.unicamp.br/pratique/p2/2017/f2/papel/
# não funciona
N = int(input())
ALTURAS = [int(i) for i in input().split()]

contado = 2
for i in range(1,N-1):
    if ALTURAS[i-1] > ALTURAS[i] < ALTURAS[i+1]:
        contado += 1

print(contado)