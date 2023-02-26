## estos son las listas , tuplas , diccionarios ,conjuntos
## tenemos las notas del salon de clases , cuantas variables son si hay 30 alunmos 
## serina 30 numeros
listaNumeros=[] # lista vacia
listaNumeros=[1,2,3,4,5,6,7]
print(type(listaNumeros))
listaAll=['hola','1',1,2.2,True,4]
print(type(listaAll))
### accedo a un elemento ,cada posicion tiene un numero que comienza desde cero 
print(listaAll[0])
print(len(listaAll))
# cual seria la ultima posicion de cualquier lista
ultimaposicion=len(listaAll)-1
print(listaAll[ultimaposicion])
print(listaAll[-1])
## palabra intersante que es el " in "

print("1" in ['hola','1',1,2.2,True,4])
print("12" in listaAll)

##metodos 
print("lista  antes => ", listaAll)
listaAll.append('nuevo elemento')
print("lista  despues => ", listaAll)
print(listaAll.count(5))# cuantas veces hay el elemento del parametro

### funcion (parametro) -> la funcion o metodo lleva 0 o n parametros

print(listaAll.index(1))
print(listaAll[listaAll.index(1)])

print("lista  antes => ", listaAll)
listaAll.remove(4)
print("lista  despues => ", listaAll)
## modificando un elemento de la lista
print(listaAll[2])
listaAll[2]="HOLA AMIGOS"
print(listaAll[2])
### lista anidada

listaAnidada=[1,12,[12,12],["hola"],(1,2),{'key1':1,'key2':2}]
## accediendo a ella
print("valor de listaanidada=>",listaAnidada[2][0])
print("valor de listaanidada=>",listaAnidada[-1]['key1'])
## una cadena de texto tmb es una lista

mensage="Hola como vamos hoy"
print(mensage[1])
print(mensage[::-1])# cambiar orden

### tuplas 
tupla = (100,"Hola",[1,2,3],-50,('mundo',20))
print(tupla,"=>",type(tupla),"=>",tupla[1])
## accediendo a un elemento
print(tupla[2])
##tupla[2]="HOLA AMIGOS" => las tuplas no se pueden modificar
print(tupla[2])

## diccionario
# Diccionario vacio
vacio = {} # dict()
vacio
type(vacio)

numeros = {
        'num1': 12,
        'num2': 15
        }
print(numeros,"=>",numeros["num1"])

## conjuntos
conjunto = set() # conjunto vacio
conjunto = {1,2,3,3,3,4,5}
print(conjunto)

print(1==int('1'))
### 

