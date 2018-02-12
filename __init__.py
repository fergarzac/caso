#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Ejemplo de modulos en el curso de Python"""
import caso.altas as altas
import caso.listado as listado
import caso.datos as datos

def principal():
    while True:
        try:
            alumnos = input("Número de alumnos (0 para buscar):")
            alumnos = int(alumnos)
            print()
        except (ValueError) as error:
            print(error)
            continue
        else:
            break
    for contador in range(alumnos):
        print("\nAlumno nuevo", contador + 1)
        datos.alumnos.append(altas.alta())
    if alumnos == 0:
    	buscar=input("Ingresa nombre o apellido:")
    	listado.buscar(buscar)
    else:
    	listado.despliega_todos()