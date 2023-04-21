# questão: https://olimpiada.ic.unicamp.br/pratique/p2/2017/f1/chefe/
# nota: 20/100

N, M, I = map(int, input().split())
class Funcionario:
    def __init__(self, idade) -> None:
        self.idade = idade
        self.chefes = []
    
    def chefe(self,chefe: object):
        self.chefes.append(chefe)
funcionarios= [Funcionario(i) for i in input().split()]
resposta = []

def min_chefe(chefe):
    idade = [chefe.idade]
    
    if chefe.chefes:
        for i in chefe.chefes:
            idade.append(min_chefe(i))
    return min(idade)

for _ in range(M+I):
    entrada = input().split()
    if "T" in entrada:
        x, y = [int(i) for i in entrada[1:]]
        funcionarios[x-1].idade, funcionarios[y-1].idade = funcionarios[y-1].idade, funcionarios[x-1].idade
        funcionarios[x-1], funcionarios[y-1]= funcionarios[y-1], funcionarios[x-1]
    elif "P" in entrada:
        x = int(entrada[1])
        if funcionarios[x-1].chefes:
            idades = []
            for i in funcionarios[x-1].chefes:
                idades.append(min_chefe(i))
            resposta.append(min(idades))
        else:
            resposta.append("*")
    else:
        x, y = [int(i) for i in entrada]
        funcionarios[y-1].chefe(funcionarios[x-1])

for i in resposta:
    print(i)
        