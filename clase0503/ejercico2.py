
##flujo de compra de un producto
producto={
    'name':"celular",
    'precio':"1000",
    'stock':500,
    'promo':True,
    'maxDescuento':10
}

def buscarProducto(name,variable):
    if producto['name']==name:
        return [producto,variable]
    else:
        return False
    
def verificarStock(product:dict)->int:
    if product['stock']:
        return product['stock']

def main():
    ##buscas el producto y ves sus caracteristicas
    nameproducto=input('nombre del producto')
    my_product=dict()
    if buscarProducto(nameproducto):
        my_product=buscarProducto(nameproducto)
    else:
        print("no existe el producto")
    ## verifica el stock
    if verificarStock(my_product):
        print(f"mi stock es {verificarStock(my_product)}")
    else:
        print("no hay stock")
    ## tiene promocion o no tiene promcion
    ## precio final


main()