def show_magician(names):
	for name in names:
		print("Hello, " + name.title() + "!")

def make_great(names):
	new_names = []
	while names:
		current_name = 'the Great ' + names.pop()
		new_names.append(current_name)
	return new_names


magician_names = ['eggy', 'lee', 'gerard', 'william']
n_names = make_great(names = magician_names[:])
show_magician(names = n_names) 
print(magician_names)