import sys
print(sys.argv)
name=input("este es una entrada de teclado: ")
edad=int(input("dame tu edad"))
message="saludo a desde"
print(message,name)

promedio=int(edad/2)
print(promedio)
#### tipos de salidas
print(message+"mi nombre")
print(message,name)
print(f"la edad es {edad} y el promedio es {promedio}")
print("la edad es {} y el promedio es {}".format(edad,promedio))
## error 
numero=str(2)
message="hola"
print(message+numero)

