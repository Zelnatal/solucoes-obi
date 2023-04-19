# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/poligrama/
# nota: -/100
# Não funciona


from collections import Counter

n = int(input())
palavra = input()
mid = n // 2
segunda_parte = palavra[mid:]
segunda_quantidade = dict(Counter(segunda_parte))

resultado = ""
while len(resultado) != 1 and mid >= 1:
    encontrou = palavra[:mid]

    while encontrou:
        primeira_quantidade = dict(Counter(encontrou))
        if set(primeira_quantidade.keys()) <= set((segunda_quantidade.keys())):
            for key in primeira_quantidade:
                if primeira_quantidade[key] > segunda_quantidade[key]:
                    break
            else:
                break
        encontrou.pop(0)
    if encontrou:
            resultado = encontrou if len(encontrou) > len(resultado) else resultado
    mid -= 1

if (len(set(resultado)) == 1):
    print(resultado[0])
else:
    print(resultado or "*")
    