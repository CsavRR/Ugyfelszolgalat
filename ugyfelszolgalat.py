def mpbe(o, p, m):
    return o * 60 * 60 + p * 60 + m

hivas = []
f = open('hivas.txt', 'rt')

for sor in f:
    sor = sor.strip().split(' ')
    sor = list(map(int, sor))
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