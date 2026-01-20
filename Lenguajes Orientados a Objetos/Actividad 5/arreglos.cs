// Mario Andrés Zaldívar de la Cruz
// #00586553



using System; 
class Arreglos {

	static void Main()
	{
		int[] arreglo = new int[10];

		Console.WriteLine("Indice\tValor");

		for (int indice = 0; indice < arreglo.Length; indice++ ) 
		{
			Console.WriteLine(indice+"\t"+arreglo[indice]);
		}
	}
}
