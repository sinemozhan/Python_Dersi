import csv

with open('iris.data',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['0'],
              row['2'],
              row['3'],
              row['3'],
              row['4'])


