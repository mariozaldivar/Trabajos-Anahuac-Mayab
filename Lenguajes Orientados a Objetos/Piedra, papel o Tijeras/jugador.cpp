#include "jugador.h"
#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>

using namespace std;

bool Jugador::hacerSeleccion() {
	cout << "Rápidamente, escriba 1, 2 o 3 para hacer su seleccion: \n 1) Piedra \n 2) Papel \n 3) Tijera" << endl; 
	cin >> this->caso;
	this->caso--;
	switch (this->caso) {
		case 0: 
			this->seleccion = "Piedra";
			return true;
			break;
		case 1: 
			this->seleccion = "Papel";
			return true;
			break;
		case 2: 
			this->seleccion = "Tijera";
			return true;
			break;

		default: 
			cout << "La elección no fue válida, perdiste!" << endl; 
			return false;
			break;
	}
}

void Jugador::imprimirJugador() {
	cout << "Este jugador tiene como eleccion: " << this->seleccion << endl;
	
}

void Jugador::seleccionRandom() {
	srand(time(NULL));
	this->caso = rand() % 3;
	switch (this->caso) {
		case 0: 
			this->seleccion = "Piedra";
			break;
		case 1: 
			this->seleccion = "Papel";
			break;
		case 2: 
			this->seleccion = "Tijera";
			break;
	}
}


