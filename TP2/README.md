# TP2 SIA

## Autores

* Justina Vacas Castro
* Josefina Assaff 
* Ian Mejalelaty

## Enunciado

Se busca implementar algoritmos geneticos con diferentes opciones de parametros y metodos y asi comparar los resultados obtenidos.

## Requisitos

Para poder ejecutuar con exito el programa utilizamos las siguientes librerias: 
    - matplotlib.pyplot 
    - random

## Ejecutar

Para ejecutar el programa utulizar el siguiente comando: 

		python3 main.py [config file]

## Configuracion

El archivo de configuracion (.json) esta compuesto por los siguientes parametros:

- generations: cantidad máxima de generaciones (condición de corte por número de generaciones)
- mutation_p: probabilidad de mutación
- mutation_a: intervalo de mutación posible
- crossing_method: "simple", "multiple", "uniform"
- selection_method: "elite", "roulette", "rank", "tournament", "boltzmann", "truncated"
- P: tamaño de población
- random_min: número mínimo para generación de cromosomas
- random_max: número máximo para generación de cromosomas
- points: array de arrays con los valores de entrada (por default: [[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.8830]])
- output: array de los valores de salida por default: [0,1,2]
- accepted_solution: valor de fitness aceptado (condición de corte por valor de fitness)