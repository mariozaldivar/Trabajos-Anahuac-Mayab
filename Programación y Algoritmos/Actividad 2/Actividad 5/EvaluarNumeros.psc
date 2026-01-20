Algoritmo EvaluarNumeros
	Definir cantidad, mas_grande, acumulado, pares, impares, num, n como Real;
	
	// Define todas las variables que se usarán
	
	acumulado = 0;
	pares = 0;
	impares = 0;
	
	
	Imprimir "Introduzca la cantidad de número que quiere evaluar";
	Leer cantidad;
	// El usuario introduce la cantidad de números que quiere tratar
	
	Imprimir "Ahora introduzca los números en el orden que guste";
	
	Para n = 1 hasta cantidad // Se utiliza un loop que cicla por cada número que quiera introducir
		Leer num; // Lee cada número individualmente
		Si num % 2 == 0 // Operador para comprobar si el número es par o no
			// Según el resultado, le suma al contador de pares o impares en las variables
			pares = pares + 1;
		Sino 
			impares = impares + 1;
		FinSi
		
		acumulado = acumulado + num; // Añade el número a la suma total para hacer el promedio al final
		
		Si num > mas_grande
			mas_grande = num; // Revisa si el número actual es más grande que el último más grande
			// En caso de si ser, cambia la variable al valor del número actual
		FinSi
	FinPara
	
	Imprimir "En las cantidades introducidas hubo ", pares, " números pares, y ", impares, " números impares"; 
	Imprimir "El promedio es ", acumulado/cantidad, ", y el número más grande visto fue ", mas_grande, ".";
	
	// Imprime las cantidades de pares e impares obtenidas
	// Calcula el promedio directamente al imprimirlo, e imprime el número más grande almacenado en la variable
	
FinAlgoritmo
