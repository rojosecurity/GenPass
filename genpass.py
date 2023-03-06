#!/usr/bin/python3 # invocando el interprete de python

# importando modulos
import argparse
import string
import random

# generando clase 
class GenPASS:
    # Metodo inial
    def __init__(self):
    # definiendo los argumentos para invocar por consola
        parser = argparse.ArgumentParser(description = 'Generador de contraseñas')
        # el argumento -l es el que va a definir la logitud del password
        parser.add_argument('-l',dest='longitudPasswd',help='numero de caracteres para su password')
        self.arguments = parser.parse_args()
    
    # Metodo clave
    def LongitudPassword(self):
        # iterar de acuerdo al valor ingresado por el argumento
        for n in range(int(self.arguments.longitudPasswd)):
            # generar la contraseña aleatoria en base las diferentes funciones
            self.pwdMinima = random.choice(string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase)
            # imprimir la contraseña de acuerdo a la iteración
            print(self.pwdMinima,end="")

# instancia de la clase
getPasswd = GenPASS()
getPasswd.LongitudPassword()
    
