# questão: https://olimpiada.ic.unicamp.br/pratique/p1/2017/f1/cofre/
# nota: --/100
# incompleto
N, M = map(int, input().split())
comb = [int(x) for x in input().split()]
pos = [int(x)-1 for x in input().split()]

atual = pos[0]
for proximo in pos[1:]:
    if proximo > atual:
        direita = proximo
        esquerda = atual
    else:
        direita = atual
        esquerda = proximo
    
    
    

