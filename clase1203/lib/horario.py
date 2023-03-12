from datetime import date,datetime,time

class Turno:
    dia:str # dias del 1 al 30
    hora_inicio:int # 0 <>24 horas
    hora_fin:int #0 <> 24 horas
    def __init__(self,dia,hora_inicio,hora_fin):
        self.dia=dia
        self.hora_inicio=hora_inicio
        self.hora_fin=hora_fin

    def format(self):
        return f"{self.dia}-{self.hora_inicio}-{self.hora_fin}"

    
    