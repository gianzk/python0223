def indexOfList(lista:list):
    try:
        print(lista[5])
    except:
        print("esta fuera de rango")
    

listaGlobal=[1,2131,1,23,23,12]
listaVacia=[]
indexOfList(listaGlobal)
### mejoramos los errores

def indexOfListv2(lista:list):
    try:
        lista.pop()
    except Exception as error:
        print("este es el error =>",error)

indexOfListv2(listaVacia)