#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""script valida"""
import caso.datos as datos

def reglas(dato, campo):
    """ Valida cada uno de los datos ingresados en los diferentes campos """

    if campo == "Carrera" and dato not in datos.carreras:
        return False
    elif campo == "Semestre" and dato < 1:
        return False
    elif campo == "Promedio" and (dato < 0 or dato > 10):
        return False
    elif (campo in ("Nombre", "Primer Apellido") and (dato == "")):
        return False
    elif campo == "Segundo Apellido" and dato == "":
        while True:
            mensaje = "No ha ingresado el segundo apellido. ¿Es correcto? S/N: "
            confirma = input(mensaje)
            if confirma.upper() in ("S", "N"):
                respuesta = True
                if confirma.upper() == "N":
                    respuesta = False
                return respuesta
    else:
        return True
