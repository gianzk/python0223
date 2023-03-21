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
    3)vender|
    4)salir
"""
##definimos la clase
def getData():
    import requests
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)
    data=response.json()
    return data
class CasaCambio:
    def __init__(self,valor_compra:float,valor_venta:float) -> None:
        self.venta=float(valor_venta)
        self.compra=float(valor_compra)
    def vender(self,montoSoles)->float:
        return montoSoles/self.venta
    def comprar(self,montoDolares)->float:
        return montoDolares*self.compra
    def __str__(self) -> str:
        return f"el valor de la venta es {self.venta} y de compra es {self.compra}"


while(True):
    print(msg)
    opcion=int(input("ingrese una opcion"))
    data=getData()
    tc=CasaCambio(data['compra'],data['venta'])
    if opcion==1:
        print(tc)
    if opcion==2:
        Montocomprar=float(input("ingrese el monto a comprar:"))
        montoCliente=tc.comprar(Montocomprar)
        print("dar ",montoCliente,"en dolares")
    if opcion==3:
        Montovender=float(input("ingrese el monto a vender:"))
        montoCliente=tc.vender(Montovender)
        print("dar ",montoCliente,"en soles")
    if opcion==4:
        pass
        print("gracias hasta luego")
        break

