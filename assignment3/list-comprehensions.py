import csv

# Read CSV into list of lists
with open('../csv/employees.csv', mode='r') as file:
    reader = csv.reader(file)
    data = list(reader)

# 1. Employee names (First Last), skipping header
full_names = [f"{row[0]} {row[1]}" for row in data[1:]]
print("Full Names:", full_names)

# 2. Names containing the letter 'e'
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("Names with 'e':", names_with_e)