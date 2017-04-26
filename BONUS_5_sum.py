# -*- coding: UTF-8 -*-
# Ptej se uzivatele na cisla, dokud nenapise 'konec'. Potom spocitej sumu (soucet) vsech zadanych cisel.
odpoved = input('Zadej cislo nebo konec: ')
soucet = 0

while odpoved != 'konec':
    cislo = int(odpoved)
    soucet = soucet + cislo
    odpoved = input('Zadej cislo nebo konec: ')

print('Soucet cisel je', soucet)
