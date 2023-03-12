import sys

ruta=sys.argv

print(ruta)
###
#pregunta 9
# definan las tuplas dentro de una lista

listaTotal=[('gian',20,'646464'),('marco',12,'123131')]#...

nombre=input('ingrese sus datos :') #nombre o dni => (elemento1 ,elemento2 ,elemento3)
listavacia=[]
#if tuplaformaste in lista 
## if edad>=18
##### lista.append((tupla))

## pregunta 10

curso={
    'nombre':"",
    'cantidad':0,
    'seccion':{
        'nombreSeccion':""
    }
    #......
}
cursoNombre=input("nombre de curso")
seccion1=input("nombre de seccion1")
curso['nombre']=cursoNombre
curso['seccion']['nombreSeccion']

print(curso)

## lista anidad
listaAnidad=[1,2,[123,122]]
listaAnidad[2][0]



###
""" import sys
import os
print(sys.argv[0])

def funcionRecursiva(path):
    for i in os.listdir(path):
        print(i)
        if file or direc :
            print
        else :
            funcionRecursiva(path+dir) """
