# Updated date: 3/3/2020
# Author: Lee Ding
# Use a dictionary to store information about a person you know. Store their 
# first name, last name, age and the city in which they live.

eggy = {
	'first_name' : 'jidan', 
	'last_name' : 'zhang',
	'age' : 25, 
	'city' : 'guangzhou'
	}

william = {
	'first_name' : 'jian', 
	'last_name' : 'wu',
	'age' : 27, 
	'city' : 'taiyuan'
	}

gerard = {
	'first_name' : 'zhe', 
	'last_name' : 'bai',
	'age' : 28, 
	'city' : 'huhehaote'
	}

people = [eggy, william, gerard]

for person in people:
	for k, v in person.items():
		if k == 'age':
			print(k.title() + " is " + str(v) + ".")
		else:
			print(k.title() + " is " + v.title() + ".")
	print("\n")


# print("The person's first name is " + person['first_name'].title())
# print("And last name is " + person['last_name'].title())
# print("Age is " + str(person['age']))
# print("Currently living in " + person['city'].title())

# for k, v in person.items():
# 	print(k.title() + " is " + str(v) + ".")