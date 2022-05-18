#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  2.py
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

prefijo = input("Dime el prefijo \n")
if prefijo[0] != '+' :
	print('Caracter no valido')
	exit()
if len(prefijo) == 3 :
	print ('Longitud correcta')
elif len(prefijo) !=3:
	print ('Longitud incorrecta')
	exit()

numero = input("Dime el numero \n")
if len(numero) == 9 and str(numero.isdigit()) == 'True':
		print('Numero de longitud y caracteres correcto')
elif len(numero) ==9 and str(numero.isdigit()) != 'True':
		print('Numero de longitud correcto y caracteres no validos')
		exit()
elif len(numero) !=9 and str(numero.isdigit()) == 'True':
		print('Numero de longitud incorrecto y caracteres  validos')
		exit()
elif len(numero) != 9 and str(numero.isdigit()) != 'True':
		print('Numero de longitud y caracteres incorrecto')
		exit()
		 

extension = input ("Dime la extension \n")
if len(extension) >=3 and len(extension) <=4 and str(extension.isdigit()) =='True':
	print('Longitud y caracteres correctos')
else:
	print('datos no validos, intentalo otra vez')
	exit()

numcomple = (prefijo+'-'+numero+'-'+extension)
words = numcomple.split('-')
numerofin = words[1]
prefi = int(numerofin[0:3])

#ANDALUCIA
if prefi >=950 and prefi <=959:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Andalucia")
#ARAGON
elif prefi >=974 and prefi <=978:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Aragon")
#ASTURIAS
elif prefi==984 or prefi==985:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Asturias")
#BALEARES
elif prefi==871:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a  Baleares")
#CANARIAS
elif prefi==922 or prefi==928:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Canarias")
#CANTABRIA
elif prefi==942:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Cantabria")
#CASTILLA LA MANCHA
elif prefi==925 or prefi==926 or prefi==949 or prefi==967 or prefi==969:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Castilla La Mancha")
#CASTILLA LEON
elif prefi==921 or prefi==923 or prefi==947 or prefi==975 or prefi==979 or prefi==980 or prefi==983 or prefi==987:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Castilla y Leon")
#CATALUÑA
elif prefi>=931 and prefi<=937 or prefi==972 or prefi==973 or prefi==977:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Cataluña")
#EXTREMADURA
elif prefi==924 or prefi==927:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Extremadura")
#GALICIA
elif prefi==981 or prefi==982 or prefi==986 or prefi==988:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Galicia")
#RIOJA
elif prefi==941:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a La Rioja")
#MADRID
elif prefi>=911 and prefi<=918:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Madrid")
#MURCIA
elif prefi==968:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Murcia")
#NAVARRA
elif prefi==948:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Navarra")
#PAIS VASCO
elif prefi==943 or prefi==945:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Pais Vasco")
#VALENCIA
elif prefi==960 or prefi==965 or prefi==966:
	prefi1 = str(prefi)
	print ("El prefijo "+prefi1+" pertenece a Comunidad Valenciana")
