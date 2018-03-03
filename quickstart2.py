import requests
import csv    
import io

headers={}
headers["User-Agent"]= "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0"
headers["DNT"]= "1"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
headers["Accept-Encoding"] = "deflate"
headers["Accept-Language"]= "en-US,en;q=0.5"
lines = []

file_id="1YSel8ALqzSlUh9Ye7Fun2abLL-UsIIR7nYl6Hr8KG1A"
url = "https://docs.google.com/spreadsheets/d/{0}/export?format=csv".format(file_id)

r = requests.get(url)

data = {}
cols = []

sio = io.StringIO( r.text, newline=None)
reader = csv.reader(sio, dialect=csv.excel)
rownum = 0

for row in reader:
    if rownum == 0:
        for col in row:
            data[col] = ''
            cols.append(col)

    else:
        i = 0
        for col in row:
            data[cols[i]] = col
            i = i +1

        print data
    rownum = rownum + 1
