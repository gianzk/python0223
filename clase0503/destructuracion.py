el_primero, segundo,*el_resto = [1, 2, 3, 4, 5]

print(el_primero,type(el_primero))

# Output: 1

print(el_resto,type(el_resto))

# Output: [2, 3, 4, 5]


## con recursividad

listaGrand=[121,312,3,21,32,1,2132132121,3,21321,3,213,21321321,321,321,3213,23121,321,3213213231,12,3,213]

def evaluarLista(listaGrand):
    primero,*resto=listaGrand
    print(primero,resto,len(resto))
    if len(resto)!=1:
        return evaluarLista(resto)
    else:
        print("here")
        return "lista completa"
        

a=evaluarLista(listaGrand)
print(a)