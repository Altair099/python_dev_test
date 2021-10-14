def myFirstFunction(a=2, b=2):
    return a + b


def mySecondFunction(value=10):
    return value * value


result = myFirstFunction()
if result == 4:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = myFirstFunction(a=3)
if result == 5:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = myFirstFunction(b=1)
if result == 3:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = mySecondFunction()
if result == 100:
    print('Правильно :)')
else:
    print('Неправильно :(')

result = mySecondFunction(value=20)
if result == 400:
    print('Правильно :)')
else:
    print('Неправильно :(')