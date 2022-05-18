#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  5.py
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


numero1 = input('Dime un numero \n')
numero2 = input('¿Entre que numero quieres dividir el numero anterior? \n')

if str(numero1.isdigit()) != 'True':
	print(str(numero1)+' no es un numero valido')
	exit()
if str(numero2.isdigit()) != 'True':
	print(str(numero2)+' no es un numero valido')
	exit()
	

numero1 = int(numero1)
numero2 = int(numero2)

cociente = numero1 / numero2
resto = numero1 % numero2
numero1 = str(numero1)
numero2 = str(numero2)
resto = str(resto)
cociente = str(cociente)
print (numero1+' entre '+numero2+' da un cociente '+cociente+' y un resto '+resto)
