import csv

with open('spreadsheet2.csv', 'w') as csv_data:
    csvwriter = csv.writer(csv_data)
    csvwriter.writerow(['forename','surename', 'email'])
    csvwriter.writerow(['john', 'mcgovern', 'john@blahblahblah.com'])
    csvwriter.writerow(['trevor', 'sullivan', 'trevor@blahblahblah.com'])