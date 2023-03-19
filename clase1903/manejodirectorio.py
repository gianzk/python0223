import os       # Nos permite manipular el sistema operativo
import shutil   # Nos permite copiar y mover archivos


print( os.getcwd() )

fullpath=os.path.abspath('./directoriodemo')
fullpathFile=os.path.abspath('./demo.png')
print(fullpath)
print(fullpathFile)