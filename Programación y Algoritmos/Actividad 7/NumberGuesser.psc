// Author: Alejandro Cervera Castillo (ID: 00580547)
//
// Teammates: 
//  	* Mario Andres Zaldívar de la Cruz (ID: 00586553)
//
// Description: Command-line number guessing game.

Funcion run_game(max_guesses)
	Definir is_integer_guessed Como Logico
	Definir guessed_integer, random_integer Como Entero
	
	is_integer_guessed <- Falso
	random_integer <- Aleatorio(1, 30)
	
	Definir remaining_guesses Como Entero
	
	remaining_guesses <- max_guesses
	
	Repetir
		// Add a newline to separated each guess prompt.
		Si remaining_guesses < max_guesses
			Imprimir ""
		FinSi
		
		Imprimir "Guess an integer between 1 and 30 (inclusively): "
		Leer guessed_integer
		
		remaining_guesses <- remaining_guesses - 1
		
		Si guessed_integer > random_integer
			Imprimir "Your guess is too high."
		SiNo 
			Si guessed_integer < random_integer
				Imprimir "Your guess is too low."
			SiNo
				Imprimir "Congrats! You guessed the random number (", random_integer, ")."
				is_integer_guessed <- Verdadero
			FinSi 
		FinSi
		
		// Take into account last attempt guesses.
		Si remaining_guesses == 0 Y NO is_integer_guessed
			Imprimir ""
			Imprimir "You exhausted your guess attempts, re-run the program to try again"
			Imprimir "The random integer was: ", random_integer
		FinSi
	Hasta Que guessed_integer == random_integer O remaining_guesses == 0
FinFuncion

Proceso NumberGuesser
	// Variables
	Definir prompt_answer Como Texto
	Definir max_guesses Como Entero
	
	max_guesses <- 4
	
	run_game(max_guesses)
	
	Repetir
		Imprimir ""
		Imprimir "Would you like to play again? [Y/N] "
		
		Leer prompt_answer
		
		Si Mayusculas(prompt_answer) == "Y" O Mayusculas(prompt_answer) == "YES"
			run_game(max_guesses)
		FinSi
	Hasta Que Mayusculas(prompt_answer) == "N" O Mayusculas(prompt_answer) == "NO" 
FinProceso