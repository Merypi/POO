class Federados:
    __apellido=""
    __nombre=""
    __dni=""
    __edad=""
    __club=""

    def __init__(self, apellido="", nombre="", dni="", edad="", club=""):
        self.__apellido=apellido
        self.__nombre=nombre
        self.__dni=dni
        self.__edad= edad
        self.__club= club

    def __str__(self) -> str:
        return ("{} {} {} {} {}".format(self.__apellido, self.__nombre, self.__dni, self.__edad, self.__club))
    
    def getAyN(self):
        return self.__apellido +" "+ self.__nombre
    
    def getdni(self):
        return self.__dni
    
    def getedad(self):
        return self.__edad
    
    def getclub(self):
        return self.__club
    def  __eq__(self, otro):
        return self.__dni ==otro.__dni