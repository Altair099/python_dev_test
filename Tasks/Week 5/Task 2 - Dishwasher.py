def dishwasher(dirty_plates, remaining_cleanser):
    for _ in range(dirty_plates):
        if remaining_cleanser >= 0.5:
            dirty_plates -= 1
            remaining_cleanser -= 0.5
        else:
            return (f"Моющее средство закончилось. Осталось {dirty_plates} тарелок")
    if remaining_cleanser > 0:
        return (f"Все тарелки вымыты. Осталось {round(remaining_cleanser,2)} ед. моющего средства")
    else:
        return ("Все тарелки вымыты, моющее средство закончилось")



print("Please enter number of plates")
plates = int(input())
print("Please enter amount of cleanser")
cleanser = float(input())
print(dishwasher(plates, cleanser))
