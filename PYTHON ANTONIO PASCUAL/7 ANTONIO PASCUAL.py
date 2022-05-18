#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  7.py
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


nota = input('¿Que nota le das al producto? Debes darle una nota de 0, 0.2, 0.4, 0.6, 0.8 o 1, siendo 0 lo mas bajo y 1 lo mas alto \n')

#if (str(nota.isnumeric())) != 'True':
#	print('numero no valido')
#	exit()


nota = float(nota)
multiplicador = float(1.5)
notfinal = float(0)
if nota == 0.0:
	nota = str(nota)
	print ('El producto tiene una nota de '+nota+'  y un nivel de mal producto')
elif nota == 0.2:
	notfinal = nota * multiplicador
	notfinal = str(notfinal)
	print ('El producto tiene una nota de '+notfinal+'  y un nivel de aceptable')
elif nota == 0.4:
	notfinal = nota * multiplicador
	notfinal = str(notfinal)
	print ('El producto tiene una nota de '+notfinal+'  y un nivel de aceptable')
elif nota == 0.6 or nota == 0.8 or nota == 1:
	notfinal = nota * multiplicador
	notfinal = str(notfinal)
	print ('El producto tiene una nota de '+notfinal+'  y un nivel de reseñable')
else:
	print('Numero no valido')
