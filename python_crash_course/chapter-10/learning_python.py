# Last updated: 7/3/2020
# Author: Lee Ding
# Write a program that reads the file and prints what you wrote three times.

file_name = '../text_files/learning_python.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

message = ''
for line in lines:
    message += line

message = message.replace('Python', 'Verilog')
print(message)
#     contents = file_object.read()

# for counter in range(3):
#     print(contents)