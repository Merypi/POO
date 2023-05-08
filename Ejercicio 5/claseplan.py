class Plan_Ahorro:
    __codigo=0
    __modelo=""
    __version=""
    __valor=0 
    __cant_cuotas=0 #mismo valor para todos los planes
    __cuotas_pagas= 0 #mismo valor para todos los planes
    def __init__(self, codigo=0, modelo= "", version="", valor=0, cuotas:int=0, cuotas_pagas=0):
        self.__codigo=codigo
        self.__modelo= modelo
        self.__version= version
        self.__valor= int(valor)
        self.__cant_cuotas= int(cuotas)
        self.__cuotas_pagas= int(cuotas_pagas)

    def __str__(self) -> str:
        return ("{} {} {} {} {} {}".format(self.__codigo, self.__modelo, self.__version, self.__valor ,self.__cant_cuotas, self.__cuotas_pagas))

    def getcodigo(self):
        return self.__codigo
    
    def getmodelo(self):
        return self.__modelo
    
    def getversion(self):
        return self.__version
    
    def getvalor(self):
        return self.__valor
    
    def getcuotas(self):
        return self.__cant_cuotas
    
    def cant_licitar(self):
        return self.__cuotas_pagas
    
    def mostrar(self):
        print("Codigo de plan:{}\nModelo:{}\nVersion:{}".format(self.__codigo, self.__modelo, self.__version))
    
    def modificar_valor(self, new):
        self.__valor = new
    
    def valorcuota(self):
        #valor cuota = (importe vehículo/cantidad de cuotas) + importe vehículo * 0.10
        return (self.__valor / self.__cant_cuotas) + self.__valor * 0.10
    
    def modificar(self, nuevo):
        self.__cuotas_pagas = nuevo