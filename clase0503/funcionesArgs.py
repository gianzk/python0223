import sys

variable=sys.argv
def my_path_function(*args):
    print(type(args))

my_path_function(variable)
#my_path_function(5,"Hola",[1,2,3,4,5],{'dia':'sabado'})
def indeterminados_nombre(**kwargs):
    print(kwargs)
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

indeterminados_nombre(cantidad=5, saludo="Hola", lista=[1,2,3,4,5])   