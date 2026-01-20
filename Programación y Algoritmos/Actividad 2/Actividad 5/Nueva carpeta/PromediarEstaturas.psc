Algoritmo PromediarEstaturas
	Definir estatura, acumulado, contador como Real;
	Definir altotes Como Logico;
	
	
	Imprimir "Introduzca una estatura en metros. Para terminar el programa, introduzca una estatura igual o menor a cero";
	Repetir
		Leer estatura; 
		
		Si estatura > 0 // Revisa que la estatura sea válida, y si si es, añade a un contador y a un acumulado
			// Ambos se usarán para el promedio al final
			contador = contador + 1; 
			acumulado = acumulado + estatura;
			
		FinSi
		
		Si estatura > 1.80 // Revisa si alguna estatura es mayor a 1.80
			altotes = Verdadero; // En caso de haber, cambia la variable altotes a verdadero para indicar que existen.
		FinSi
		
		
	Mientras Que estatura > 0 // Condición que revisa que la estatura introducida sea válida, si no, termina el ciclo
	
	Si acumulado > 0 Entonces
		Escribir "El promedio de estatura es de ", acumulado/contador, " metros"; 
		Si altotes == Verdadero
			Escribir "Entre ese grupo hay al menos un altote de más de 1.80";
		FinSi
	Sino 
		Escribir "No introdujiste ninguna estatura válida";
		
		// Calcula el promedio con las variables y escribe el resultado directamente.
	FinSi
	
FinAlgoritmo
