#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  12.py
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

patata = "[a-zA-Z0-9]"

frase = input('Dime palabras \n')

words = frase.split(' ')

resultado = re.search(patata,frase)



for i in words:
	resultado = re.search(patata,i)
	if resultado == None:
		print('Has introducido un caracter no valido')
		exit()


def contpalabras(frase):
    frase = frase.split()
    palabras = {}
    for i in frase:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def masrepe(palabras):
    palabramas = ''
    apariciones = 0
    for palabra, repe in palabras.items():
        if repe > apariciones:
            palabramas = palabra
            apariciones = repe
    return palabramas, apariciones


print(contpalabras(frase))
print(masrepe(contpalabras(frase)))
