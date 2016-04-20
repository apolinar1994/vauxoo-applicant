 #!/usr/bin/python
 # -*- coding: iso-8859-15 -*-
"""
Crear un programa que dada la lista de numeros, obtener la suma del mismo
 """
import os, sys
class CalculatorClass():
   lista = []
   suma = 0
   def llenarlista(self):
       x= int (raw_input("Ingrese Tamaño De La Lista:")) #Ingresar tamanio de la lista
       for i in range(x):
           
           self.lista.append(int(raw_input("Ingrese Numero:")))   #llenar lista
       
       for i in self.lista:#imprimir lista
           print i
 
   def sum(self):
       for i in self.lista:
           self.suma+= i
       print "La Suma De Los Datos Es:",self.suma
 
obj = CalculatorClass()
obj.llenarlista()
obj.sum()
			
