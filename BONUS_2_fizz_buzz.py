# Vypis cela cisla od 1 do 100.
# Pokud je cislo delitelne 3 vypis misto neho retezec "Fizz"
# Pokud je cislo delitelne 5 vypis misto neho retezec "Buzz"
# Pokud je cislo delitelne soucasne 3 a 5 vypis misto neho retezec "FizzBuzz"

# Bonus: zeptej se uzivatele horni hranici - cislo do ktereho se ma vypisovat (misto 100 napevno)

for cislo in range (int(input("Zadej cislo: "))):
	if cislo % 15 == 0:
		print("FizzBuzz")
	elif cislo % 3 == 0:
		print("Fizz")
	elif cislo % 5 == 0:
		print("Buzz")
	else:
		print(cislo)
