def make_shirt(size, slogon):
	"""this function is used to display the shirt customers order"""
	# print("You order a " + str(size) + " size T shirt with slogon: " + slogon + ".")
	shirt = "You order a " + str(size) + " size T shirt with slogon: " + slogon + "."
	return shirt

while True:
	print("Please enter the size and slogon for your shirt.")
	order_size = input("Size: ")
	order_slogon = input("Slogon: ")
	message = make_shirt(size = order_size, slogon = order_slogon)
	print(message)
