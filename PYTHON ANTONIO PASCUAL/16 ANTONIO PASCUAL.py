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

longitud = input('De cuanta longitud va a ser la lista \n')
while  str(longitud.isdecimal()) != 'True':
	print('Solo son validos numeros enteros')
	longitud = input('De cuanta longitud va a ser la lista \n')

while len(lista) < int(longitud):
	numero = input('Dime que numero quieres agregar a la lista \n')
	if  numero.isdecimal():
		lista.append(numero)
	if not numero.isdecimal():
		print('solo son validos numeros enteros')
		#numero = input('Dime que numero quieres agregar a la lista otra vez\n')
		
		

v = set(lista)



posicion = input('Dime que valor quieres obtener, por ejemplo si quieres el quinto mayor valor introduce 5, si quieres el octavo mayor valor de la lista introduce 8 \n')
while int(posicion) > len(v):
	print('La posicion de la lista debe ser igual o menor a la longitud de la lista')
	posicion = input('Dime que valor quieres obtener, por ejemplo si quieres el quinto mayor valor introduce 5, si quieres el octavo mayor valor de la lista introduce 8 \n')

while str(posicion.isdecimal()) != 'True':
	print('Recuerda que solo valen introducir numeros positivos')
	posicion = input('Dime que valor quieres obtener, por ejemplo si quieres el quinto mayor valor introduce 5, si quieres el octavo mayor valor de la lista introduce 8 \n' )
	

posi = int(posicion)
posneg = posi * -1

resultado = sorted(v)[posneg]

print('El ' + posicion+'  mayor numero de la lista es '+resultado)

