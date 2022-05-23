#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  1.py
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



nombre = input("Dime tu nombre \n")
if str(nombre.isalpha()) != 'True':
	print('Hay caracteres no validos')
	exit()
apellido1 = input("Dime tu primer apellido \n")
if str(apellido1.isalpha()) != 'True':
	print('Hay caracteres no validos')
	exit()
apellido2 = input("Dime tu segundo apellido \n")
if str(apellido2.isalpha()) != 'True':
	print('Hay caracteres no validos')
	exit()

	
entero= (nombre +' '+ apellido1 +' '+ apellido2)

words = entero.split(' ')
character = ''

for word in words:
	character += word[0]

print (entero.lower())
print(entero.upper())
print(character.upper())
