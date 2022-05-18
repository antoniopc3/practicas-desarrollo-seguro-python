#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  11.py
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


coste = input('Dime el total de la factura \n')
if str(coste.isnumeric()) != 'True':
	print('Solo son validos numeros')
	exit()
coste = float(coste)
iva = input('Dime el % de IVA \n')
if str(iva.isnumeric()) != 'True':
	print('Solo son validos numeros')
	exit()
iva = float(iva)

	
portcost = float(0)
portcost = coste / 100
portiva = float(0)
portiva = portcost * iva
total = float(0)
total = coste + portiva

print(str(total)+' euros es el total de la factura')
