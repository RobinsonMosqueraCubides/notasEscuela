from statistics import mean
from estudiante import *
def agregarNotas(notas, codigo,clave):

    student[codigo][clave].append(notas)

def calculoNotas(id):

    parcial = (mean(student[id]["parcial"]))*0.5
    quiz = (mean(student[id]["quiz"]))*0.35
    taller = (mean(student[id]["taller"]))*0.15
    notaFinal = parcial+quiz+taller

    return notaFinal

def pasarMateria():

    for i in student.keys():
        x = calculoNotas(i)
        if x < 3.6:
            return i
        