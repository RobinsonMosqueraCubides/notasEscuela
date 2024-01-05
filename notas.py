from statistics import mean
from estudiante import *
def agregarNotas(notas, codigo,clave):

    student[codigo][clave].append(notas)

def calculoNotas(id):
    notaFinal=0
    if len(student[id]["parcial"]) != 0:
        parcial = (mean(student[id]["parcial"]))*0.5
        notaFinal+=parcial
    elif len(student[id]["quiz"]) != 0: 
        quiz = (mean(student[id]["quiz"]))*0.35
        notaFinal+=quiz
    elif len(student[id]["taller"]) !=0: 
        taller = (mean(student[id]["taller"]))*0.15
        notaFinal+=taller
    else:
        print("no hay notas registradas")
    return notaFinal

def pasarMateria():

    for i in student.keys():
        x = calculoNotas(i)
        if x < 3.6:
            
            return i