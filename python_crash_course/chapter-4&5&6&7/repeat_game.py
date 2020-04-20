prompt = "Please enter your age to check the price in your age: "
prompt += "\n,or enter 'quit' to end the game."

age = ""
while age != 'quit':
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("You can watch the movie for free.")
        elif age <= 12:
            print("Your ticket is $10.")
        elif age > 12:
            print("Your ticket is $15.")
