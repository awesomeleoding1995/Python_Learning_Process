# Store a person's name, and include some whitespace characters at the beginning and the end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.

first_name = "\tLee"
last_name = "\nDing\n"
full_name = first_name + last_name
print (full_name)

full_name = first_name.lstrip() + last_name
print (full_name)

full_name = first_name.lstrip() + last_name.strip()
print (full_name)