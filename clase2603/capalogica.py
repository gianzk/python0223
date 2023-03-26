from capamodelo import *
import uuid

def consultar(opcion:int):
    match opcion:
        case 1:
            crear_table()
            print("se ejecuto caso 1")
        case 2:
            insertar_data()
            print("se ejecuto caso 2")
        case 3:
            data=mostrar_tabla()
            print("data =>",data)
            print("se ejecuto caso 3")
        case _:
            print("action por default")

