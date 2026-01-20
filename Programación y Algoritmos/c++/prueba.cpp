#include <iostream>

using namespace std;
int main()
{
	float calificacion;

	cout << "Escribe la calificacion: ";
	cin >> calificacion;

	if (calificacion >= 6)
	{
		cout << "Aprobado";

	}
	else 
	{
		cout << "Reprobado";
	}
}

