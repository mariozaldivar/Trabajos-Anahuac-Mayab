Algoritmo sin_titulo
	Definir c1, c2, c3 como Entero;
	Definir P como Real;
	Escribir "Calificación 1:";
	Leer c1;
	Escribir "Calificación 2:";
	Leer c2;
	Escribir "Calificación 3:";
	Leer c3;
	P = (c1 + c2 + c3)/3;
	Si P >= 6 Entonces
		Escribir "Promedio: ", P, " Estudiante Aprobado";
	SiNo
		Escribir "Promedio:", P, " Estudiante reprobado";
	FinSi
FinAlgoritmo
