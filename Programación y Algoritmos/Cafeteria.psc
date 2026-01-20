Algoritmo Cafeteria
	Definir siono como caracter;
	Definir pasteles, cafes, sandwiches, totalprecio, totalpiezas Como Entero;
	
	siono = "s";
	
	Repetir 
		
		Escribir "Introduzca el número de prendas cafés que desea comprar. El costo por pieza es de $25.";
		Leer cafes;
		Escribir "Introduzca el número de prendas sandwiches que desea comprar. El costo por pieza es de $60.";
		Leer sandwiches;
		Escribir "Introduzca el número de pasteles que desea comprar. El costo por pieza es de $40.";
		Leer pasteles;
		
		totalpiezas = cafes + sandwiches + pasteles;
		totalprecio = (cafes * 25) + (sandwiches * 60) + (pasteles * 40);
		
		Si totalprecio > 300
			Escribir "Al hacer una compra con un importe mayor a 300$, usted se hace acreedor a un descuento del 15%";
			Escribir "El precio regular es de $", totalprecio;
			Escribir "Descuento total: $", totalprecio * .15;
			Escribir "El total a pagar es de $", totalprecio * .85;
			
		SiNo
			Si totalpiezas >= 5
				Escribir "Al hacer una compra de más de 5 productos, usted se hace acreedor a un descuento del 10%";
				Escribir "El precio regular es de $", totalprecio;
				Escribir "Descuento total: $", totalprecio * .10;
				Escribir "El total a pagar es de $", totalprecio * .90;
			SiNo
				Escribir "Su total a pagar es de $", totalprecio;
			FinSi
			
			
		FinSi
		
		Repetir 
			Escribir "¿Desea repetir el cálculo? Escriba S para continuar, o N para terminar";
			Leer siono;
			siono = Minusculas(siono);
			
			
			
			
		Mientras Que minusculas(siono) <> "s" y Minusculas(siono) <> "n"
		
		
	Mientras Que siono == "s"
FinAlgoritmo
