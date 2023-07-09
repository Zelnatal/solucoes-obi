# questão: https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/passatempo/
# notas: 100/100

l,c = map(int,input().split())
result_l = []
matriz_h = []
matriz_v = [['']*l for _ in range(c)]
dicionario = {}
for i in range(l):
    *linha,r = input().split()
    matriz_h.append(linha)
    result_l.append(int(r))
    for j,v in enumerate(linha):
        dicionario[v] = None
        matriz_v[j][i] = v

result_c = list(map(int,input().split()))

falta = list(dicionario.keys())

def encontrou(n,v):
    falta.remove(n)
    dicionario[n] = v
    for i,m in enumerate(matriz_h):
        if n in m:
            c = m.count(n)
            result_l[i] -= c*v
            for _ in range(c):
                m[m.index(n)] = None
            matriz_h[i] = m
    for i,m in enumerate(matriz_v):
        if n in m:
            c = m.count(n)
            result_c[i] -= c*v
            for _ in range(c):
                m[m.index(n)] = None
            matriz_v[i] = m
    

while falta:
    for p,i in enumerate(matriz_h):
        liset = list(filter(None,i))
        if len(set(liset)) ==1:
            encontrou(liset[0],result_l[p]/len(liset))
    for p,i in enumerate(matriz_v):
        liset = list(filter(None,i))
        if len(set(liset)) ==1:
            encontrou(liset[0],result_c[p]/len(liset))
    
for i in sorted(list(dicionario.keys())):
    print(i,int(dicionario[i]))
