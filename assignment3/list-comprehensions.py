import csv

# Read CSV into list of lists
# The header is: employee_id, first_name, last_name, phone
with open('../csv/employees.csv', mode='r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Task: Create a list of employee names (first_name + space + last_name)
# We skip data[0] because it is the header row.
# We use row[1] for first_name and row[2] for last_name.
full_names = [f"{row[1]} {row[2]}" for row in data[1:]]

print("Full Names List:")
print(full_names)

# Task: Create another list including only those names that contain the letter "e"
names_with_e = [name for name in full_names if 'e' in name.lower()]

print("\nNames containing the letter 'e':")
print(names_with_e)