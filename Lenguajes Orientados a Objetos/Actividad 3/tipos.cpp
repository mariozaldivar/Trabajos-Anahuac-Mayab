#include <iostream>


// Mario Andrés Zaldívar de la Cruz
// # 00586553

using namespace std;

int main()
{
    
    cout << "Estos son los tipos de datos incluidos en C++";
    short entero_corto = 1; // 2 bytes
    int entero = 10; // 4 bytes
    float punto_flotante = 10.5; // 4 bytes
    long entero_largo = 100; // 4 bytes
    long double entero_doble_de_largo = 102849371029341903; // 10 bytes
    double doble = 10000000000000; // 8 bytes
    bool booleano = true; // 1 byte
    char caracter = 'a'; // 1 byte

    
    cout << "El tipo de dato short representa un número entero corto, y ocupa 2 bytes. Ejemplo: " << entero_corto << endl;
    cout << "El tipo de dato int representa a un entero, como " << entero << endl;
    cout << "El tipo de dato float representa un numero con decimal flotante, como "  << punto_flotante << endl;
    cout << "El tipo de dato long representa un entero largo, y ocupa 4 bytes, como " << entero_largo << endl;
    cout << "El tipo de dato long double representa un numero un poco mas largo que el double, ocupa 10 bytes, como" << entero_doble_de_largo << endl;
    cout << "El tipo de dato double representa un numero con el doble de capacidad que un int, utilizando 8 bytes, como " << doble << endl;
    cout << "El tipo de dato bool representa un valor binario verdadero o falso, como " << booleano << endl;
    cout << "El tipo de dato char representa un caracter, representado por un numero ASCII, como " << caracter << endl;
    

}

