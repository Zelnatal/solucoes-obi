# questão: https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/tempo/
# nota: 100/100
class Tempo:
    valor = -1

    def __init__(self, inicial, ultimo):
        self.inicial = inicial
        self.ultimo = ultimo

    def calcular(self, final):
        self.valor = final - self.inicial + self.ultimo


n = int(input())
args = [input() for _ in range(n)]
pos = {}
i = 0
for arg in args:
    """
    match arg.split():
        case ["R", numero]:
            numero_int = int(numero)
            pos[numero_int] = Tempo(
                i, pos[numero_int].valor if numero_int in pos else 0
            )
            i += 1
        case ["E", numero]:
            numero_int = int(numero)
            pos[numero_int].calcular(i)
            i += 1
        case ["T", numero]:
            numero_int = int(numero)
            i += numero_int - 1
    """

    letra, numero = arg.split()
    if letra == "R":
        numero_int = int(numero)
        pos[numero_int] = Tempo(i, pos[numero_int].valor if numero_int in pos else 0)
        i += 1
    elif letra == "E":
        numero_int = int(numero)
        pos[numero_int].calcular(i)
        i += 1
    elif letra == "T":
        numero_int = int(numero)
        i += numero_int - 1

for i in sorted(pos):
    print(i, pos[i].valor)
