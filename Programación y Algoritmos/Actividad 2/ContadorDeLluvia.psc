Algoritmo ContadorDeLluvia
	Definir N, contador, cantidadLluvia como Entero;
	Definir debil, moderada, fuerte Como Entero;
	
	Imprimir "Introduzca la cantidad de días";
	Leer N;
	
	Imprimir "Ahora introduzca la cantidad de mm de lluvia en cada uno de esos días";
	
	debil = 0;
	moderada = 0;
	fuerte = 0;
	
	Para contador = 1 hasta N
		Leer cantidadLluvia;
		
		Si cantidadLluvia <= 2 Entonces
			debil = debil + 1;
			
		FinSi
		Si cantidadLluvia > 2 Entonces
			moderada = moderada + 1;
			
		FinSi
		Si cantidadLluvia > 15 Entonces
			moderada = moderada + 1;
			
		FinSi
		
	FinPara
	
	Imprimir "Hubo lluvia débil ", debil, " días, moderada ", moderada, " días, y fuerte ", fuerte, " días";
	
FinAlgoritmo
