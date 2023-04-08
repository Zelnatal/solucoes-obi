# questão: https://olimpiada.ic.unicamp.br/pratique/p1/2020/f1/3por2/
# nota: 100/100
n = int(input())
lista = [int(input()) for _ in range(n)]
lista.sort(reverse=True)
for i in range(2,n,3):
    lista[i] = 0
print(sum(lista))
