#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  14.py
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

cadena = '[A-Za-z0-9]:/#.'

web = input("Dame la pagina \n")

resultado = re.search(cadena,web)

if resultado != None:
	print('Esta pagina no es valida')
	exit()
from urllib import request

pagina=request.urlopen(web)
datos=pagina.read()
datos=str(datos)
datos = len(datos)
print(datos)
