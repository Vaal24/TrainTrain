# -*- coding: utf-8 -*-
import urllib2
import json
import datetime

url = 'https://api.irail.be/connections/?to=Yvoir&from=Nivelles&format=json'

# Récupération des données via urllib2
req = urllib2.Request(url)
handle = urllib2.urlopen(req)
res = handle.read()


# Transformation des données au format json en un dictionaire python
res = json.loads(res)


# Boucle sur les départs
data = []
for connection in res.get('connection'):
        data.append({'Train':connection.get('departure').get('vehicle'),'Duration':str(datetime.timedelta(seconds=int(connection.get('duration'))))[0:-3]})



#print json.dumps(data)

#recupereles donnée des départ (retard et heure)

url = 'https://api.irail.be/liveboard/?station=Nivelles&fast=true&format=json'

# Récupération des données via urllib2
req = urllib2.Request(url)
handle = urllib2.urlopen(req)
res = handle.read()

# Transformation des données au format json en un dictionaire python
res = json.loads(res)

data2 = []
for depart in res.get('departures').get('departure'):
        data2.append({'Train': depart.get('vehicle'), 'delay': int(depart.get('delay'))/60, 'Depart':depart.get('time')})

#print json.dumps(data2)


#fusion des deux data
dataFinal =[]
for d1 in data: 
	for d2 in data2:
		if d1.get('Train') == d2.get('Train'):
			dataFinal.append({'Departure time':d2.get('Depart'),'Delay':d2.get('delay'),'Duration':d1.get('Duration')})



print json.dumps(dataFinal)




	




