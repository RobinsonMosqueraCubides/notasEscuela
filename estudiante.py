
student = {}
def alumno(codigo, nombre, edad):
    student[codigo]={"nombre": nombre,
                     "edad": edad,
                     "quiz":[],
                     "taller": [],
                     "parcial" : []}

def validarEstudiante(codigo):

    if codigo in student:
        return True
    else:
        return False    

def imprimirEstudiantes(id):
    print(f"Nombre: {student[id]['nombre']}\nNotas de parcial: {student[id]['parcial']}\nNotas de Quiz: {student[id]['quiz']}\nNotas de talleres: {student[id]['taller']}")
    

    
    