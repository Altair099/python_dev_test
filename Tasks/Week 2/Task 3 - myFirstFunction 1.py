def myFirstFunction(first, second):
    return first + second
    # ну или так
    # return first * second


def mySecondFunction(number):
    return number * number


result = myFirstFunction(2, 2)
if result == 4:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = mySecondFunction(10)
if result == 100:
    print('Правильно :)')
else:
    print('Неправильно :(')