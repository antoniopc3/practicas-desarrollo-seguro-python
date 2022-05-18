#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  15.py
#  
#  Copyright 2022 apcuenca <apcuenca@11LAP5CG8452LZY>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import re

pregunta = input('Si quieres buscar pulsa la b, si quieres insertar un nuevo numero de telefono, pulsa la i \n')

cadena ="[bi]"

resultado = re.search(cadena,pregunta)

if resultado == None:
	print('Has introducido un caracter no valido')
	exit()








if str(pregunta) == 'i':
	from pathlib import Path

	fileName = r"listin.txt"
	fileObj = Path(fileName)
	fileObj.is_file()
	resultado = fileObj.is_file()
	resultado = str(resultado)

	if resultado == 'False':
		import os
		archi1=open("listin.txt","w")
		print('El archivo no existia,lo acabas de crear')
		#numnom = input('Dime el numero en primer lugar y el nombre en segundo lugar, separados por una coma \n')
		numero = input('Dime el telefono \n')
		if str(numero.isnumeric()) != 'True':
			print('Solo son validos numeros')
			exit()
		nombre = input('Dime el nombre \n')
		if str(nombre.isalpha()) != 'True':
			print('Solo son validas letras')
			exit()
	
		numnom = str(numero)+','+str(nombre)
		archi1.write(numnom)
		archi1.close()
	else:
		import os
		archi1=open("listin.txt","a")
		print('El archivo ya existia,vas a escribir sobre el')
		#numnom = input('Dime el numero en primer lugar y el nombre en segundo lugar, separados por una coma \n')
		numero = input('Dime el telefono \n')
		if str(numero.isnumeric()) != 'True':
			print('Solo son validos numeros')
			exit()
		nombre = input('Dime el nombre \n')
		if str(nombre.isalpha()) != 'True':
			print('Solo son validas letras')
			exit()
		numnom = str(numero)+','+str(nombre)
		archi1.write(str(numnom)+'\n')
		archi1.close()
#archivo = open("listin.txt")
#linea=archivo.readline()
#while linea != '':
#	linea=archivo.readline()
#	print(linea)
elif str(pregunta) == 'b':
	busqueda = input('Dime que telefono buscas \n')
	if str(busqueda.isnumeric()) != 'True':
		print('Solo son validos numeros')
		exit()
	with open("listin.txt","r") as archivo:
		if busqueda  in archivo.read():
			print('este numero existe')
		else:
			print('Este numero no existe')
		
		
#f = open("archivo.txt", "r")
#while(True):
#    linea = f.readline()
#   print(linea)
#  if not linea:
#        break
#f.close()
	
