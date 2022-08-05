import requests
import json

def buscar_jugador():
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
            nombre= pagina['player'][0]['strPlayer']
            nacionalidad= pagina['player'][0]['strNationality']
            equipo= pagina['player'][0]['strTeam']
            altura= pagina['player'][0]['strHeight']
            peso= pagina['player'][0]['strWeight']
            descripcion= pagina['player'][0]['strDescriptionEN']
            deporte= pagina['player'][0]['strSport']
            fechaNacimiento= pagina['player'][0]['dateBorn']
            fechaMuerte= pagina['player'][0]['dateSigned']
            genero= pagina['player'][0]['strGender']
            posicion= pagina['player'][0]['strPosition']
            Dominante=pagina['player'][0]['strSide']
            foto= pagina['player'][0]['strCutout']

            print("Nombre del jugador "+ nombre
            +"\nNacionalidad del jugador "+ nacionalidad
            +"\nEquipo del jugador "+ equipo
            +"\nAltura del jugador "+ altura  
            +"\nPeso del jugador "+ peso
            +"\nDescripcion del jugador "+ descripcion
            +"\nDeporte del jugador "+ deporte
            +"\nFecha de nacimiento del jugador "+ fechaNacimiento
            +"\nFecha de muerte del jugador "+ fechaMuerte
            +"\nGenero del jugador "+ genero
            +"\nPosicion del jugador "+ posicion
            +"\nDominante del jugador "+ Dominante
            +"\nFoto del jugador "+ foto
            )

    except Exception as e:
        print(e)
        print('Jugador no encontrado')


