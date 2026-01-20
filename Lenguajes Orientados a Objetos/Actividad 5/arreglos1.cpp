#include <iostream>
#include <array>

using namespace std;

int main()
{
	array<int,10> arreglo; 

    cout << "Indice: " << "\t" << "Valor" << endl;
    for (int i = 0; i < 10; i++)
    {
		arreglo[i] = 0;
        cout << i << "\t" << arreglo[i] << endl;
    }

}



