# Last updated: 8/3/2020
# Author: Lee Ding
# Write a class called Employee. The __init__()method should take in a first
# name, a last name, and an annual salary, and store each of these as attributes.

class Employee():
    """class Employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """initialise parameters"""

        self.first_n = first_name
        self.last_n = last_name
        self.annual_s = annual_salary

    def give_raise(self, salary_incr=5000):
        """add annual salary by default or other setting numbers"""

        self.annual_s += salary_incr

