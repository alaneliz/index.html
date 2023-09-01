Proceso sin_titulo
	Definir num_clientes Como Entero;
	Definir clientes Como Entero;
	Definir precio_total Como Entero;
	Definir num_fiestas_tematicas Como Entero;
	Definir paquete_inicial Como Entero;
	Definir personas, mas_personas, chilidog, hot_dog, pizza, marinitas, es_tematica_la_fiesta, aumento, precio, pastel, pinata, refrescos, aguas_de_sabor, botanas, gelatinas, invitaciones, espectaculo, Musica_ambiental Como Entero;
	Definir respuesta Como Caracter;
	Definir Respuesta Como Entero;
	
	
	clientes <- 0;
	precio_total <- 0;
	num_fiestas_tematicas <- 0;
	
	paquete_inicial <- 3000;
	
	personas <- 60;
	mas_personas <- 0;
	chilidog <- 15;
	hot_dog <- 10;
	pizza <- 50;
	marinitas <- 12;
	es_tematica_la_fiesta <- 0;
	aumento <- 15;
	precio <- 0;
	pastel <- 250;
	pinata <- 350;
	refrescos <- 650;
	aguas_de_sabor <- 250;
	botanas <- 300;
	gelatinas <- 100;
	invitaciones <- 250;
	espectaculo <- 700;
	Musica_ambiental <- 200;
	
	
	
	Mientras respuesta = "si" o respuesta = "Si" o respuesta = "SI" Hacer
		Escribir "¿Deseas pagar un servicio de fiestas? R: 1.SI, 2.NO";
		Leer respuesta;
		
		Si respuesta = "1" Entonces
			Escribir "Genial el costo del paquete tiene un valor inicial de $3,000";
			Escribir "que incluye la renta del salón por 3 horas para 60 personas.";
			
			Escribir "¿Deseas invitar más personas de las 60 predeterminadas? 1.SI, 2.NO";
			Leer respuesta;
		FinSi
		
			
			Si respuesta = "1" Entonces
				Escribir "Agrega la cantidad de personas (se avisa que el límite de invitados es 140)";
				Leer mas_personas;
				
				Si mas_personas > 140 Entonces
					personas <- 140;
					Escribir "Lo sentimos, no puedes invitar tantos :c";
					Escribir "Te limitaremos a 140";
				Sino
					personas <- personas + mas_personas;
					Escribir "Irán", personas, "personas";
					
					Escribir "¿La fiesta es temática?";
					Escribir "Si es así, avisamos que los costos de los siguientes servicios aumentan un 15%.";
					Escribir "R: 1.SI, 2.NO";
					Leer es_tematica_la_fiesta;
					
					Si es_tematica_la_fiesta = 1 Entonces
						num_fiestas_tematicas <- num_fiestas_tematicas + 1;
					FinSi;
					
					Escribir "Irán", personas, "personas";
				FinSi;
				
			Sino
				Escribir "¿La fiesta es temática?";
				Escribir "Si es así, avisamos que los costos de los siguientes servicios aumentan un 15%.";
				Escribir "R: 1.SI, 2.NO";
				Leer es_tematica_la_fiesta;
				
				Si es_tematica_la_fiesta = 1 Entonces
					num_fiestas_tematicas <- num_fiestas_tematicas + 1;
				FinSi;
			FinSi;
			
			Si es_tematica_la_fiesta = 1 Entonces
				Mientras es_tematica_la_fiesta = 1 Hacer
					Escribir "Deseas agregar alguno de estos servicios:";
					Escribir "1.-pastel = ($250)";
					Escribir "2.-piñata = ($350)";
					Escribir "3.-refrescos = ($650)";
					Escribir "4.-aguas_de_sabor = ($250)";
					Escribir "5.-botanas = ($300)";
					Escribir "6.-gelatinas = ($100)";
					Escribir "7.-invitaciones = ($250)";
					Escribir "8.-espectaculo = ($700)";
					Escribir "9.-Musica_ambiental = ($200)";
					Escribir "10.-chilidog = ($400)";
					Escribir "11.-hotdog = ($300)";
					Escribir "12.-pizza = ($600)";
					Escribir "13.-marinitas =($450)";
					Escribir "14.-Ya no quiero comprar nada";
				FinMientras
				
			FinSi
				Leer respuesta;
					
				Si Respuesta = "1" Entonces
					precio <- pastel * aumento / 100 + pastel;
				FinSi
				
				 SI Respuesta = "2" Entonces
					precio <- pinata * aumento / 100 + pinata;
				FinSi
						 Si Respuesta = "3" Entonces
							 precio <- refrescos * aumento / 100 + refrescos;
						 finsi
						 
							 Si Respuesta = "4" Entonces
								 precio <- aguas_de_sabor * aumento / 100 + aguas_de_sabor;
							 FinSi
							 
								Si Respuesta = "5" Entonces
									precio <- botanas * aumento / 100 + botanas;
								FinSi
								
									 Si Respuesta = "6" Entonces
										 precio <- gelatinas * aumento / 100 + gelatinas;
									 FinSi
									 
										 Si Respuesta = "7" Entonces
											 precio <- invitaciones * aumento / 100 + invitaciones;
										 FinSi
										 
											 Si Respuesta = "8" Entonces
												 precio <- espectaculo * aumento / 100 + espectaculo;
											 FinSi
											 
												 Si Respuesta = "9" Entonces
													 precio <- Musica_ambiental * aumento / 100 + Musica_ambiental;
												 FinSi
												 
													 Si Respuesta = "10" Entonces
															chilidog <- chilidog + mas_personas * 15;
															precio <- chilidog * aumento / 100 + chilidog;
														FinSi
														
														 Si Respuesta = "11" Entonces
																hot_dog <- hot_dog + mas_personas * 10;
																precio <- hot_dog * aumento / 100 + hot_dog;
															FinSi
															
															 Si Respuesta = "12" Entonces
																 precio <- pizza * aumento / 100 + pizza;
															 FinSi
															 
																 Si Respuesta = "13" Entonces
																	 precio <- marinitas * aumento / 100 + marinitas;
																 FinSi
																 
																	 Si Respuesta = "14" Entonces
																			precio <- precio_total;
																			es_tematica_la_fiesta <- 0;
																		FinSi;
																		
																		Si Respuesta >= "1" y Respuesta <= "13" Entonces
																			precio_total <- precio_total + precio;
																			Escribir "Tu paquete aumentó $", precio;
																			Escribir "Tu total actual es de $", precio_total;
																		FinSi;
																		
																	FinMientras;
																
																
																clientes <- clientes + 1;
																num_clientes <- num_clientes + 1;
																
																Escribir "¿Deseas pagar un servicio de fiestas? R: 1.SI, 2.NO";
																Leer respuesta;
																
																Si Respuesta = "2" Entonces
																	respuesta <- "no";
																FinSi;
														
															
															Escribir "Número de clientes atendidos: ", num_clientes;
															Escribir "Número de fiestas temáticas: ", num_fiestas_tematicas;
															Escribir "Ingresos totales: $", precio_total;
															Escribir "Promedio de ingresos por cliente: $", precio_total / num_clientes;
															
														
														
FinAlgoritmo


