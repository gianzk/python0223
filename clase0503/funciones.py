### f(x)=>y / y=x+2

#  declaracion
def my_function():
#body => acciones
    print("esta es mi funcion")
# opcional es el retorno de un valor 
    return 1

my_function() 
variable=my_function()#uso de return
print(variable)

## parametros 
def my_function_with_parameters(nombre):
    print(f"hola mi nombres es {nombre}")

def my_function_with_parametersv2(name):
    return f"Hola mi nombre es {name}"

def my_function_with_parametersv3(name:str,lastname="guti")->str:
    return f"Hola mi nombre es {name} y apellido {lastname}"

nombre_variable=input("ingrese su nombre ")## declarado directo
my_function_with_parameters(nombre_variable)
saludo=my_function_with_parametersv2(nombre_variable)
saludoCompleto=my_function_with_parametersv3(nombre_variable,"crisostomo")
print(saludo)
print(saludoCompleto)


