Algoritmo Factorial 
	Definir num, contador, resultado como Real;
	Escribir "Introduzca el número del cuál quiere conocer el factorial";
	Leer num;
	
	
	Si num < 0 // Revisa que el número no sea negativo, para descartar aquellos casos
		Escribir "El número no es válido para hacer un factorial";
		
	Sino 
		resultado = 1; // Establece el resultado base como 1, ya que en caso de ser 0, el resultado será 1
		// Y en caso de ser cualquier otro, para que las multiplicaciones den un resultado, 
		// no pueden multiplicarse por 0, y si se multiplican por 1, nada se verá afectado de cualquier manera.
		
		
		Para contador = num hasta 1 con Paso -1; // Se realiza un ciclo que disminuye desde el número introducido
			// hasta 1, y cada uno de esos valores se multiplica por el resultado hasta el momento.
			resultado = resultado * contador;
			
		FinPara
		
		Escribir "El resultado es ", resultado; // Se imrpime el resultado
	FinSi
	
	
FinAlgoritmo
