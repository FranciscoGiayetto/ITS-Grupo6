import requests
import json

nombre= input("Ingrese el nombre del jugador: ")
nombre= nombre.lower()
nombre= nombre.capitalize()

apellido= input("Ingrese el apellido del jugador: ")
apellido= apellido.lower()
apellido= apellido.capitalize()
try :
    responsed = requests.get (f'https://www.thesportsdb.com/api/v1/json/2/searchplayers.php?p={nombre}%20{apellido}')
    if responsed.status_code == 200:
        pagina= json.loads(responsed.text)
        print(pagina['player'][0]['strPlayer'])
except Exception as e:
    print('Jugador no encontrado')
