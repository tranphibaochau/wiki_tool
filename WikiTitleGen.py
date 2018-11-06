import sys, csv
from urllib.parse import quote
import pandas as pd

data = []
appendflag = False
flag = False
with open('tor_wikipedia_edits_20181026.tsv') as csv_file:
    data_csv_reader = csv.reader(csv_file, delimiter='\t')
    next(data_csv_reader)
    for row in data_csv_reader:
        if row != []:
            removeList = ['User', 'user:', 'Talk:', 'talk:', 'User talk:', 'User Talk:', 'user Talk:', 'user talk:']
            for word in removeList:
                if word in row[3]:
                    appendflag = False
                    break
                else:
                    appendflag = True
            if appendflag == True:
                title = quote(row[3].encode("utf-8"))
                data.append(title)
                appendflag = False

TitleList = []
for i in range(len(data)):
    if data[i] not in TitleList:
        TitleList.append(data[i])
    else:
        continue
    print(data[i])
    print(TitleList)
TitleList = pd.Series(TitleList)
Titles = pd.DataFrame(TitleList, columns = ['Titles'])
Titles.to_csv('WikiPageTitles.csv')