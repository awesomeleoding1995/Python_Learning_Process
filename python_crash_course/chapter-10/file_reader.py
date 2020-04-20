# file_name = '/Users/awesomeLeoding/OneDrive - RMIT University/Documents/python_work/python_crash_course/text_files/pi_digits.txt'
file_name = '../text_files/pi_digits.txt'
with open(file_name) as file_object:
    # contents = file_object.read()
    # # print(contents)
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines()

# for line in lines:
# 	print(line.rstrip())
pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))