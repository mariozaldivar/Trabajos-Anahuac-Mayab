Algoritmo TrianguloEsValido
	// Mario Andrés Zaldívar de la Cruz 
	// El algoritmo le pide al usuario que introduzca las longitudes de los lados en cualquier orden,
	// luego valida el triángulo comprobando que ninguna suma de alguno de los lados sea mayor que
	// el tercer lado, y finalmente por medio de varios if-statements anidados, comprueba si los 3
	// lados son iguales, si 2 son iguales, o si todos son diferentes, e imprime un mensaje de acuerdo.
	
	Definir l1, l2, l3 como Real;
	Escribir "Introduzca las longitudes de los lados en el orden que guste";
	Leer l1;
	Leer l2;
	Leer l3;
	
	Si (l1 + l2 < l3) o (l1 + l3 < l2) o (l2 + l3 < l1) 

		Escribir "Error, el triángulo no es válido";
		
	Sino
		Si ( l1 == l2 y l1 == l3) 
			Escribir "El triángulo es equilátero";
		Sino
			Si (l1 == l3 o l1 == l2 o l2 == l3)
				Escribir "El triángulo es isóceles";
				
			Sino
				Escribir "El triángulo es escaleno";
			FinSi
		FinSi
		
		Si (l1^2 + l2 ^2 == l3^2) o (l2^2 + l3 ^2 == l1^2) o (l1^2 + l3^2 == l2^2)
			Escribir "Es un triángulo rectángulo";
			
		SiNo
			Escribir "El triángulo no es rectángulo";
		FinSi
	FinSi
	
	
	
	
FinAlgoritmo
