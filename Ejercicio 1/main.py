# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:16:55 2023

"""
from ClaseEmail import Email
import csv

def crearcorreo ():
    print("--Carga de datos--")
    name=input("ingrese nombre:")
    dominio=input("ingrese dominio:")
    tipo_dominio=input("ingrese tipo:")
    contra=input("ingrese cantraseña")
    unemail=Email(name, dominio, tipo_dominio, contra)
    print('Estimado', name, 'le enviaremos sus mensajes a la direccion:', unemail.retornaEmail()) 
    return unemail

def readfile():
    archivo=open("mail.csv")
    reader=csv.reader(archivo,delimiter=',')
    lista=[]
    for fila in reader:
        if '@' in fila and '.' in fila:
            otromail = Email() 
            if otromail.crearcuenta(fila) != None:
                lista.append(otromail)
                print("Cuenta creada")
        else:
            print("Direccion no valida:{}".format(fila))
    return lista


if __name__ == '__main__':
    '''email= crearcorreo()
    email.modificarcontraseña()     
    cuenta=Email() 
    mail=input("ingrese correo para crear cuenta:")
    cuenta.crearcuenta(mail)'''
    mail_archivo=readfile()
    dom=input("ingrese dominio para conocer su cantidad:")
    c=0
    for mail in mail_archivo:
        #Buscar el dominio en el contenedor del mail
        if dom in mail:
            c+=1
            print("Coincidencia de dominio")
    print("Se han encontrado {} emails con el dominio buscado".format(c))
    



        
    

        
    
    