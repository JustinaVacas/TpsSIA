# TP1 SIA

## Autores

* Justina Vacas Castro
* Josefina Assaff 
* Ian Mejalelaty

## Enunciado

Se busca implementar un generador de soluciones para un rompecabezas de 8 numeros.

## Ejecutar

Para ejecutar el programa utulizar el siguiente comando: 

		python3 rompecabeza.py [config file]

## Configuracion

El archivo de configuracion (.json) esta compuesto por los siguientes parametros:

- algoritmo: "BPA", "BPP", "BPPV", "BHL", "BHG", "AESTRELLA"
- estado_inicial: "(0,1,3,2,4,5,6,7,8)"
- limite: valor numerico
- heuristica: "Manhattan","Hamming","Hamming-edit"
