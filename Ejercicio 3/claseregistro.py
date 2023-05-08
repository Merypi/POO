class Registro:
    __temperatura=0.0
    __humedad=0.0
    __presion=0

    def __init__(self ,temperatura=0.0 ,humedad=0.0 , presion=0):
        if (type(temperatura)==float)&(type(humedad)==int)&(type(presion)==int):

            self.__temperatura = float(temperatura)
            self.__humedad= int(humedad)
            self.__presion = int(presion)

    def gettemp(self):
        return("{}".format(float(self.__temperatura)))

    def gethum(self):
        return(int(self.__humedad))

    def getpres(self):
        return(int(self.__presion))

    def __str__(self):
        return "%4.2f   %4d    %6d " % (self.__temperatura, self.__humedad,self.__presion)