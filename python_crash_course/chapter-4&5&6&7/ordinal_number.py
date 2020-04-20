# Updated date: 3/3/2020
# Author: Lee Ding
# Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most
# ordinal numbers end in th, except 1, 2, and 3.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
