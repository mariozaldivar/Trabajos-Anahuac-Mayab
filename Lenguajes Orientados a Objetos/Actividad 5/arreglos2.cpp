#include <iostream>

using namespace std;

int main()
{
    int array[10];

    cout << "Indice: " << "\t" << "Valor" << endl;

    for (int i = 0; i < 10; i++)
    {
        array[i] = 0;
        cout << i << "\t" << array[i] << endl;
    }


}
