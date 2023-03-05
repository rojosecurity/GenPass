#!/usr/bin/python3

import argparse
import string
import random



class GenPASS:
    
    def __init__(self):
        parser = argparse.ArgumentParser(description = 'Generador de contraseñas')
        parser.add_argument('-l',dest='longitudPasswd',help='numero de caracteres para su password')
        self.arguments = parser.parse_args()

    def LongitudPassword(self):
        for n in range(int(self.arguments.longitudPasswd)):
            self.pwdMinima = random.choice(string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase)
            print(self.pwdMinima,end="")
    

# instancia de la clase
getPasswd = GenPASS()
getPasswd.LongitudPassword()
    