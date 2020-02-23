#!/usr/bin/python

import requests
import json

app_key = 'c1f42caf-a67f-46b9-aba6-e14c23e777e5'

def extr(word_id):
	url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/' + word_id + '?key=' + app_key
	r = requests.get(url)
	audio = r.json()[0]['hwi']['prs'][0]['sound']['audio']
	rcs = "https://media.merriam-webster.com/soundc11/s/" + audio + ".wav"
	return rcs
