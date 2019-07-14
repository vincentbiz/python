import csv
import random

number = random.randint(1,531)

with open('steambook.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    titles = []
    for line in csv_reader:
        titles.append(line['ï»¿Title'])
    print(titles[number])
