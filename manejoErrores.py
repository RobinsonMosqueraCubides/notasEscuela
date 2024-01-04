import os

def validarNumero():
    while True:
        try:
            codigo = float(input(""))
            return codigo
        except:
            os.system("clear")
            print("Ingrese un numero")

def validarSTR():

    while True:
        nombre = input("")
        
        if nombre.isalpha():
            return nombre
            break
        else:
            print("ingrese el nombre en letra")