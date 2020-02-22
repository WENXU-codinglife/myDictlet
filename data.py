#!/usr/bin/python

import requests
import json

#TODO: replace with your own app_id and app_key
#app_id = '<my app_id>'
app_key = 'c1f42caf-a67f-46b9-aba6-e14c23e777e5'

#language = 'en'
word_id = 'selfie'

url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/' + word_id + '?key=' + app_key

r = requests.get(url)

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))