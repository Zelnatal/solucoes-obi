# questão: https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/minmax/
# nota 100/100

s,a,b = [int(input()) for _ in range(3)]
lista = list(range(a,b+1))

min_n = 0

for i in lista:
    numero = i
    soma = 0
    while numero: soma,numero = soma + numero % 10, numero // 10
    if soma == s:
        min_n = i
        break

print(min_n)

max_n = 0

for i in lista[::-1]:
    numero = i
    soma = 0
    while numero: soma,numero = soma + numero % 10, numero // 10
    if soma == s:
        max_n = i
        break

print(max_n)
    
