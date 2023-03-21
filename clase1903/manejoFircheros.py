import os
ruta = os.getcwd()

file_path = os.path.join(ruta,'src','texto.txt')

with open(file_path,mode='r') as f:
    data = f.readlines()
    
    print(data)