def recursivaSuma(n):
    ##caso base 1
    if n!=1:
        return n+recursivaSuma(n-1)
    else:
        return 1
    
suma=recursivaSuma(100)
print(suma)


#10
##10 + fx(9)
## 10 + 9 +fx(8)
## 10 +9 +8 +fx(7)
## 10 +9+8+ ...........+f(1)
## 10 +9 +8 +......+1

#factorial
#5!=1*2*3*4*5 -> 5!=5*4*3*2*1

def factorial(n):
    if n!=1:
        return n*factorial(n-1)
    else:
        return 1

fact=factorial(5)
print(fact)

""" import os
path=os.path.abspath('..')

for f in os.scandir(path):
    print(f,"=>",f.path)
    print(f.is_dir())

def funcionListCarpeta(path):
    #funcion que me liste el path
    listaCarpeta=[]
    for f in listaCarpeta:
        if f.isDir():
            funcionListCarpeta(f.path)
        else:
            print(f.path)
 """





