from urllib import response
import requests
import json

responsed = requests.get('https://www.thesportsdb.com/api/v1/json/2/searchplayers.php?p=Luka%20Modric')
print(responsed.status_code)

pagina= json.loads(responsed.text)

print(pagina['player'][0]['strDescriptionES'])

