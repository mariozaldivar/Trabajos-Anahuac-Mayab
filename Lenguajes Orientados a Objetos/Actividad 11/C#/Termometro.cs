using System;

class Termometro
{

    Random rand = new Random();
    private float tempC;
    public Termometro() 
    {
        tempC = rand.Next(101);
    }

    public Termometro(float temp)
    {
        tempC = temp;
    }

    public float TemperaturaC()
    {
        Console.WriteLine($"La temperatura en °C es de: {tempC}°C");
        return tempC;
    }
    public float TemperaturaK()
    {
        float tempK = tempC + 273.15f;
        Console.WriteLine($"La temperatura en K es de: {tempK}K");
        return tempK;
    }
    public float TemperaturaF()
    {
        float tempF = (tempC * 9/5) + 32f;
        Console.WriteLine($"La temperatura en °F es de: {tempF}°F");
        return tempF;
    }

    public void MostrarTemperatura()
    {
        TemperaturaC();
        TemperaturaK();
        TemperaturaF();
    }


}