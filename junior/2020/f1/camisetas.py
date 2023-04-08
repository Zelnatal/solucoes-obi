# questão: https://olimpiada.ic.unicamp.br/pratique/pj/2020/f1/camisetas/
# nota: 100/100
n = int(input())
lista_n = [int(i) for i in input().split()]
p = int(input())
m = int(input())
print("S" if lista_n.count(1) >= p and lista_n.count(2) >= m else "N")
