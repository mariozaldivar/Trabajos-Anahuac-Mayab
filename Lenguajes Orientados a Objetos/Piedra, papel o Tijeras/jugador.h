#pragma once

#include <string>

using namespace std;

class Jugador {

	public: 

		string seleccion;
		int caso;
		void imprimirJugador(); 
		bool hacerSeleccion();
		void seleccionRandom();
		
	
};
