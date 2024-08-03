# A prototype of tourism data extraction

import requests
from bs4 import BeautifulSoup
import csv

# TODO: Data POSTed by user through Front-End
# year = int(input("Year: "))
# month = int(input("Month: "))

year = 2024
month = 7

# Get HTML data and structure
URL = f"https://www.malaysia.travel/events/{year}/{month:02}"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

events = []

# Extract events
for card in soup.findAll('div', attrs = {'class':'card w-100 border-0 border mb-3'}):
    event = {}
    categories = []

    event['title'] = card.h5.text
    event['link'] = "https://www.malaysia.travel" + card.a['href']
    event['desc'] = card.p.text
    date = card.find('div', attrs = {'class':'card-footer bg-gray-100 border-0'})
    event['date'] = date.text.strip()
    for row in card.findAll('div', attrs = {'class':'btn btn-sm nohover mb-3'}):
        categories.append(row.text)
    event['category'] = ','.join(categories)
    events.append(event)

# Generate results in csv file
filename = 'web-scrap-gen.csv'
with open('web-scrap-gen.csv', 'w') as file:
    out = csv.DictWriter(file, ['title','link','desc', 'date', 'category'])
    out.writeheader()
    for event in events:
        out.writerow(event)
