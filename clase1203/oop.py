#introduccion a programacion orientada a objectos

#todos los elementos de python son clases 
a:str="Hola"
b:int=1
c=list() # dado que list tmb es una clase
## creando clases

class Customer:
##atributos y que funcionalidades hace
    id=0
    fullname=""
    dni=""
    productoComprado=""
    fecha=""
    def __init__(self,idParametro,fullnameParametro,dniParametro):
        self.id=idParametro
        self.fullname=fullnameParametro
        self.dni=dniParametro
    def __str__(self) -> str:
        return f"el cliente se llama {self.fullname} con identificador {self.dni}" 
    def verificar(self):
        print("este es el cliente",self.fullname)
    def comprar(self,product):
        self.productoComprado=product
try:
    ismael=Customer(1,'ismael Marin','77877878')
    ismael.comprar("celular")
    print(ismael.productoComprado)
    print("este es el print del objeto ",ismael)
    print(__name__)
except Exception as E:
    print(E)
## describan un clase x sus atributos y metodos
""" class Rectangulo:
     base
     altura
     area

     def getArea():
          return this.Area;
    def  setArea():
         this.area=base*altura """
####objectos dentro de objectos
class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return f'la pelicula {self.titulo} con duracion de {self.duracion}'


class Catalogo:

    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self):
        self.peliculas = []

    def agregar(self, p:Pelicula):  # p será un objeto Pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)

p1=Pelicula('avatar',160,2022)
p2=Pelicula('ant man',120,2023)
p3=Pelicula('avengers',150,2019)

c1=Catalogo()
c1.agregar(p1)
c1.agregar(p2)
c1.agregar(p3)

c1.mostrar()

