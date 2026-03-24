#include "jugador.h"
#include <iostream> 

using namespace std; 

Jugador jugador1;
Jugador jugador2;
int ronda = 0;
bool running = true;

void verificarGanador(Jugador j1, Jugador j2) {
	int resultado = (j1.caso - j2.caso + 3) % 3;
	if (resultado == 0) {cout << "Es un empate! La eleccion de tu oponente fue: " << j2.seleccion << endl;}
	else if(resultado == 1) {cout << "Ganaste! La elección de tu oponente fue: " << j2.seleccion << endl;}
	else if(resultado == 2) {cout << "Perdiste! La eleccion de tu oponente fue: " << j2.seleccion << endl;}

}

void jugar() {
	ronda++;
	cout << "Ronda " << ronda << ":";

	if (jugador1.hacerSeleccion() == false) {cout << "Tu eleccion no fue valida, perdiste!" << endl; return;}
	jugador2.seleccionRandom();
	verificarGanador(jugador1, jugador2);

}


int main() {
	while (running) {
		jugar();
		string choice;
		cout << "\n Quieres volver a jugar? Escribe Si/No" << endl;
		cin >> choice;
		if (choice == "no" || choice == "No") {
			running = false;
		}

	}
}



