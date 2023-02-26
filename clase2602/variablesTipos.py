### variables 
### recomendaciones no iniciar con numeros
## sin espacios ni caracteres especiales
message="hola"
edad=20
message_de_saludo=" hola "

## tipos de datos
entero=21
flotante=3.14
unValorLogico=True
unacadenadetexto="cadena de texto"
### cadena de texto multilineas 3 comillas
literalCadena="""
    Hola como 
    estas 
    sigo sin error 
"""
## carateres de escape \t-> tabulacion \n  ->separacion de linea

cadenaSaludo="Hola"
persona="Gianmarco"
saludoPersonalizado=cadenaSaludo+persona
print(saludoPersonalizado)
print("linea de comparacion")
print(cadenaSaludo,persona)
# cantidad de caratecteres de una cadena
sizeCadena=len(saludoPersonalizado)
print(len(saludoPersonalizado))
print("linea de comparacion")
print(sizeCadena)
print("linea de comparacion")
print(type(flotante))
print(type(saludoPersonalizado))
print(type(flotante)==float) # comparacion de tipos , para los otros serian str, int ,...
# int() -> convierte otro tipo de dato a entero
edad2="3"
print(edad2,"=>",type(edad2))
print("linea de comparacion")
edadInt=int(edad2)
print(edadInt,"=>",type(edadInt))
a=3
b=3

c=(a==b)
print("este es booleano","=>",c)
