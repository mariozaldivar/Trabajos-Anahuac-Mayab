Algoritmo DistanciaEntrePuntos
	
	// Mario Andrés Zaldívar de la Cruz
	// El algoritmo le pide al usuario que introduzca las coordenadas, primero x1,y1
	// y luego x2,y2, después de lo cual imprime directamente la distancia de los puntos
	// en el mensaje final utilizando la fórmula de distancia entre dos puntos. 
	
	
	Definir x1,x2, y1, y2 Como Real;
	Escribir "Introduzca la coordenada x1";
	Leer x1;
	Escribir "Introduzca la coordenada y1";
	Leer y1;
	Escribir "Introduzca la coordenada x2";
	Leer x2;
	Escribir "Introduzca la coordenada y2";
	Leer y2;
	
	Escribir "La distancia entre el punto x1,y1 y x2,y2 es de " raiz((x2-x1)^2 + (y2-y1)^2), " unidades.";
	
FinAlgoritmo
