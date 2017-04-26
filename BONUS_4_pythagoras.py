# -*- coding: UTF-8 -*-
# Napis funkci, ktera ti pro dve zadane delky odvesen pravouhleho trojuhelnika vypocita delku prepony. (TIP budes potrebovat Pythagorovu vetu)
from math import sqrt

a = int(input('Zadej delku prvni odvesny: '))
b = int(input('Zadej delku druhe odvesny: '))

c = sqrt(a**2 + b**2)

print('Delka prepony je %.2f.' %c)
