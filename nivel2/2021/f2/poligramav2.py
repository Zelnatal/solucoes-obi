# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/poligrama/
# nota: 80/100

N = int(input())
PALAVRA = input()
resposta = None

for i in range(1, N//2+1):
    primeira = PALAVRA[:i]
    primeira_sort = sorted(primeira)
    
    for j in range(i, N, i):
        if sorted(PALAVRA[j:i+j]) != primeira_sort:
            break
    else:
        resposta = primeira
        break
    
print(resposta or "*")