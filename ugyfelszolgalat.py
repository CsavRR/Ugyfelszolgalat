def mpbe(o, p, m):
    return o * 60 * 60 + p * 60 + m

hivas = []
f = open('hivas.txt', 'rt')

for sor in f:
    sor = sor.strip().split(' ')
    sor = list(map(int, sor))
    sor.append(mpbe(sor[0], sor[1], sor[2]))
    sor.append(mpbe(sor[3], sor[4], sor[5]))
    hivas.append(sor)

print('3. feladat')
orak = {}

for ora in hivas:
    if ora[0] not in orak.keys():
        orak[ora[0]] = 0
    orak[ora[0]] += 1

for k, v in orak.items():
    print(f'{k} ora {v} hivas')

print('4. feladat')
maxH = 0
maxHSor = 0
hSor = 1

for hiv in hivas:
    hivH = mpbe(hiv[3], hiv[4], hiv[5]) - mpbe(hiv[0], hiv[1], hiv[2])
    if maxH < hivH:
        maxH = hivH
        maxHSor = hSor
    hSor += 1

print(f'A leghosszabb ideig vonalban levo hivo {maxHSor}. sorban szerepel, a hivas hossza: {maxH} masodperc.')

print('5. feladat')

ido = input('Adjon meg egy idopontot! (ora perc masodperc) ')
ido = list(map(int, ido.strip().split(' ')))
idoM = mpbe(ido[0], ido[1], ido[2])

i = 0

while i < len(hivas) and not(mpbe(hivas[i][0], hivas[i][1], hivas[i][2]) <= idoM and idoM < mpbe(hivas[i][3], hivas[i][4], hivas[i][5])):
    i += 1

if i < len(hivas):
    telefonalo = i + 1
else:
    telefonalo = -1

if telefonalo:
    varakozokSz = 0
    for hiv in hivas:
        if mpbe(hiv[0], hiv[1], hiv[2]) <= idoM and idoM < mpbe(hiv[3], hiv[4], hiv[5]):
            varakozokSz += 1
    print(f'A varakozok szama: {varakozokSz} a beszelo a {telefonalo}. hivo.')
else:
    print('Nem volt beszelo.')

print('6. feladat')

utsoH = 0
utsoE = 0
muszakV = mpbe(12, 0, 0)
i = 0

for hiv in hivas:
    kezdet = mpbe(hiv[0], hiv[1], hiv[2])
    veg = mpbe(hiv[3], hiv[4], hiv[5])
    if kezdet <= muszakV and veg > mpbe(hivas[utsoH][3], hivas[utsoH][4], hivas[utsoH][5]):
        utsoE = utsoH
        utsoH = i
    i += 1

utsoEveg = mpbe(hivas[utsoE][3], hivas[utsoE][4], hivas[utsoE][5])
utsoHkezd = mpbe(hivas[utsoH][0], hivas[utsoH][1], hivas[utsoH][2])
varakozas = utsoEveg - utsoHkezd

if varakozas < 0:
    varakozas = 0

print(f'Az utolso telefonalo adatai a(z) {utsoH + 1}. sorban vannak, {varakozas} masodpercig vart')

kapcsolt = []
elotte = 0
muszakK = mpbe(8, 0, 0)
i = 0

for hiv in hivas:
    if muszakK < hiv[7] and hivas[elotte][7] < hiv[7]  and hiv[6] <= muszakV:
        kapcsolt.append(i)
        elotte = i
    i += 1

s = open('sikeres.txt', 'wt')

if hivas[kapcsolt[0]][6] < muszakK:
    kezd = '08 00 00'
else:
    kezd = str(hivas[kapcsolt[i]][0]) + ' ' + str(hivas[kapcsolt[i]][1]) + ' ' + str(hivas[kapcsolt[i]][2])

vege = str(hivas[kapcsolt[0]][3]) + ' ' + str(hivas[kapcsolt[0]][4]) + ' ' + str(hivas[kapcsolt[0]][5])

s.write(f'{kapcsolt[0] + 1} {kezd} {vege}')

for i in range(1, len(kapcsolt) - 1):
    if hivas[kapcsolt[i - 1]][7] < hivas[kapcsolt[i]][6]:
        kezd = str(hivas[kapcsolt[i]][0]) + ' ' + str(hivas[kapcsolt[i]][1]) + ' ' + str(hivas[kapcsolt[i]][2])
else:
    kezd = str(hivas[kapcsolt[i - 1]][3]) + ' ' + str(hivas[kapcsolt[i - 1]][4]) + ' ' + str(hivas[kapcsolt[i - 1]][5])

vege = str(hivas[kapcsolt[i]][3]) + ' ' + str(hivas[kapcsolt[i]][4]) + ' ' + str(hivas[kapcsolt[i]][5])

s.write(f'{kapcsolt[i] + 1} {kezd} {vege}')

f.close()
s.close()