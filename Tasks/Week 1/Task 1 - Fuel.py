fuel_consumption_for_100_kilometers = 6.2
fuel_left = 0.54
fuel_tank_liters = 40

kilometers_can_drive = 0
# Не знаю, зачем мы создаём эту переменную, возможно мы именно её должны были в конце принтить, а не kilometers_left, но что-то пошло не так при составлении задания)

kilometers_left = (fuel_tank_liters * fuel_left) / (fuel_consumption_for_100_kilometers / 100)
print(kilometers_left)