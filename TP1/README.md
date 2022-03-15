# TP1 SIA

## Autores

* Justina Vacas Castro
* Josefina Assaff 
* Ian Mejalelaty

## Enunciado

Se busca implementar un generador de soluciones para un rompecabezas de 8 numeros.

## Requisitos

Para poder ejecutuar con exito el programa se necesita installar el siguiente plugin: Colorama 

## Ejecutar

Para ejecutar el programa utulizar el siguiente comando: 

		python3 rompecabeza.py [config file]

## Configuracion

El archivo de configuracion (.json) esta compuesto por los siguientes parametros:

- algoritmo: "BPA", "BPP", "BPPV", "BHL", "BHG", "A*"
- estado_inicial: "(0,1,3,2,4,5,6,7,8)" (se lee el cuadrado de izquierda a derecha)
- limite: valor numerico (en caso de no querer limite poner -1)
- heuristica: "M" (para Manhattan),"H" (para Hamming),"NA" (para el no admisible)
