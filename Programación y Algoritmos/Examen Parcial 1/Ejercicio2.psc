Algoritmo CargoPaqueteria
	// Mario Andrés Zaldívar de la Cruz #00586553
	Definir running Como caracter;
	Definir peso, tarifa, costo Como Real;
	
	running = "s";
	tarifa = 160;
	
	Repetir
		Imprimir "Introduzca el peso de su paquete en kilogramos. Tenga en cuenta que no puede sobrepasar los 15 kg.";
		Leer peso;
		Si peso > 15
			Imprimir "El peso sobrepasa los 15kg, por ende no es válido";
			
		SiNo
			costo = peso * tarifa;
			Imprimir "Costo del servicio: ", peso, " x ", tarifa, " = ", costo;
			Si peso <= 3
				Imprimir "Cargo por combustible: (5.5%): ", costo*.055;
				costo = costo * 1.055;
				Imprimir "Total a pagar: ", costo, " pesos";
			SiNo
				Imprimir "Cargo por combustible: (12%): ", costo*.12;
				costo = costo * 1.12;
				Imprimir "Total a pagar: ", costo, " pesos";
			FinSi
			
			
		FinSi
		
		
		
		Repetir 
			Imprimir "¿Desea repetir el cálculo? Escriba S para si, o N para no";
			Leer running;
			running = Minusculas(running);
		Mientras Que Minusculas(running) <> "s" y Minusculas(running) <> "si" y Minusculas(running) <> "n" y Minusculas(running) <> "no"
	Mientras Que running == "s" o running == "si"
FinAlgoritmo
