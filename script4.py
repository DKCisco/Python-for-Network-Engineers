import csv

with open("spreadsheet1.csv", 'r') as csv_data:
    csv_reader = csv.DictReader(csv_data)
    #print(csv_reader)
    for row in csv_reader:
        print(row["surname"])