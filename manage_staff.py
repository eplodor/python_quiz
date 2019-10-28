import numpy as np

class Employee:
	def __init__(self, id, name, position, salary):
		self.id = id
		self.name = name
		self.position = position
		self.salary = salary
	def read_data(self):
		print("|{:<10}".format(self.id), end='')
		print("|{:<10}".format(self.name), end='')
		print("|{:<10}".format(self.position), end='')
		print("|{:>10}".format(self.salary))

def create_employee(data_list):
	return (Employee(data_list[0], data_list[1], data_list[2], data_list[3]))

def create_staff_list(filename):
	employees = []
	with open(filename) as f:
		line = f.readline()
		while line:
			line = line.strip()
			employees.append(create_employee(line.split('#')))
			line = f.readline()
	return employees

def reorder_list(employees):
	return sorted(employees, key=lambda x: x.id)

def read_list(employees):
	for employee in employees:
		employee.read_data()

def display_options():
	print("\n1. New Staff")
	print("2. Delete Staff")
	print("3. View Summary Data")
	print("4. Save & Exit")

def display_records(list):
	print("|{:<10}".format("ID"), end='')
	print("|{:<10}".format("Name"), end='')
	print("|{:<10}".format("Position"), end='')
	print("|{:>10}".format("Salary"))
	orderered = reorder_list(list)
	read_list(orderered)

def is_existing_id(id, employees) :
	for employee in employees :
		if employee.id == id:
			return employee
	return 0

def delete_staff(employees):
	print("Delete Staff")
	id = input("Input ID[SXXXX]:")
	employee = is_existing_id(id, employees)
	if (employee != 0) :
		employees.remove(employee)
		print("Data has been successfully deleted")
	else:
		print("Data Not Found")

def input_id(employees):
	while 1:
		id = input("Input ID[SXXXX]:")
		if id[0] == 'S' and len(id) == 5 and is_existing_id(id, employees) == 0 and id[1:].isnumeric() :
			return id

def input_name():
	while 1:
		name = input("Input Name[0...20]:")
		if len(name) <= 20:
			return name

def input_position():
	while 1:
		position = input("Input Position[Staff|Officer|Manager]:")
		if position == "Staff" or position == "Officer" or position == "Manager":
			return position

def input_salary(position):
	while 1:
		salary = int(input("Input Salary for %s:" % position))
		if position == "Staff" and salary >= 3500000 and salary <= 7000000:
			return salary
		if position == "Officer" and salary >= 7000001 and salary <= 10000000:
			return salary
		if position == "Manager" and salary > 10000000:
			return salary

def new_staff(employees):
	id = input_id(employees)
	name = input_name()
	position = input_position()
	salary = input_salary(position)
	employees.append(Employee(id, name, position, salary))

def summary_data(employees):
	print("1. Staff")
	print("Minimum Salary : %d" % min(int(employee.salary) for employee in employees if employee.position == "Staff"))
	print("Maximum Salary : %d" % max(int(employee.salary) for employee in employees if employee.position == "Staff"))
	print("Average Salary : %d" % np.mean([int(employee.salary) for employee in employees if employee.position == "Staff"]))

	print("2. Officer")
	print("Minimum Salary : %d" % min(int(employee.salary) for employee in employees if employee.position == "Officer"))
	print("Maximum Salary : %d" % max(int(employee.salary) for employee in employees if employee.position == "Officer"))
	print("Average Salary : %d" % np.mean([int(employee.salary) for employee in employees if employee.position == "Officer"]))

	print("3. Manager")
	print("Minimum Salary : %d" % min(int(employee.salary) for employee in employees if employee.position == "Manager"))
	print("Maximum Salary : %d" % max(int(employee.salary) for employee in employees if employee.position == "Manager"))
	print("Average Salary : %d" % np.mean([int(employee.salary) for employee in employees if employee.position == "Manager"]))

def write_data(init, current, filename):
	#pas encore ajouté dans le fichier
	set1 = set(i.id for i in init)
	diff1 = [i for i in current if (i.id) not in set1]

	#pas encore supprimé
	set2 = set(c.id for c in current)
	diff2 = [c for c in init if c.id not in set2]

	with open(filename, "r+") as f:
		for d in diff1:
			f.write("%s#%s#%s#%s" % (d.id, d.name, d.position, d.salary))
	""" with open(filename, "r+") as f:
		lines = f.readlines()
		for c in current :
			for i in init :
				if c.id != i.id:
					f.write("%s#%s#%s#%s" % (c.id, c.name, c.position, c.salary))
					break
				else :
					for line in lines :
						if line[0:5] != c.id :
							f.write(line) """
	print("Exiting")
	exit()


def main():
	employees = create_staff_list("staff.txt")
	init = create_staff_list("staff.txt")
	while 1:
		display_records(employees)
		display_options()
		choice = input("Input Choice: ")
		if choice == "1":
			new_staff(employees)
		if choice == "2":
			delete_staff(employees)
		if choice == "3":
			summary_data(employees)
		if choice == "4":
			write_data(init, employees, "staff.txt")

main()