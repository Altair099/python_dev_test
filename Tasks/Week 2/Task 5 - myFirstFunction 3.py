def myFirstFunction(*numbers):
    return sum(numbers)


def mySecondFunction(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


result = myFirstFunction(2)
if result == 2:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = myFirstFunction(2, 4)
if result == 6:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = myFirstFunction(5, 10, 15)
if result == 30:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = mySecondFunction(5)
if result == 5:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = mySecondFunction(5, 5)
if result == 25:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = mySecondFunction(10, 9, 2)
if result == 180:
    print('Правильно :)')
else:
    print('Неправильно :(')