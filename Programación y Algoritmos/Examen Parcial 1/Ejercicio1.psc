Algoritmo CasaDeCambio
	// Mario Andrés Zaldívar de la Cruz #00586553
	Definir contador, valoractual, valormax, valoracumulado Como Real;
	
	Imprimir "Introduzca el precio del dólar en pesos para cada día de la semana del 23 al 29 de enero.";
	Para contador = 23 Hasta 29
		Imprimir contador," de enero:";
		Leer valoractual;
		
		Si valoractual > valormax Entonces
			valormax = valoractual;
		FinSi
		
		valoracumulado = valoracumulado + valoractual;
	FinPara
	
	Imprimir "Precio promedio: ", valoracumulado/7, " pesos.";
	Imprimir "Precio más alto: ", valormax, " pesos.";
	
	
FinAlgoritmo
