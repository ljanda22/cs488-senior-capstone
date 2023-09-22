import csv

filename = "creditcard.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        row.append(row)

    print("Total no. of rows: %d"%(csvreader.line_num))
    print('Field names are: ' + ', ' .join(field for field in fields))

    print('\nRows are:\n')
for row in rows[:284808]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')
