#bloque basico de manejo de errores
try:
    n = int(input("Introduce un número: "))

    m = 7

    print("{}/{} = {}".format(m,n,m/n))
except:
    print("ingrese un valor correcto")


## abstrayendo en una funcion los bloques try -except 
listaGlobal=[]
listaGlobalv2=[1,2,3,32,32,2,3]
def retirarElementos(listaParametro:list):
    try:
        listaParametro.pop()
        print(listaParametro)
    except:
        print("la lista esta vacia")

retirarElementos(listaGlobal)
retirarElementos(listaGlobalv2)

try:
    a="hola"
    """ print(a+1) """
except:
    print("except")
else:
    print("solo si el bloque try ejecuta correctamente ok")
finally:
    print("siempre se ejecuta")








