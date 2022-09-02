import csv

with open('spreadsheet1.csv', 'r') as csv_data:
    csv_reader = csv.reader(csv_data)
    next(csv_reader)
    #print(csv_reader)
    for line in csv_reader:
        print(line[2])