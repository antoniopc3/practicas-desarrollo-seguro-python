#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  3.py
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

patata = '[a-zA-Z0-9]'

entrada = input("Dime que animales hay en el zoo \n")

words = entrada.split('*')

resultado = re.search(patata,entrada)


#if resultado == None:
#	exit()
#else:
for i in words:
	resultado = re.search(patata,i)
	if resultado != None:
		print (i)
