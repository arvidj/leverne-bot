import requests
import re
from bs4 import BeautifulSoup, Tag, NavigableString
import json

from datetime import datetime

def strings_cc(strs):
    r = ''
    for i in strs:
        r += i
    return r


months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december']
# ymonths = [(year, month) for year in range(2008, 2017) for month in months]
ymonths = [(year, month) for year in range(2009, 2017) for month in months]


entries = []
for ym in ymonths:
    print("%s - %s" % ym)
    url = 'http://dannejohansson.se/%s/%s/' % ym
    print(url)
    html_doc = requests.get(url)
    if html_doc.status_code == 200:
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        for entry in soup.find_all(class_='entrybody'):
            title = entry.find('h3').string

            meta = entry.find(class_='entrymeta2')
            # Skrivet 31 August - 2009, 16:56
            date_str = re.search("Skrivet (\d*.*)", ''.join(list(meta.strings))).group(1)
            date = datetime.strptime('31 August - 2009, 23:15', "%d %B - %Y, %H:%M")

            body = ''
            for i in meta.next_siblings:
                if (isinstance(i, Tag) and
                    i.has_attr('class') and
                    'entrymeta' in i['class']):
                    # print("break")
                    break

                if (isinstance(i, Tag) and i.strings):
                    # if not i.strings:
                    #     print (i)
                    body += strings_cc(i.strings)
                if (isinstance(i, NavigableString)):
                    body += str(i)


            # print("Title: ", title)
            # print("Date: ", date)
            # print("Body: ", body.strip())

            entries.append({
                'title': title,
                'date': str(date),
                'body': body
            })

    else:
        print("Could not fetch %s, got code %s" % (url, html_doc.status_code))


f = open('danne.json', 'w+')
json.dump(entries, f)
f.close()
