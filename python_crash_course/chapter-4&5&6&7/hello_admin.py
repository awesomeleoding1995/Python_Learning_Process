# Updated date: 3/3/2020
# Author: Lee Ding
# Make a list of five or more usernames, including the name 'admin'. Imagine you
# are writing code that will print a greeting to each user after they log in to 
# a website. Loop through the list, and print a greeting to each other.

users = ['admin', 'eric', 'eggy', 'evelyn', 'lee']

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")