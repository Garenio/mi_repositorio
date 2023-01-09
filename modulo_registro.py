import json
from pprint import pprint
from google.colab import drive
drive.mount('/drive/')

ruta = "/drive/MyDrive/Curso Python/001 - Primera pre-entrega+Garcia"

cuentas_db = {}

def inicio():       # FUNCIÓN DE PORTAL DE INICIO
    print("Bienvenido al Gestor de Usuarios.")
    print("Para continuar escriba una de las siguientes acciones:")
    print("")
    print("REGISTRO > Se inicia el proceso de registro de usuarios.")
    print("LOGIN > Se inicia el proceso de inicio de sesión de usuarios.")
    print("CONSULTAR > Se muestra la lista de todos los usarios registrados.")
    print("SALIR > Se finaliza el programa.")
    print("")
    while True:
        accion = input("Escriba una opción:    ")
        if accion == "REGISTRO" or accion == "registro":
            registro()
            break
        elif accion == "LOGIN" or accion == "login":
            login()
            break
        elif accion == "CONSULTAR" or accion == "consultar":
            consultar()
            break
        elif accion == "SALIR" or accion == "salir":
            print("Gracias por usar el Gestor de Usuarios.")
            break
        else:
            print("")
            print("Opción incorrecta.")
            print("")

def registro():     # FUNCIÓN DE REGISTRO DE USUARIOS
    print("")
    print("======================================================")
    print("")
    print("Bienvenido/a al registro de usuarios.")
    print("Escriba un nuevo usuario y contraseña:")
    print("")
    usuario = input("> Nombre de Usuario:    ")
    contrasenia = input("> Contraseña:    ")
    cuentas_db[usuario] = contrasenia       # Con esto estoy agregando el par key-value en dict cuentas_db.
    with open(ruta + "/cuentasDB.json", "w") as f:
        json.dump(cuentas_db, f, indent=4)      # Aquí guardo el valor actual del dict cuentas_db en un archivo externo.
    print("")
    print(f"¡Se regristró el usuario {usuario} con contraseña {contrasenia}!")
    print("")
    print("======================================================")
    return(inicio())


def login():    # FUNCIÓN DE LOGEO DE USUARIOS
    print("")
    print("======================================================")
    print("")
    print("Bienvenido/a!")
    print("Escriba su usuario y contraseña para logear:")
    print("")
    usuario = input("Usuario:    ")
    if usuario in cuentas_db.keys():        # Aquí verifico que el usuario ingresado existe en la DB
        print("Usuario encontrado...")
        intentos = 0
        while intentos < 3:     # Defino una cantidad máxima de intentos para acceder
            contrasenia = input("Contraseña:    ")
            if contrasenia == cuentas_db[usuario]:      # Se compara la contraseña ingresada con el valor de la key del dict.
                print("La contraseña es correcta. ¡Acceso autorizado!.")
                break
            else:
                intentos += 1
                print(f"La contraseña es incorrecta. Te quedan {3 - intentos} intento/s antes de que se bloquee la cuenta.")
        else:
            print("")
            print("===========================")
            print("La cuenta ha sido bloqueada")
            print("===========================")
    else:
        print(f"El usuario {usuario} no se encuentra en la DB.")
        login()


#FUNCIÓN DE CONSULTA DE LA DB DE LAS CUENTAS:

def consultar():
    print("")
    print("======================================================")
    print("")
    print("Las cuentas registradas en la DB son:")
    with open(ruta + "/cuentasDB.json") as file:
        registroCuentas = json.load(file)
        pprint(registroCuentas)
#FUNCIÓN DE CONSULTA DE LA DB DE LAS CUENTAS:

def consultar():
    print("")
    print("======================================================")
    print("")
    print("Las cuentas registradas en la DB son:")
    with open(ruta + "/cuentasDB.json") as file:
        registroCuentas = json.load(file)
        pprint(registroCuentas)