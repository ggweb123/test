f = open('rrr.txt', 'r')
sp = []
for i in f:
    sp.append(int(i))
maxi1 = -999999
for i in sp:
    if str(i)[-2:] == '17':
        if i > maxi1:
            maxi1 = i
c = 0
maxi2 = -999999
for i in range(len(sp) - 2):
    k = 0
    if len(str(abs(sp[i]))) == 4:
        k += 1
    if len(str(abs(sp[i + 1]))) == 4:
        k += 1
    if len(str(abs(sp[i + 2]))) == 4:
        k += 1
    if k == 2:
        if sp[i] % 5 == 0 or sp[i + 1] % 5 == 0 or sp[i + 2] % 5 == 0:
            if sp[i] + sp[i + 1] + sp[i + 2] > maxi1:
                c += 1
                if sp[i] + sp[i + 1] + sp[i + 2] > maxi2:
                    maxi2 = sp[i] + sp[i + 1] + sp[i + 2]
print(c, maxi2)