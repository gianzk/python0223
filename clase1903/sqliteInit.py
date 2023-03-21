import sqlite3


con = sqlite3.connect("tutorial.db")
sta=con.cursor()

sta.execute("create table client(nombre,dni)")

