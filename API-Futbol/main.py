from pickle import FALSE, TRUE
import requests
import json

dic1=[]
x=TRUE

while x==TRUE:
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

            lines=["Nombre del jugador "+ nombre,
            "Nacionalidad del jugador "+ nacionalidad,
            "Equipo del jugador "+ equipo,
            "Altura del jugador "+ altura , 
            "Peso del jugador "+ peso,
            "Descripcion del jugador "+ descripcion,
            "Deporte del jugador "+ deporte,
            "Fecha de nacimiento del jugador "+ fechaNacimiento,
            "Fecha de muerte del jugador "+ fechaMuerte,
            "Genero del jugador "+ genero,
            "Posicion del jugador "+ posicion,
            "Dominante del jugador "+ Dominante,
            "Foto del jugador "+ foto]

            with open('PlayerInfo.txt', 'w') as f:
                for line in lines:
                    f.write(line)
                    f.write('\n')
    except Exception as e:
        print(e)
        print('Jugador no encontrado')
    x= input("Desea buscar otro jugador? (s/n) ")
    x= x.lower()
    if x=='n':
        x=FALSE
        print('Finalizando Busqueda')
        break
    elif x=='s':
        x=TRUE
        continue