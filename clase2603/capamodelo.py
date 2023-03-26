import sqlite3

conn=sqlite3.connect('demo.db')
#uri conection => uri conection to mysql with python
# sqlalchemy modulo simplifica eso
cur=conn.cursor()

def crear_table():
    cur.execute("CREATE TABLE IF NOT EXISTS USER(id INTERGER,USERNAME TEXT,EMAIL TEXT)")
    conn.commit()

def insertar_data():
    for i in range(10000):
        username='user'+str(i)
        usernamev2=f'user{i}'
        email='user'+str(i)+'@gmail.com'
        cur.execute("insert into user values(?,?,?)",(i,usernamev2,email))
        conn.commit()

def mostrar_tabla():
    data=cur.execute("SELECT * FROM USER").fetchall()
    return data


#####
# leer un archivo con pandas pero desde un vista =>menu iteractivo 
# etl => filtrar un columa
# data source => data load
#reubicar pero pidiendo el nombre archvio output