planets = {
	'Меркурий': 57910006,
	'Венера': 108199995,
	'Земля': 149599951,
	'Марс': 227939920,
	'Юпитер': 778330257,
	'Сатурн': 1429400028,
	'Уран': 2870989228,
	'Нептун': 4504299579,
	#Плутон не планета :(
}

print("Average distance to the Sun: ", sum(list(planets.values())) / len(planets))
print("Planets in alphabetical order: ", sorted(list(planets.keys())))
print("Neptune ", planets['Нептун'] / planets['Земля'], " times farther from Sun then Earth")
