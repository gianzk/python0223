def saludar(name):
    print(__name__,"name in lib")
    print(f"Hola,soy {name} te estoy saludando desde la función saludar() " \
            "del módulo saludos")


def sumar(numero1,numero2):
    print(numero1+numero2)

saludar("dentro")