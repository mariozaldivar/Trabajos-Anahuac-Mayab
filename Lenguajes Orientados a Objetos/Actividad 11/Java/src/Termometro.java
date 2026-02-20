import java.util.Random;

public class Termometro {
    public float tempC;
    Termometro()
    {
        Random random = new Random();
        tempC = random.nextFloat(100);

    }

    Termometro(float temp)
    {
        tempC = temp;
    }


    public float TemperaturaC()
    {
        System.out.println("La temperatura en °C es de: " + tempC + "°C");
        return tempC;
    }
    public float TemperaturaF()
    {
        float tempF = (tempC * 9/5) + 32f;
        System.out.println("La temperatura en °F es de: " + tempF + "°F");
        return tempF;
    }
    public float TemperaturaK()
    {
        float tempK = tempC + 273.15f;
        System.out.println("La temperatura en K es de: " + tempK + "K");
        return tempK;
    }

    public void MostrarTemperatura()
    {
        this.TemperaturaC();
        this.TemperaturaF();
        this.TemperaturaK();
    }

}
