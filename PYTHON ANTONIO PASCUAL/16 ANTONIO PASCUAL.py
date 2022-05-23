#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  17.py
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


#numeros = input('Dime unos cuantos numeros \n')

#Creamos 2 listas vacias
lista = []

longitud = int(input('De cuanta lonitud va a ser la lista \n'))
if longitud < 9:
	print('La longitud minima es 9')
	exit()

while len(lista) < longitud:
	numero = input('Dime que numero quieres agregar a la lista \n')
	if  str(numero.isdigit()) == 'True':
		lista.append(numero)
	elif str(numero.isdigit()) != 'True':
		print('solo son validos numeros')
		exit()

resultado = sorted(lista)[-9]

print('El enesimo mayor numero de la lista es '+resultado)

