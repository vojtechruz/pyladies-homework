# Najdi na internetu text své oblíbené písně, zkopíruj si ho do řetězce, a zjisti, kolikrát je v něm použito
# písmeno K

source = input('Zadej zdrojovy text: ')
to_find = input('Zadej hledany retezec: ')
occurrences = source.count(to_find)

print('Retezec "{0}" se v textu nachazi {1} krat'.format(to_find, occurrences))
