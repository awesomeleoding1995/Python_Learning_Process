class Restaurant():
	"""store restaurant name and cuisine type"""

	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type

	def describe_restaurant(self):
		print("The is a " + self.type.title() + 
			" restaurant called " + self.name.title() + ".")

	def open_restaurant(self):
		print("Now the restaurant is opening.")

class IceCreamStand(Restaurant):
	"""this is the child class of Restaurant"""

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavours = ''

	def describe_flavour(self, flavour):
		self.flavours = flavour
		print("This is a " + self.flavours.title() + " ice cream.")

ice_cream = IceCreamStand('dariy queen', 'italian')
ice_cream.describe_flavour('pieapple')









# restaurant_1 = Restaurant('paparich', 'malaysia')
# # print("this is a " + restaurant_1.type.title() + " restaurant called " + 
# # 	restaurant_1.name.title())
# restaurant_1.describe_restaurant()
# # restaurant_1.open_restaurant()

# restaurant_2 = Restaurant('tianfuli', 'sichuan')
# restaurant_2.describe_restaurant()

# restaurant_3 = Restaurant('universal', 'italian')
# restaurant_3.describe_restaurant()