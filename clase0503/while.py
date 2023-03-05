#estructuras iterativas
## por que usarlos

listaVaciar=[] ## llenar 100 datos
## es necesario hacer 100 lineas de inputs ?

## esto es un bucle infinito
while False: # con True, cambiamos a false para que no ejecute
    print("ejecutando") 
## detenemos la consola por ctrl +c 

year_init=int(input("año de inicio de reporte"))
year_end=int(input("año de fin de reporte"))
lista_year_not_report=[2008,2009,2010]


while year_init<=year_end:
    if year_init in lista_year_not_report:
     print(f"este año {year_init} no hay reporte")  
    else:
     print(f"el reporte de este año {year_init}")
    year_init+=1# year_init=year_init+1

### palabras break y continue
    ## break rompe el bucle
    ## continue ,ignora todo lo que esta y regresa al punto inicial del bucle

## menu iterativo
print("Bienvenido al menú interactivo")
while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    
    opcion = input() # me devuelve un string ''
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la suma es: {n1+n2}")
    elif opcion =='3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
    


        


