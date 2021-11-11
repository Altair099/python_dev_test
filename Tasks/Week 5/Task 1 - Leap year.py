def is_leap_year(year):
    if year % 4 != 0:
        return "no"
    if year % 100 == 0:
        if year % 400 != 0:
            return "no"
    return "yes"




print("Please enter year")
year = int(input())
print(is_leap_year(year))
