# Last updated: 7/3/2020
# Author: Lee Ding
# Write a program that prompts the user for their name. When they respond, Write
# their name to a file called guest.txt

file_name = '../text_files/guest_book.txt'
greeting_word = 'Howdy, '
user_name = ''

with open(file_name, 'a') as file_object:

	while user_name != 'q':
		message = 'Please enter your name:\n'
		message += 'And press q + Enter to quit.\n'
		user_name = input(message)

		if user_name != 'q':
			greeting = greeting_word + user_name + '!'
			print(greeting)

			file_object.write(greeting + "\n")


