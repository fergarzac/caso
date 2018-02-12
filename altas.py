#! /usr/bin/python3
# -*-coding: utf-8 -*-
import caso.datos as datos
import caso.valida as valida
"""Módulo que contiene la funcion de altas."""
""""""


def alta():
	"""Al invocar esta función manda llamar la función anidada dentro de ella desde el return y le pasa 
	como argumento cada uno de los campos en el orden establecido en objeto llamado orden del archivo datos."""
	def ingresa(campo):
		while True:
			mensaje = "Ingrese " + campo.lower() + ": " 
			dato = input(mensaje)
			if datos.campos[campo] != str:
				try:
					if eval(dato) == datos.campos[campo](dato):
						dato = datos.campos[campo](dato)
					else:
						continue
				except:
					continue
			if valida.reglas(dato, campo):
				return dato
				  
	return {campo: ingresa(campo) for campo in datos.orden}
