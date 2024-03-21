def mbpe(o, p, m):
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
    hivH = mbpe(hiv[3], hiv[4], hiv[5]) - mbpe(hiv[0], hiv[1], hiv[2])
    if maxH < hivH:
        maxH = hivH
        maxHSor = hSor
    hSor += 1

print(f'A leghosszabb ideig vonalban levo hivo {maxHSor}. sorban szerepel, a hivas hossza: {maxH} masodperc.')