Algoritmo TablaDeMultiplicar
	Definir num, n como Entero; // Declara num (el número a multiplicar) y n (el contador para el for loop)
	
	Escribir "Introduzca el número del cual quiera conocer la tabla";
	Leer num;
	
	Para n = 1 hasta 10 // Utiliza n como el contador, que aumentará del 1 al 10 progresivamente
		Escribir num, " x ", n, " = ", num * n; // Imprime el resutlado de la multiplicación de n y num
		// Con cada ciclo, n aumenta acorde a la tabla de multiplicar, multiplicando oportunamente a num
		// El resultado se imprime en una string concatenada con un formato legible. 
	FinPara
	
	
FinAlgoritmo
