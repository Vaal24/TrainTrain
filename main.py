# -*- coding: utf-8 -*-
import urllib2
import json
import datetime

def nextTrain(depart,destination):
	url = 'https://api.irail.be/connections/?to='+destination+'&from='+depart+'&format=json'

	# Récupération des données via urllib2
	req = urllib2.Request(url)
	handle = urllib2.urlopen(req)
	res = handle.read()


	# Transformation des données au format json en un dictionaire python
	res = json.loads(res)


	# Boucle sur les départs
	data = []
	for connection in res.get('connection'):
		data.append({'Train':connection.get('departure').get('vehicle'),'Duration':str(datetime.datetime.fromtimestamp(int(connection.get('duration'))).strftime('%H:%M'))})


	#recupereles donnée des départ (retard et heure)

	url = 'https://api.irail.be/liveboard/?station='+depart+'&fast=true&format=json'

	# Récupération des données via urllib2
	req = urllib2.Request(url)
	handle = urllib2.urlopen(req)
	res = handle.read()

	# Transformation des données au format json en un dictionaire python
	res = json.loads(res)

	data2 = []
	for depart in res.get('departures').get('departure'):
		data2.append({'Train': depart.get('vehicle'), 'delay': int(depart.get('delay'))/60, 'Depart':str(datetime.datetime.fromtimestamp(int(depart.get('time'))).strftime('%H:%M'))})



	#fusion des deux data
	dataFinal =[]
	for d1 in data: 
		for d2 in data2:
			if d1.get('Train') == d2.get('Train'):
				dataFinal.append({'Departure time':d2.get('Depart'),'Delay':d2.get('delay'),'Duration':d1.get('Duration')})



	return json.dumps(dataFinal)


print nextTrain('Nivelles','Yvoir')
print nextTrain('Nivelles','Ath')



	




