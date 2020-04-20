# Upadated date: 6/11/2019
# Author: Lee Ding
# If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you'd like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.

guest_invited = ['Gerard', 'William', 'Lee', 'Lesley']

# print('Hi ' + guest_invited[0] + '! We are gonna have a dinner in Saturday night, would you like to join us?')
# print('Hi ' + guest_invited[1] + '! We are gonna have a dinner in Saturday night, would you like to join us?')
# print('Hi ' + guest_invited[2] + '! We are gonna have a dinner in Saturday night, would you like to join us?')
# print('Hi ' + guest_invited[3] + '! We are gonna have a dinner in Saturday night, would you like to join us?')

# print('We are sorry that ' + guest_invited[3] + ' can not make it here.' )
# del guest_invited[3]
# guest_invited.insert(3, 'Spongebob')
# print('But we are happy that ' + guest_invited[3] + ' can come to our dinner!')

guest_invited.insert(0, 'James')
guest_invited.insert(3, 'Julie')
guest_invited.append('Matt')

print('Hi ' + guest_invited[0] + '! We are gonna have a dinner in Saturday night, would you like to join us?')
print('Hi ' + guest_invited[1] + '! We are gonna have a dinner in Saturday night, would you like to join us?')
print('Hi ' + guest_invited[2] + '! We are gonna have a dinner in Saturday night, would you like to join us?')
print('Hi ' + guest_invited[3] + '! We are gonna have a dinner in Saturday night, would you like to join us?')
print('Hi ' + guest_invited[4] + '! We are gonna have a dinner in Saturday night, would you like to join us?')
print('Hi ' + guest_invited[5] + '! We are gonna have a dinner in Saturday night, would you like to join us?')
print('Hi ' + guest_invited[6] + '! We are gonna have a dinner in Saturday night, would you like to join us?')

print('Guys, I just got a bad news that I can only invite two of our guests tonight.')
popped_guest = guest_invited.pop()
print('Sorry ' + popped_guest + ' you can not be invited to our dinner.')
popped_guest = guest_invited.pop()
print('Sorry ' + popped_guest + ' you can not be invited to our dinner.')
popped_guest = guest_invited.pop()
print('Sorry ' + popped_guest + ' you can not be invited to our dinner.')
popped_guest = guest_invited.pop()
print('Sorry ' + popped_guest + ' you can not be invited to our dinner.')
popped_guest = guest_invited.pop()
print('Sorry ' + popped_guest + ' you can not be invited to our dinner.')
print('Congrats ' + guest_invited[0] + ' you are sitll invited.')
print('Congrats ' + guest_invited[1] + ' you are sitll invited.')

del guest_invited[1]
del guest_invited[0]

print(guest_invited)
len(guest_invited)