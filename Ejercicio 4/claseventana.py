class Ventana:
    __Titulo = "Nombre"
    __xSupIzquierda = 0
    __ySupIzquierda = 0
    __xInfDerecha = 500
    __yInfDerecha = 500

    def __init__(self, nombre = "Nombre", xsup = 100, ysup = 100, xinf = 100, yinf = 100):
        self.__Titulo = str(nombre)
        self.__xSupIzquierda = int(xsup)
        self.__ySupIzquierda = int(ysup)
        self.__xInfDerecha = int(xinf)
        self.__yInfDerecha = int(yinf)
    
    def mostrar(self):
        print("Titulo: {}, xSup: {}, ySup: {}, xInf: {}, yInf: {}".format(self.__Titulo,self.__xSupIzquierda,self.__ySupIzquierda,self.__xInfDerecha,self.__yInfDerecha))
    
    def getTitulo(self):
        return self.__Titulo
    
    def alto(self):
        return (self.__yInfDerecha - self.__ySupIzquierda)
    
    def ancho(self):
        return (self.__xInfDerecha - self.__xSupIzquierda)
    
    def moverDerecha(self, desplazamiento = 1):
        if((desplazamiento+self.__xInfDerecha) <= 500 and (desplazamiento+self.__xSupIzquierda) < self.__xInfDerecha):
            self.__xInfDerecha += desplazamiento
            self.__xSupIzquierda += desplazamiento
        else:
            print("Desplazamiento invalido")
    
    def moverIzquierda(self, desplazamiento = 1):
        if((self.__xSupIzquierda-desplazamiento) >= 0 and (self.__xInfDerecha-desplazamiento) > self.__xSupIzquierda):
            self.__xInfDerecha -= desplazamiento
            self.__xSupIzquierda -= desplazamiento
        else:
            print("Desplazamiento invalido")
    
    def bajar(self, desplazamiento = 1):
        if(desplazamiento+self.__yInfDerecha) <= 500 and (desplazamiento+self.__ySupIzquierda) < self.__yInfDerecha:
            self.__yInfDerecha += desplazamiento
            self.__ySupIzquierda += desplazamiento
    
    def subir(self, desplazamiento = 1):
        if(self.__ySupIzquierda-desplazamiento) >=0 and (self.__yInfDerecha - desplazamiento) > self.__ySupIzquierda:
            self.__yInfDerecha -= desplazamiento
            self.__ySupIzquierda -= desplazamiento