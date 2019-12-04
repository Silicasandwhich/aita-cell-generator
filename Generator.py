import random

length = int(input("number of cells: "))
output = ""
for i in range(0,length):
	current_cell = "("
	current_cell += str(random.randint(1,99))
	if random.randint(1,2) == 1:
		current_cell += 'M'
	else:
		current_cell += 'F'
	current_cell += ')'
	output += current_cell
print(output)
