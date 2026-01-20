#include <iostream>
#include <locale.h>

using namespace std;

int contador = 0;
int total = 0; 

int main() 
{
	setlocale(LC_ALL, "");

	cout << "Vaya introduciendo la estatura en centimetros de los 5 alumnos" << endl;
	for (int i = 1; i <= 5; i++)
	{
		
		int estatura = 0 ;
		while (estatura < 110 || estatura > 220)
		{
			cout << "Escribe la estatura del alumno " << i << ": ";
			cin >> estatura; 
		}
		if (estatura > 170)
		{
			contador++;
		}
		total = total + estatura;


	}

	cout << "El promedio de estatura de los alumnos es: " << total/5 << "cm" << endl;
	cout << "Hubo " << contador << " alumnos mas altos que 170cm" << endl;

	
}

