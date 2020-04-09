import requests
import datetime
from pytz import timezone

x = datetime.datetime.now()
print(x)
datetime_obj_pacific = timezone('US/Pacific').localize(x)
print(datetime_obj_pacific)

today = "2"
for i in range(1,10):
    today = today + str(datetime_obj_pacific)[i]

print(today)


url = 'https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json'

response = requests.get(url)
print(response)
quotes = response.json()['quoteText']
author = response.json()['quoteAuthor']
link = response.json()['quoteLink']
print(quotes)
print(author)
print(link)