import re

class Email:
    __idCuenta= " "
    __dominio= " "
    __tipodom=" "
    __contraseña=" "

    def __init__(self, idCuenta="", dominio="", tipodom="", contraseña=""):
       self.__idCuenta=idCuenta
       self.__dominio= dominio
       self.__tipodom = tipodom
       self.__contraseña = contraseña
    
    def retornaEmail(self):
        return f"{self.__idCuenta}@{self.__dominio}.{self.__tipodom}"

    def getdominio(self):
        return self.__dominio

    '''  def crearcuenta(self, mail ):
         password=input("ingrese contraseña:")
         self.__contraseña= password
         partes=mail.split("@")
         self.__idCuenta=partes[0]
         dom=partes[1].split(".")
         self.__dominio=dom[0]
         self.__tipodom=dom[1]'''

    def crearcuenta(self, direccionCorreo):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+')
        valido= re.fullmatch(regex, direccionCorreo)
        
        if valido:
            print("Valid email")
            partes = direccionCorreo.split("@")
            self.__idCuenta = partes[0]
            DominioyTipoDominio = partes[1].split(".")
            self.__dominio = DominioyTipoDominio [0]
            self.__tipodom = DominioyTipoDominio [1]
        else:
            print("Invalid email")

        return valido

    def modificarcontraseña(self):
        oldpass=input("ingrese contraseña actual:")
        if oldpass == self.__contraseña:
            newpass=input("ingrese nueva contraseña:")
            self.__contraseña = newpass
            print("se actualizó la contraseña")
        else:
            print("la contraseña es incorrecta")  
