import random

# Flotante aleatorio >= 0 y < 1.0
print(random.random())

def numeroRandon(numero:int)->float:
    return random.random()*numero

# 0 -> numero


#
lista_valores = [1,2,3,4, 'hola', 'x']

print(random.choice(lista_valores))