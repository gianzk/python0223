import requests

url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat

# https://apis.net.pe/api-tipo-cambio.html

# 1. conectarme al sitio
response = requests.get(url)

data=response.json() # nos brinda la información en formato JSON

#print(type(data))  el formato json es un dict

#print(data['compra'])

###apuntar los que participan

## hacer una clase casaCambio inicializar con venta,compra
## hacer un metodo vender y comprar que reciba parametro el valor a comprar o vender
## hacer un menu iterativo que tenga la opicion de vender,comprar y que use la clase

msg="""
    1)ver tipo de cambio
    2)comprar
    3)vender
    4)salir
"""
##definimos la clase

###############
class CasaCambio:
    def __init__(self) -> None:
        pass
    def vender():
        pass
    def comprar():
        pass
    def __str__(self) -> str:
        pass


while(True):
    print(msg)
    opcion=int(input("ingrese una opcion"))

    if opcion==1:
        pass
    if opcion==2:
        pass
    if opcion==3:
        pass
    if opcion==4:
        pass
        print("gracias hasta luego")
        break