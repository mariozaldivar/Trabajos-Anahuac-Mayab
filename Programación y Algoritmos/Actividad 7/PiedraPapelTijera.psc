Algoritmo PiedraPapelTijera
	Definir seleccion, opciones, siono Como Caracter;
	Definir jugada_computadora, ganadas, perdidas, empates Como Entero;
	Definir jugando Como Logico;
	
// Alejandro Cervera y Mario Zaldívar

	Dimension opciones[3];
	
	opciones[0] = "piedra";
	opciones[1] = "papel";
	opciones[2] = "tijeras";
	ganadas = 0;
	perdidas = 0;
	empates = 0;
	
	// Declara todas las variables necesarias, y declara un Array con todas las posbiles 
	// opciones para que la computadora juegue
	
	Escribir "Bienvenido a piedra, papel o tijera. Cuando esté listo para empezar presione enter";
	Esperar Tecla;
	jugando = Verdadero;
	
	// Espera a una acción del jugador para empezar el juego
	
	Escribir "Prepárese para jugar. A la cuenta de 3, escriba su elección lo más rápido posible. Debes escribir piedra, papel o tijeras.";
	
	Repetir
		Escribir "3...";
		Esperar 1 segundo;
		Escribir "2...";
		Esperar 1 segundo;
		Escribir "1...";
		Esperar 1 segundo;
		Escribir "AHORA";
		Leer seleccion;
		
		// Hace una cuenta regresiva y lee el input del usuario
		
		jugada_computadora = Aleatorio(0,2); // Calcula un número aleatorio, que será el index
		// de la jugada en la lista
		
		
		Según Minusculas(seleccion) // Utiliza un gran switch statement para leer todos los casos
		// posibles, y determinar cuál es el resultado en cada uno.
	Caso "tijera":
		Segun opciones[jugada_computadora]
			Caso "tijeras":
				Escribir "La computadora juega tijeras, es un empate";
				empates = empates + 1;
				
			Caso "piedra":
				Escribir "La computadora juega piedra, perdiste";
				perdidas = perdidas + 1;
			Caso "papel":
				Escribir "La computadora juega papel, ganaste";
				ganadas = ganadas + 1;
		FinSegun
	Caso "tijeras":
		Segun opciones[jugada_computadora]
			Caso "tijeras":
				Escribir "La computadora juega tijeras, es un empate";
				empates = empates + 1;
			Caso "piedra":
				Escribir "La computadora juega piedra, perdiste";
				perdidas = perdidas + 1;
			Caso "papel":
				Escribir "La computadora juega papel, ganaste";
				ganadas = ganadas + 1;
		FinSegun
	Caso "piedra":
		Segun opciones[jugada_computadora]
			Caso "tijeras":
				Escribir "La computadora juega tijeras, ganaste";
				ganadas = ganadas + 1;
			Caso "piedra":
				Escribir "La computadora juega piedra, es un empate";
				empates = empates + 1;
			Caso "papel":
				Escribir "La computadora juega papel, perdiste";
				perdidas = perdidas + 1;
		FinSegun
		
	Caso "papel":
		Segun opciones[jugada_computadora]
			Caso "tijeras":
				Escribir "La computadora juega tijeras, perdiste";
				perdidas = perdidas + 1;
			Caso "piedra":
				Escribir "La computadora juega piedra, ganaste";
				ganadas = ganadas + 1;
			Caso "papel":
				Escribir "La computadora juega papel, es un empate";
				empates = empates + 1;
				
			
		FinSegun
		
	De Otro Modo:
		Escribir "Jugada inválida, perdiste";
		
		

FinSegun


siono = "";
Mientras no (Minusculas(siono) == "n" o Minusculas(siono) == "s") // Empieza un loop para
	// Pedirle al jugador que elija si sigue jugando o no. No se detiene hasta que elija una
	// opción válida.
	Escribir "¿Le gustaría seguir jugando? Escriba S para si, o N para no";
	Leer siono;
	Si Minusculas(siono) == "n" // Si la opción es "n", cambia la variable jugando a Falso,
		// lo cual provoca que el loop termine al llegar al final.
		jugando = Falso;
	FinSi
FinMientras


		
	Mientras Que jugando = verdadero // Mantiene el loop mientras jugando sea verdadero.
	
	Escribir "Al final se jugaron ", (perdidas + ganadas + empates), " partidas, ganaste ", ganadas, ", perdiste ", perdidas, " y empataste ", empates, ".";
FinAlgoritmo
