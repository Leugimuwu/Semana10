# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:55:25 2022

@author: migue
"""

# Problema: Necesitamos mostrar los nombres de una cadena 
# presenta las primeras letras en mayúscula
# en Word se conoce como Formato Titulo

# Importar la libreria 

import camelcase

nombre="miguel angel yauricasa mendoza"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam

cam=camelcase.CamelCase()
print("Con camelcase.....")

#Imprimimos el nombre en formato titulo
#Utilizamos camelcase

print(cam.hump(nombre))

# Para resolver el problema 
# Creamos otro objeto llamado cam2
# Al definir el objeto, incluimos los argumentos
# 'miguel' y 'yauricasa'

cam2=camelcase.CamelCase('miguel','yauricasa')
print(cam2.hump(nombre))




