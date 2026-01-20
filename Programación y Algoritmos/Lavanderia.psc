Algoritmo Lavanderia
	Definir siono como caracter;
	Definir tipo1, tipo2, totalprendas, totalprecio Como Entero;
	
	siono = "s";
	
	Repetir 
		
		Escribir "Introduzca el número de prendas tipo 1 (camisas, blusas). El costo por prenda es de $55.";
		Leer tipo1;
		Escribir "Introduzca el número de prendas tipo 2 (faldas, pantalones). El costo por prenda es de $75.";
		Leer tipo2;
		
		totalprendas = tipo1 + tipo2;
		totalprecio = (tipo1 * 55) + (tipo2 * 75);
		
		Si totalprendas >= 5
			Escribir "Al entregar al menos 5 prendas, usted se hace acreedor a un descuento del 15%";
			Escribir "Descuento total: $", totalprecio * .15;
			Escribir "El total a pagar es de $", totalprecio * .85;
			
		SiNo
			
		Escribir "Su total a pagar es de $", totalprecio;
			
		FinSi
		
		Repetir 
			Escribir "¿Desea repetir el cálculo? Escriba S para continuar, o N para terminar";
			Leer siono;
			siono = Minusculas(siono);
			
		
			
			
		Mientras Que minusculas(siono) <> "s" y Minusculas(siono) <> "n"
			
		
	Mientras Que siono == "s"
	
FinAlgoritmo
