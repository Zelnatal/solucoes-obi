# questão: https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/lista/
# nota: 70/100

N = int(input())
L = list(map(int,input().split()))

direita = 0
esquerda = N-1
contado = 0

while direita < esquerda:
    if L[direita] == L[esquerda]:
        direita += 1
        esquerda -= 1
    elif L[direita] < L[esquerda]:
        temp = L.pop(direita+1)
        esquerda -= 1
        L[direita] += temp
        contado += 1
    else:
        temp = L.pop(esquerda-1)
        esquerda -= 1
        L[esquerda] += temp
        contado += 1

print(contado)