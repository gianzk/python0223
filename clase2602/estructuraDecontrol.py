## tenemos las siguientes formas , if => opcional (else),  if dentro del if(if ) opcional (else)
## tenemos el if ,elif elif elif elif

opciones="""
    1)sumar 2 numeros
    2)Calular mi impuesto
    3) Mostrar si el valor ingresado es par o impar
    4) Adios !
"""
print(opciones)
op=int(input("ingrese una opcion a desarrollar:"))

if type(op) == int:
    #entonces luego hacemos if anidado
    if op==1:
        numero1=int(input("numero1:"))
        numero2=int(input("numero2:"))
        print(numero1+numero2)
    elif op==2:
        impuesto=0.0
        tasa=0
        salario=int(input("ingrese su salario:"))
        if salario<5000:
            tasa=5
        elif salario>=5000 and salario<15000:
            tasa=10
        elif salario>=15000 and salario<35000:
            tasa=15
        else:
            tasa=45
        impuesto=(salario*tasa)/100
        print(f"el valor de tasa es {tasa} y de tu impuesto es {impuesto}")
    elif op==3:
        valor=int(input("ingrese un valor "))
        if valor%2==0:
            print(" es para ")
        else:   
            print("es impar")
    else: 
        print("aun no tenemos esa opcion")
else:
    print("ingrese un valor entero ,valor no permitido")

