public_key = 3403
prime_numbers = []
number = 100

while number > 1:
    is_prime = True
    division_number = number - 1
    while division_number > 1 and is_prime:
        if number % division_number != 0:
            division_number -= 1
            continue
        is_prime = False
    if is_prime:
        prime_numbers.append(number)
    number -= 1

for prime_number in prime_numbers:
    if public_key % prime_number == 0:
        print(f"Combination numbers: {prime_number} and {int(public_key / prime_number)}")
        break
