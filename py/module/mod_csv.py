import csv

with open('names.csv', 'w', newline='') as csvFile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)

writer.writeheader()
writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
