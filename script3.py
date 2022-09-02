import csv

with open('spreadsheet1.csv', 'r') as csv_data:
    csv_reader = csv.reader(csv_data)

    with open('newfile.csv', 'w') as new_data:
        csv_writer = csv.writer(new_data, delimiter='\t') # '\t\' is using the tab instead of , for delimiter
        for line in csv_reader:
            csv_writer.writerow(line)