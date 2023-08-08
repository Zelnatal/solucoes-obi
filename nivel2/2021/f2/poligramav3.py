# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/poligrama/
# nota: 100/100

N = int(input())
P = input()
saída = "*"

def palavras_divididas():
    div = 1
    while div < N:
        if N % div == 0:
            yield P[0:div], div
        div += 1

for ana,d in palavras_divididas():
    anas = sorted(ana)
    for ps in range(d,N,d):
        if anas != sorted(P[ps:ps+d]):
            break
    else:
        saída = ana
        break
    
print(saída)