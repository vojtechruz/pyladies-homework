# Vypis cela cisla od 1 do 100.
# Pokud je cislo delitelne 3 vypis misto neho retezec "Fizz"
# Pokud je cislo delitelne 5 vypis misto neho retezec "Buzz"
# Pokud je cislo delitelne soucasne 3 a 5 vypis misto neho retezec "FizzBuzz"

# Bonus: zeptej se uzivatele horni hranici - cislo do ktereho se ma vypisovat (misto 100 napevno)
hranice = int(input('Zadej horni hranici: '))
for i in range(hranice + 1):
    zbytek3 = i % 3
    zbytek5 = i % 5

    if zbytek3 == 0 and zbytek5 == 0:
        print('FizzBuzz')
    elif zbytek3 == 0:
        print('Fizz')
    elif zbytek5 == 0:
        print('Buzz')
    else:
        print(i)
