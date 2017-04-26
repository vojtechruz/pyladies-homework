# -*- coding: UTF-8 -*-
# Napiš program, který simuluje tuto hru:
# První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka. Potom hází další hráč,
# dokud nepadne šestka i jemu. Potom hází hráč třetí, a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky
# potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)
# Program by měl vypisovat všechny hody, a nakonec napsat, kdo vyhrál.

from random import randrange

def hod():
    hod = randrange(1,7)
    print(hod)
    pocet = 1
    while  hod != 6:
        hod = randrange(1,7)
        print(hod)
        pocet = pocet + 1
    return pocet

print('Prvni hrac:')
pocet_1 = hod()
print('Pocet hodu je', pocet_1)

print('Druhy hrac:')
pocet_2 = hod()
print('Pocet hodu je', pocet_2)

print('Treti hrac:')
pocet_3 = hod()
print('Pocet hodu je', pocet_3)

print('Ctrvrty hrac:')
pocet_4 = hod()
print('Pocet hodu je', pocet_4)

vysledky = []
vysledky = [pocet_1, pocet_2, pocet_3, pocet_4]

pozice_max = vysledky.index(max(vysledky))

print(vysledky)

if pozice_max == 0:
    print('Vyhral prvni hrac.')
elif pozice_max == 1:
    print('Vyhral druhy hrac.')
elif pozice_max == 2:
    print('Vyhral treti hrac.')
else:
    print('Vyhral ctvrty hrac.')
