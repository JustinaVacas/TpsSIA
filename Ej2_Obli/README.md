# SIA - Ej1 Optimizacion no lineal 

## Autores

* Justina Vacas Castro
* Josefina Assaff 
* Ian Mejalelaty

## Enunciado

Calcular los valores de W, w y w0 que minimizan el error para los datos de entrada ξ1,ξ2,ξ3, utilizando el metodo del gradiente descendiente, el metodo de gradientes conjugados y el metodo ADAM.

## Requisitos

Para poder ejecutar con exito el programa utilizamos las siguientes librerias: 
    - scipy.optimize
    - qiskit.algorithms.optimizers

## Ejecutar

Para ejecutar el programa utilizar el siguiente comando: 

		python3 main.py 

## Salida

El programa devolvera los siguientes resultados para cada metodo:
    - argumento optimo (W,w,w0)
    - error en el optimo
    - tiempo de ejecucion
    
    Gradiente conjugado
    W =  [6.14978292 7.12182304 7.12182304]
    w = [-2.7609107   0.53929392  2.34593696]
	[-2.7609107   0.53929392  2.34593696]
	w0 =  [0.06283707 0.06283707]
	Error =  4.720788338621333e-06
	Time =  0.0295407772064209
