import csv
import datetime
import os

# Employee data
fields = ["employee_id", "first_name", "last_name", "department"]
rows = [
    ["1", "John", "Bowman", "HR"],
    ["2", "Lauren", "Davis", "HR"],
    ["3", "David", "Smith", "Sales"],
    ["4", "Alice", "Johnson", "Marketing"],
    ["5", "Charlie", "Brown", "Finance"],
    ["6", "Jane", "Doe", "IT"],
    ["7", "Mike", "Miller", "IT"],
    ["8", "Sophia", "Martinez", "Marketing"],
    ["9", "Phillip", "Garcia", "Sales"],
    ["10", "William", "Anderson", "Finance"],
    ["11", "Olivia", "Thomas", "Engineering"],
    ["12", "James", "Jackson", "HR"],
    ["13", "Isabella", "White", "IT"],
    ["14", "Benjamin", "Harris", "Sales"],
    ["15", "Mia", "Clark", "Marketing"],
    ["16", "Lucas", "Lewis", "Finance"],
    ["17", "Amelia", "Robinson", "Engineering"],
    ["18", "Henry", "Walker", "HR"],
    ["19", "Evelyn", "Hall", "IT"],
    ["20", "Ethan", "Young", "Engineering"]
]

employees = {"fields": fields, "rows": rows}

employee_id_column = 0

def read_employees():
    global employees
    return employees

def column_index(name):
    return fields.index(name)

def first_name(employee_id):
    for row in employees["rows"]:
        if row[0] == str(employee_id):
            return row[1]
    return None

def employee_find(employee_id):
    return [row for row in employees["rows"] if row[0] == str(employee_id)]

def employee_find_2(employee_id):
    return [row for row in employees["rows"] if row[0] == str(employee_id)]

def sort_by_last_name():
    return sorted(employees["rows"], key=lambda x: x[2])

def employee_dict(row):
    return {fields[i]: row[i] for i in range(1, len(fields))}

def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_dict = employee_dict(row)
        result[row[0]] = emp_dict
    return result

def get_this_value():
    return "ABC"

def set_that_secret(value):
    import custom_module
    custom_module.secret = value

# Minutes
minutes1 = None
minutes_set = None
minutes_list = None

def read_minutes():
    global minutes1
    with open("minutes.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        data = [(row[0], row[1]) for row in reader]
    
    d1 = {"rows": sorted(data, key=lambda x: x[0], reverse=True)}
    d2 = {"rows": sorted([row for row in data if row[0] == "Sarah Murray"], key=lambda x: x[1])}
    minutes1 = d1
    return d1, d2

def create_minutes_set():
    global minutes_set
    with open("minutes.csv", "r") as f:
        lines = f.read().splitlines()
    minutes_set = set(lines)
    return minutes_set

def create_minutes_list():
    global minutes_list
    with open("minutes.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        data = []
        for row in reader:
            name, date_str = row
            dt = datetime.datetime.strptime(date_str, "%B %d, %Y")
            data.append((name, dt))
    minutes_list = data
    return minutes_list

def write_sorted_list():
    if minutes_list is None:
        create_minutes_list()
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    with open("minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Date"])
        for name, dt in sorted_list:
            date_str = dt.strftime("%B %d, %Y")
            writer.writerow([name, date_str])
    return [(name, dt.strftime("%B %d, %Y")) for name, dt in sorted_list]