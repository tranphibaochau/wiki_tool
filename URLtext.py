import requests
import csv

def urlRequest(IP, timeS): #Requests HTML page
    response = requests.get("http://metrics.torproject.org/exonerator.html?ip={IP}&timestamp={timeS}&lang=en".format(IP = IP, timeS = timeS))
    index = response.text[8535:8585]
    return index

data = []
with open('tor_wikipedia_edits_20180522.tsv') as file: #Opens data file
    data_csv_reader = csv.reader(file, delimiter='\t')
    next(data_csv_reader) #Skips headers line
    for rows in data_csv_reader:
        row = []
        for cell in rows:
            row.append(cell)
        if rows != []:
            data.append(row)

with open('TorHTMLResults.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    headers = ['revid', 'editor', 'datetime', 'reverting', 'reverted', 'match']
    writer.writerow(headers)
    for i in range(len(data)):
        date = data[i][2].split(' ')
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
        print(currentRow)
"""        
rows[2] = rows[2].split(' ') #Gets YYYY-MM-DD from date and time
row.append(rows[1])
row.append(rows[2][0])
"""