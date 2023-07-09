# questão: https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/lista/
# nota: 70/100

n = int(input())
a = [int(x) for x in input().split()]
r, l = 0, n-1
c = 0
while r < l:
    if a[r] < a[l]:
        v = a.pop(r+1)
        c += 1
        l -= 1
        a[r] += v
    elif a[r] > a[l]:
        v = a.pop(l-1)
        c += 1
        l -= 1
        a[l] += v
    else:
        r += 1
        l -= 1 
print(c)