class User():
	"""this class is used to create user-related profile"""

	def __init__(self, first_name, last_name):
		self.f_name = first_name
		self.l_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		formatted_name = self.f_name + " " + self.l_name
		return formatted_name.title()

	def greet_user(self):
		print("Thanks for logging in!")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def rest_login_attempts(self):
		self.login_attempts = 0

class Admin(User):
	""" This is a child class of User"""

	def __init__(self, first_name, last_name):
		"""initialise parent class"""

		super().__init__(first_name, last_name)
		self.privilege = Privileges()
		
	
class Privileges():
	"""describe tha attribute of admin"""

	def __init__(
			self,
			privileges = [
				'can add post', 'can delete post',
				'can ban user', 'can manage post' 
				]
 			):
		self.privileges = privileges

	def show_privileges(self):
		for privilege in self.privileges:
			print("\nYou " + privilege)




admin = Admin('eggy', 'zhang')
admin_name = admin.describe_user()
print("Welcome " + admin_name)
admin.privilege.show_privileges()
admin.greet_user()


# user_1 = User('william', 'wu')
# user_2 = User('gerard', 'bai')
# user_3 = User('eggy', 'zhang')

# user_1_name = user_1.describe_user()
# print("\nWelcome " + user_1_name)
# user_1.greet_user()

# # counter = 0
# for counter in range(0, 5):
# 	user_1.increment_login_attempts()
# 	print(str(user_1.login_attempts))
# 	counter += 1
# user_1.rest_login_attempts()
# print(str(user_1.login_attempts))
# user_2_name = user_2.describe_user()
# print("\nWelcome " + user_2_name)
# user_2.greet_user()

# user_3_name = user_3.describe_user()
# print("\nWelcome " + user_3_name)
# user_3.greet_user()