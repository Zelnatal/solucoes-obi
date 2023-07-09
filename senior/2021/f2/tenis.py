# questão: https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/tenis/
# nota : 100/100
lista = [int(input()) for _ in range(4)]
lista.sort()
print(abs((lista[0]+lista[3])-(lista[1]+lista[2])))
