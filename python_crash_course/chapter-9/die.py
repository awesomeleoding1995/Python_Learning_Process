from random import randint

class Die():
	"""this is a class for rolling dice"""

	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		point = randint(1, self.sides)
		print("You have rolled " + str(point) + ".")

my_die = Die(20)
for counter in range(0, 10):
	my_die.roll_die()
