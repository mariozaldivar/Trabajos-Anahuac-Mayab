class Test {
    public static void main(String[] args)
    {
        Termometro termometro1 = new Termometro();
        Termometro termometro2 = new Termometro(30);

        System.out.println("Para el termometro sin parametros: ");
        termometro1.MostrarTemperatura();

        System.out.println("Para el termometro con parametros: ");
        termometro2.MostrarTemperatura();


    }
}
