class Conjunto:
    __conjunt=[]
     
    def __init__(self, l):
        self.__conjunt=l
        
    def __str__(self):
        return ("{}".format(self.__conjunt))

    def getconj(self):
        return(self.__conjunt)
    
    def __add__(self, otro):
        newconjunto=[]
        if(type(self)==type(otro)):
            a=set(self.getconj())
            b=set(otro.getconj())
            c=a|b  
        else: print("Error")
        return(list(c))
        
    def __sub__(self, otro):
        
        if(type(self)==type(otro)):
            a=set(self.getconj())
            b=set(otro.getconj())
            c=a&b  
        else: print("Error")
        return(list(a-c))

    def __eq__(self, otro):
        igual=True
        if len(self.__conjunt)==len(otro.getconj()):
            otroconj=otro.getconj()
            for numero in otroconj:
                if not numero in self.__conjunt:
                    #print("Elemento distinto") 
                    igual=False
        else: igual=False
        return igual
    
    ''' def __init__(self):
        self.__lista= []

    def getconjunto(self):
        return self.__lista[:]
    
    def __add__(self, otro):
        adicion=otro.getConjunto()
        for numero in self.__lista:
            if numero not in adicion:
                adicion.append(numero)
        return Conjunto(adicion)'''
    
    