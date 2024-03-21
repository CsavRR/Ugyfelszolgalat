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