#!/usr/bin/python

import requests
import json

app_key = 'c1f42caf-a67f-46b9-aba6-e14c23e777e5'


def extr(word_id):
#get the URL
	url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/' + word_id + '?key=' + app_key
	r = requests.get(url)
	#rr = json.dumps(r.json(),indent = 2)
	#print(rr)
#pick out the URL of audio
	audio = r.json()[0]['hwi']['prs'][0]['sound']['audio']
	rcs = "https://media.merriam-webster.com/soundc11/" + word_id[0] + "/" + audio + ".wav"
#pick out the definitions
	n = len(r.json()[0]['def'][0]['sseq'])
	#print(n)
	Nofdef = []
	definitions = []
	index = 0
	while index < n:
		Nofdef.append(len(r.json()[0]['def'][0]['sseq'][index])) 
		#print(Nofdef)
		i = 0
		while i < Nofdef[index]:
			definitions.append(r.json()[0]['def'][0]['sseq'][index][i][1]['dt'][0][1])
			i = i + 1
		index = index + 1


	return rcs, definitions


