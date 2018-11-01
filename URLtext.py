import requests
import csv
import sys

def urlRequest(IP, timeS): #Requests HTML page
    response = requests.get("http://metrics.torproject.org/exonerator.html?ip={IP}&timestamp={timeS}&lang=en".format(IP = IP, timeS = timeS))
    index = response.text[8535:8585]
    return index

data = []
with open(sys.argv[1]) as file: #Opens data file
    data_csv_reader = csv.reader(file, delimiter='\t')
    next(data_csv_reader) #Skips headers line
    for rows in data_csv_reader:
        row = []
        for cell in rows:
            row.append(cell)
        if rows != []:
            data.append(row)

with open(sys.argv[2], 'w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    headers = ['revid', 'editor', 'datetime', 'reverting', 'reverted', 'match']
    writer.writerow(headers)
    for i in range(len(data)):
        date = data[i][2].split(' ') #Gets just YYYY-MM-DD from Datetime
        urlIndex = urlRequest(str(data[i][1]), str(date[0]))
        if 'Result is positive' in urlIndex:
            result = 'TRUE'
        elif 'Result is negative' in urlIndex:
            result = 'FALSE'
        else:
            result = 'Inconclusive'
        currentRow = data[i]
        currentRow.append(result)
        writer.writerow(currentRow)
        #print(currentRow)
