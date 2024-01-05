import os
from estudiante import *
from notas import *
from manejoErrores import *
def menuNotas(select1, codigo):
    comodin = codigo
    if select1 == 1:    
        print("ingrese la nota del parcial\n")
        notaParcial = validarNumero()
        x = rangoNotas(notaParcial)
        if x:
            agregarNotas(notaParcial,codigo,"parcial")
            menoSecundario()
        else:
             os.system('cls')
             print("Ingresa un numero del 1 al 5")
             menuNotas(select1=1, codigo=comodin)
             
    elif select1 == 2:
       
        print("Ingrese la nota del quiz:\n")
        quices = validarNumero()
        agregarNotas(quices,codigo,"quiz")
        menoSecundario()
    elif select1 == 3:
           
        print("Ingrese la nota del taller:\n")
        taller = validarNumero()
        agregarNotas(taller,codigo,"taller")
        menoSecundario()
    else:
        print("Numero ingresado es invalido")
        menoSecundario()
    
        

def menoSecundario(select=2):
    if select == 1:

        print("Ingrese el codigo del estudiante")
        
        codigo = int(validarNumero())
        x = validarEstudiante(codigo)
        if x == False:
            print("Ingrese el Nombre del estudiante")
            nombre = validarSTR()
            print("ingrese la edad del estudiante")
            edad = int(validarNumero())
            alumno(codigo,nombre,edad)
            print("Desea agregar otro alumno\n1. Sí\n2. No")
            select2 = validarNumero()
            if select2 == 1:
                menoSecundario(select2)
            elif select2 == 2:
                os.system("cls")
                menuPrincipal()
            else: 
                 os.system("cls")
                 print("ingrese 1 para agregar o 2 para salir")
        else:
            print(f"Estudiante ya existe es: {student[codigo]['nombre']}")
            menuPrincipal()
    
           
    elif select == 2:
        print("Codigo\tNombre")
        for i in student:
            print(f"{i}\t{student[i]['nombre']}")
        print("ingrese el codigo del estudiante o 0 para regresar el menu principal:")
        codigo = validarNumero()
        if codigo != 0:
            x = validarEstudiante(codigo)
            if x == True:
                print("1. Notas de parcial\n2. Nota de quiz\n3. Nota de taller")
                select1 = validarNumero()
                menuNotas(select1,codigo)
                
            else:
                print("Estudiante no existe")
                menoSecundario()
        else:
            menuPrincipal()
    elif select == 3:
        print("ingrese el codigo del estudiante o 0 para regresar al menu principal:")
        id = int(validarNumero())
        if id != 0: 
            x = validarEstudiante(id)
            if x == True:
                imprimirEstudiantes(id)
                notasFinal = calculoNotas(id)
                print(f"Nota final {notasFinal}")            
            else:
                print("Estudiante no existe")
                menoSecundario(select=3)
        else: menuPrincipal()
        
    elif select == 4:
        clave = pasarMateria()
        print(f"{student[clave]['nombre']}")
        
    else:
        menuPrincipal()

def menuPrincipal():
    
    while True:
        
        print("1. Registrar alumno\n2. Registrar notas\n3. Buscar Estudiante\n4. Listar estudiantes que no pasaron\n5. Salir")
        
        select = validarNumero()
        

        if select == 1:
                os.system("cls")
                menoSecundario(select)
                break
        elif select == 2:
                os.system("cls")
                menoSecundario(select)
                break
        elif select == 3:
                os.system("cls")
                menoSecundario(select)
                break
        elif select == 4:
                os.system("cls")
                menoSecundario(select)
        elif select == 5:            
                break        
        else:
                os.system("cls")
                print("Ingreso no valido, por favor ingrese un numero del 1 al 5")
        

menuPrincipal()

