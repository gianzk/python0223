

c=range(4) ## RANGE(START,STOP,STEP) => por default start 0, stop=4, step=1
d=range(10,50,4)### -> 10,14.....46
e=range(0,100,1)### ->0,1,2,3,4,....99
for i in c: ## d,e
    print(i)

## supongamos un sistema

n=int(input("ingrese la cantidad de alumnos:"))
listaAlumnos=list()# []
for i in range(1,n+1):
    nombreAlumno=input("nombre de alumno")
    alumno=(i,nombreAlumno)
    listaAlumnos.append(alumno)

print(listaAlumnos)

### evaluando numeros
# sec=0.0
for i in range(1000):
    print(i)
#sec=0.00001 =>0.00001*10
numero=int(input("identifica que el numero sea primo"))
es_primo=True
for num in range(2, numero):
    if numero % num == 0:
        es_primo=False
        break # 

if es_primo:
    print("el numero es primo")
else:
    print("el numero no es primo")


