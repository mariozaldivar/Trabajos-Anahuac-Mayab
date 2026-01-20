Algoritmo sin_titulo
	Definir edad Como Entero;
	Definir sexo, siono Como Caracter;
	Definir running como Logico;
	running = Verdadero;
	
	Mientras running
		Mientras Minusculas(sexo) <> "masculino" o Minusculas(sexo) <> "femenino"
			Imprimir "Escriba el sexo (Masculino/Femenino)";
			Leer sexo;
			
		FinMientras
		Imprimir "Escriba su edad";
		Leer edad;
		
		Segun Minusculas(sexo)
			Caso "masculino":
				Imprimir "Su frecuencia ideal mínima para hacer ejercicio es ", 220 - edad * .60, "PPM";
				Imprimir "y frecuencia ideal máxima ", 220 - edad * .75, "PPM";
			Caso "femenino":
				Imprimir "Su frecuencia ideal mínima para hacer ejercicio es ", 226 - edad * .60, "PPM";
				Imprimir "y frecuencia ideal máxima ", 226 - edad * .75, "PPM";
		FinSegun
			
		
		Escribir "¿Desea calcular una vez más?";
		
		
		
		
	FinMientras
FinAlgoritmo
