# saves names and numbers to a CSV file

import csv

# get name and number
name = input("Name: ")
number = input("Number: ")

# open CSV file
with open("phonebook.csv", "a") as file:

    # print to file
    writer = csv.writer(file)
    writer.writerow([name, number])

