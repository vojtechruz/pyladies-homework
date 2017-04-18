# -*- coding: UTF-8 -*-
# Vypis vsechna cela cisla od 1 do 1000, ktera obsahuji cislici 7.

for i in range(1001):
    cislo = str(i)
    if '7' in cislo:
        print(i)
