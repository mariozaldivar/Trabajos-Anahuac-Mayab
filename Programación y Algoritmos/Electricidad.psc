Algoritmo Electricidad
	Definir consumo, costo como Real;
	Escribir "Por favor escriba su consumo en kWh";
	Leer consumo;
	
	
	Si (consumo < 150 y consumo > 0 ) Entonces
		costo = consumo * 0.80;
	FinSi
	
	Si (consumo < 300 y consumo > 151 ) Entonces
		costo = consumo;
	FinSi
	
	
	
	
FinAlgoritmo
