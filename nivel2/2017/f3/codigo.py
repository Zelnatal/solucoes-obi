# questões: https://olimpiada.ic.unicamp.br/pratique/p2/2017/f3/codigo/
# nota: -/100

from collections import defaultdict

anteriores ,prefixo, sufixo = defaultdict(bool), defaultdict(bool), defaultdict(bool)
entrada = [input() for _ in range(int(input()))]

resposta = 'ok'
for atual in entrada:
    if anteriores[atual]:
        resposta = atual
        break
    anteriores[atual] = True
    for x in range(1,10):
        pre_atual, suf_atual = atual[0:x], atual[x:10]
        if sufixo[pre_atual] and prefixo[suf_atual]:
            resposta = atual
            break
        sufixo[suf_atual] = True
        prefixo[pre_atual] = True
    if resposta != 'ok':
        break
print(resposta)