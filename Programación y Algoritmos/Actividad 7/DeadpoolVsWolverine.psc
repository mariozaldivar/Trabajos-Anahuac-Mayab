Algoritmo DeadpoolVsWolverine
	// Alejandro Cervera y Mario Zaldívar
	
	
	Definir salud_deadpool, salud_wolverine, turno, anterior, daño Como Entero;
	Definir simulando Como Logico;
	Definir seguir como Caracter;
	
	simulando = Verdadero;
	seguir = "";
	
	
	Mientras simulando
		
		
		turno = 1;
		Escribir "Escribe la vida inicial para Deadpool";
		Leer salud_deadpool;
		Escribir "Escribe la vida inicial para Wolverine";
		Leer salud_wolverine;
		
		// Lee la salud que el jugador introduce para ambos personajes
		anterior = 0;
		
		Mientras (salud_deadpool > 0) y (salud_wolverine > 0) // Crea un loop que sigue mientras ambos peleadores sigan vivos.
			
			
			Imprimir "Turno ", turno;
			Si anterior <> 100 // Revisa que Wolverine pueda atacar.
				daño = Aleatorio(10, 120); // Genera el daño
				
				anterior = daño; // Almacena el daño que provocó Wolverine, para saber si Deadpool podrá atacar el siguiente turno
				salud_deadpool = salud_deadpool - daño; // Resta la salud
				Escribir "Wolverine ataca a Deadpool con ", daño, " de daño.";
				Si salud_deadpool <= 0 // Revisa si Deadpool sigue vivo.
					Escribir "Deadpool se ha quedado sin puntos de vida";
					Escribir "¡Wolverine gana la batalla con ", salud_wolverine, " puntos de salud restantes!";
				Sino
					Escribir "Salud restante de Deadpool: ", salud_deadpool;
				FinSi
				
				
			SiNo
				Escribir "Wolverine recibió demasiado daño el turno anterior y necesita recuperarse";
				
			FinSi
			
			Si (salud_deadpool > 0) // Revisa si Deadpool sigue vivo antes de llevar a cabo la lógica
				Si anterior <> 120 // Revisa que Deadpool pueda atacar
					daño = Aleatorio(10, 100);
					Escribir "Deadpool ataca a Wolverine con ", daño, " de daño.";
					
					anterior = daño;
					salud_wolverine = salud_wolverine - daño; 
					
					Si salud_wolverine <= 0
						Escribir "Wolverine se ha quedado sin puntos de vida";
						Escribir "¡Deadpool gana la batalla con ", salud_deadpool, " puntos de salud restantes!";
					Sino
						Escribir "Salud restante de Wolverine: ", salud_wolverine;
					FinSi
					
					
				Sino 
					Escribir "Deadpool recibió demasiado daño el turno anterior y necesita recuperarse";
				FinSi
				
			FinSi
			
			turno = turno + 1;
			Escribir "";
			Esperar 1 segundo;
		
		FinMientras
		Imprimir "¿Desea simular otra pelea? Escriba S para si y N para no";
		Leer seguir;
		Mientras no (minusculas(seguir)== "n") y no (minusculas(seguir) == "s")
			Imprimir "Respuesta no válida, por favor escriba S o N";
			Leer seguir;
			
			
		FinMientras
		
		Si minusculas(seguir) == "n"
			simulando = Falso;
		FinSi
		
	FinMientras
	
	
	

	
FinAlgoritmo
