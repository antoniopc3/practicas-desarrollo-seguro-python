#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  13.py
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

v = [0, 4 , 80, 6, 1, 3, 6, 1, 5, 350]

suma = 0
i = 0
while i < len(v):
	suma += v[i]
	i += 1
media = suma /len(v)
#print ("La media vale ", media)

suma = 0
i = 0
while i < len(v):
	suma += (v[i] - media)**2.0
	i += 1
s = (suma / len(v))**0.5
#print ("Desviacion = ", s)

i=0
while i < len(v):
	resta = v[i] - media
	abajo = resta / s
	if abajo <= -2 or abajo >=2:
		print ( 'El numero con una puntuacion tipica mayor que 2 o menor que -2 es: '+str(v[i]))
	elif abajo >= -2 and abajo <=2:
		print ('No hay numeros con una gran puntuacion tipica') 
	i += 1

print ('La desviacion tipica es igual a  ', s)
print ("La media vale ", media)

#while i < len(v):
#	arriba = v[i] - media
	#abajo = arriba / s
	#i += 1

