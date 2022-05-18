#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  6.py
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

mascarillas = input('Dime cuantas mascarillas vas a comprar \n')
geles = input('Dime cuantos geles vas a comprar \n')

if str(mascarillas.isdigit()) != 'True':
	print(str(mascarillas)+' no es valido como valor de mascarillas')
	exit()
if str(geles.isdigit()) != 'True':
	print(str(geles)+' no es valido como valor de geles')
	exit()

mascarillas = int(mascarillas)
geles = int(geles)

pesomasc = mascarillas * 0.112
pesogel = geles * 0.250

pesototal = pesomasc + pesogel
pesototal =str(pesototal)
geles = str(geles)
mascarillas =str(mascarillas)
print('El numero de mascarillas compradas es de '+mascarillas+' y el numero de geles es de '+geles+' con un peso total de '+pesototal+' kilos')
