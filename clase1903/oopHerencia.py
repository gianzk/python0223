class Persona:
    def __init__(self,fullname,tipoDocumento,nroDocumento):
        self.fullname=fullname
        self.tipoDocumento=tipoDocumento
        self.nroDocumento=nroDocumento

    def __str__(self):
        return f"la persona {self.fullname} con {self.tipoDocumento} y numero {self.nroDocumento}"

    def update(self):
        print("puede actualizar su info")

## cliente ,asesor ,admin

class Cliente(Persona):
    def __init__(self,fullname,tipoDocumento,nroDocumento):
        Persona.__init__(self,fullname,tipoDocumento,nroDocumento)
        #super().__init__(fullname,tipoDocumento,nroDocumento)

class Asesor(Persona):
    def __init__(self,fullname,tipoDocumento,nrDocumento):
       # Persona.__init__(fullname,tipoDocumento,nrDocumento)
        super().__init__(fullname,tipoDocumento,nrDocumento)

p1= Persona('gianmarco','dni','77534646')
a2= Cliente('gianmarcoClient','ruc','77534646')
a1= Asesor('gianmarcoAsesor','dni','717534646')

a2.update()
print(a2)
print(a1)