# Task 2: CSV to List of Dictionaries (people.csv)
import csv

people_list = []

try:
    with open("people.csv", "r") as file:
        lines = file.readlines()

        headers = lines[0].strip().split(",")

        for line in lines[1:]:
            values = line.strip().split(",")

            person = {}

            for i in range(len(headers)):
                person[headers[i]] = values[i]

            people_list.append(person)

    print("People List:")
    for person in people_list:
        print(person)

except Exception as e:
    print("An exception occurred:", e)