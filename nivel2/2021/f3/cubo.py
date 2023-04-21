# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2021/f3/cubo/
# nota: 100/100
a = int(input())
b = int(input())
inicial :float = a**(1/6)
if not inicial.is_integer():
    inicial = int(inicial) + 1
final = int(b**(1/6))
print(int(final - inicial) + 1)