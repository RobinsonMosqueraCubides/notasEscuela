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


    
    