import os

def validarNumero():

    while True:
        try:
            codigo = float(input(""))
            return codigo
            break
        except:
            os.system("clear")
            print("Ingrese un numero")

def validarSTR():
    pass