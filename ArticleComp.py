import sys, csv
import pandas as pd

directories = []
first = []
second = []
third = []
with open('article_compositions20.txt') as csv_file:
    data_csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in data_csv_reader:
        if row != []:
            directories.append(row[1])
            data = (row[2:])
            rowUnsorted = []
            rowSorted = []
            for cell in data:
                cell = float(cell)
                rowUnsorted.append(cell)
                rowSorted.append(cell)
            rowSorted.sort()
            p1 = rowUnsorted.index(rowSorted[-1])
            p2 = rowUnsorted.index(rowSorted[-2])
            p3 = rowUnsorted.index(rowSorted[-3])
            first.append((p1 + 1, (rowSorted[-1] * 100)))
            second.append((p2 + 1, (rowSorted[-2] * 100)))
            third.append((p3 + 1, (rowSorted[-3] * 100)))

composition = {'Directories': directories, 'First': first, 'Second': second, 'Third': third}
table = pd.DataFrame(composition, columns = ['Directories', 'First', 'Second', 'Third'])
table.to_csv('ArticleCompositions20.csv', index = False)