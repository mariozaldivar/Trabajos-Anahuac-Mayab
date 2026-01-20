Algoritmo Promedio
	Definir calif_acumulada Como Real;
	Definir materias como Real;
	Definir calif_actual como Real;
	Definir contador Como Real;
	
	Escribir "Introduzca la cantidad de materias que requiera promediar";
	Leer materias;
	calif_acumulada = 0;
	Para contador = 1 hasta materias Con Paso 1
		Leer calif_actual;
		calif_acumulada = calif_acumulada + calif_actual;
		
	FinPara
	
	Escribir "Su promedio es de " calif_acumulada/materias;
	
FinAlgoritmo
