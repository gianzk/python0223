## for

lista=[None,1,2,3,4,5,[1221,21321]]
edad=20
## estructura de for 
for variable in lista: # lista->estructura iterable
    if type(variable):
        print(variable,"=>",type(variable))
    if type(variable)==list:
        for variable2 in variable:
            print("this =>",variable2)

for index,valor in enumerate(lista):
    print(index,valor,"2do bucle")
    if index!=0 and index%2!=0:
        print('entre en la condicion')