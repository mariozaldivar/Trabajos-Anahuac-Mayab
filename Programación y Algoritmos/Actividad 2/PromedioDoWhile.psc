Algoritmo PromedioDoWhile
	Definir calif_acumulada Como Real;
	Definir materias como Real;
	Definir calif_actual como Real;
	Definir contador Como Real;
	
	Escribir "Introduzca la cantidad de materias que requiera promediar";
	Leer materias;
	calif_acumulada = 0;
	contador = 0;
	Repetir
		
		Leer calif_actual;
		calif_acumulada = calif_acumulada + calif_actual;
		contador = contador + 1;
		
	Hasta Que contador >= materias
	
	
	Escribir "Su promedio es de " calif_acumulada/materias;
FinAlgoritmo
