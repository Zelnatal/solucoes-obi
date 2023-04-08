# questão: https://olimpiada.ic.unicamp.br/pratique/ps/2020/f1/paciente/
# nota: 100/100
n, c = [int(x) for x in input().split()]
linhas = [input() for _ in range(c)]
resposta = []
infectados = []
for linha in linhas:
    lista = linha.split()
    if lista[0] not in infectados:
        resposta.append(int(lista[0]))
    for i in lista[2:]:
        infectados.append(int(i))

resposta = [x for x in sorted(resposta) if x not in infectados]
for i in resposta:
    print(i)
    