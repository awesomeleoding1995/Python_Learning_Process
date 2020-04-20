# Updated date: 2/3/2020
# Author: Lee Ding
# Think of your at least five places in the world you'd like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.

places = ['paris', 'melbourne', 'new york', 'beijing', 'sydney']
print(places)

print(sorted(places))

print("Here is the original list: ")
print(places)

print("Here is the reverse list: ")
print(sorted(places, reverse = True))

print("Here is the original list: ")
print(places)

places.reverse()
print(places)
print("Here is the original list: ")
print(places)

places.sort(reverse = True)
print(places)
