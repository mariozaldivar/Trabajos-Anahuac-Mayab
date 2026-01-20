Algoritmo MedidorDeTemperatura
	
	// Mario Andrés Zaldívar de la Cruz 
	// El programa le pide al usuario que introduzca una temperatura en Fahrenheit,
	// la convierte a Celsius usando la fórmula, y luego por medio de if statemets
	// verifica en qué rango se encuentra, para imprmir el mensaje adecuado
	
	Definir temperatura, celsius como Real;
	Escribir "Introduzca la temperatura actual en grados Fahrneheit";
	Leer temperatura;
	
	celsius = (temperatura - 32) * 5/9;
	
	
	Escribir "Dicha temperatura equivale a ", celsius, "°C";
	Si (celsius < 20)
		Escribir "Temperatura no clasificada para hacer ejercicio al aire libre";
	FinSi
	Si (celsius >= 20 y celsius <= 25)
		Escribir "Temperatura ideal para hacer ejercicio al aire libre";
	FinSi
	Si (celsius > 25 y celsius <= 32)
		Escribir "Temperatura peligrosa para hacer ejercicio al aire libre";
	FinSi
	Si (celsius > 32)
		Escribir "Temperatura contraindicada para hacer deporte al aire libre";
	FinSi
	
	
	
	
FinAlgoritmo
