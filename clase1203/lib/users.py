from lib.horario import Turno

class Doctores:
    id:int
    fullname:str 
    horario:list
    especialidad:str
    pass
    def __init__(self,id,fullname,especialidad):
        self.id=id
        self.fullname=fullname
        self.especialidad=especialidad
    def agregarTurno(self,dia,hora_inicio,hora_fin):
        turno=Turno(dia,hora_inicio,hora_fin)
        ## validar que no se cruce las horas
        self.horario.append(turno)
        self.horario.sort()
    def mostrarHorario(self):
        for i,j in enumerate(self.horarios):
            print(i,"=>",j)
#### agrupar a los doctores

class Pacientes:
    id:int
    fullname:str
    citas:list
    solicitud:dict
    def __init__(self,id,fullname):
        self.id=id
        self.fullname=fullname
    def enviarSolicitud(self,especialidad,turno:Turno):
        self.solicitud={
            "especialidad":especialidad,
            "turno":turno
        }

