class Evaluacion:
    __dni=""
    __estilo=""
    __puntaje=""
    __juez1=0.0
    __juez2=0.0
    __juez3=0.0

    def __init__(self, dni="", estilo="", juez1=0.0, juez2=0.0, juez3=0.0):
        self.__dni=dni
        self.__estilo= estilo
        self.__juez1=float(juez1)
        self.__juez2=float(juez2)
        self.__juez3=float(juez3)

    def __str__(self) -> str:
        return ("{}{}{}{}{}".format(self.__dni, self.__estilo, self.__juez1, self.__juez2, self.__juez3))
    
    def getestilo(self):
        return self.__estilo
    
    def getdni(self):
        return self.__dni
    
    def getPuntajeJueces(self):
        return ("Juez 1:{} \nJuez 2:{} \nJuez3:{}".format(self.__juez1, self.__juez2, self.__juez3))
    
    def __gt__(self, otro):
        prom1 = (otro.__juez1 + otro.__juez2 + otro.__juez3) / 3
        prom = (self.__juez1 + self.__juez2 + self.__juez3) / 3
        return prom > prom1