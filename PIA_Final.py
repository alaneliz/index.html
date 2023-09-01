#Se requiere un programa que permitirá calcular el total a pagar por un paquete de fiesta infantil. El costo del paquete tiene un valor inicial de $3,000 
#que incluye la renta del salón por 3 horas para 60 personas.
#Si desea agregar más personas al paquete el cliente puede elegir un máximo de 140 personas más (la capacidad del salón es de 200 personas).
num_clintes = (0)
clientes = (0)
precio_total = (0)
num_fiestas_tematicas = (0)
personas_totales = (0)
paquete_inicial = 3000

personas = (60)
mas_personas= (0)
chilidog = (15)
hot_dog = (10)
pizza = (50)
marinitas = (12)
es_tematica_la_fiesta = (0)
aumento = (15)
precio = (0)
pastel = (250)
piñata = (350)
refrescos = (650)
aguas_de_sabor = (250)
botanas = (300)
gelatinas = (100)
invitaciones = (250)
espectaculo = (700)
Musica_ambiental= (200)
chilidog = (400)
hotdog = (300)
pizza = (600)
marinitas =(450)
respuesta = "si"

while respuesta == "si" or respuesta == "Si" or respuesta == "SI":
    Entrada = int( input ("""
    ¿Deseas pagar un servicio de fiestas? R: 1.SI, 2.NO
    """))
    precio = 0
    clientes += 1
    if Entrada == 1:
        print ("""
        Genial el costo del paquete tiene un valor inicial de $3,000 
        que incluye la renta del salón por 3 horas para 60 personas.
        """)
        ReSpUeStA = int(input("""
        ¿deseas invitar mas personas de las 60 predeterminadas? 
        1.SI, 2.NO
        """))
        if ReSpUeStA == 1:
            mas_personas = int( input ("""agrega la cantidad de personas *se avisa que el limite de invitados es 140  """))
            if mas_personas > (140):
                personas = (140)
                print ("""
                    lo sentimos no puedes invitar tantos :c
                    te limitaremos a 140
                        """)
            else:
                personas + mas_personas
                personas += mas_personas
                print("iran", personas)         
                es_tematica_la_fiesta = int(input("""
                ¿La fiesta es tematica? 

                si es asi avisamos que los costos de los siguientes servicios 
                aumentan un 15% de los servicios.
                R 1.SI, 2.NO
                """))
                if es_tematica_la_fiesta == "1":  
                    num_fiestas_tematicas += 1

            print("iran", personas)   
        else:
            es_tematica_la_fiesta = int(input("""
            ¿La fiesta es tematica? 

            si es asi avisamos que los costos de los siguientes servicios 
            aumentan un 15% de los servicios.
            R 1.SI, 2.NO
            """))
            if es_tematica_la_fiesta == "1":  
                    num_fiestas_tematicas += 1

            
        if es_tematica_la_fiesta == 1:
            while es_tematica_la_fiesta == 1:
                respuesta = int(input("""Desea agregar alguno de estos servicios:
                1.-pastel = ($250)
                2.-piñata = ($350)
                3.-refrescos = ($650)
                4.-aguas_de_sabor = ($250)
                5.-botanas = ($300)
                6.-gelatinas = ($100)
                7.-invitaciones = ($250)
                8.-espectaculo = ($700)
                9.-Musica_ambiental= ($200)
                10.-chilidog = ($400)
                11.-hotdog = ($300)
                12.-pizza = ($600)
                13.-marinitas =($450)
                """))

                if respuesta == 1:
                    precio = pastel * aumento
                    precio = precio / 100
                    precio= precio + pastel
                elif respuesta == 2:
                    precio = piñata * aumento
                    precio = precio / 100
                    precio= precio + piñata
                elif respuesta == 3:
                    precio = refrescos * aumento
                    precio = precio / 100
                    precio= precio + refrescos           
                elif respuesta == 4:
                    precio = aguas_de_sabor * aumento
                    precio = precio / 100
                    precio= precio + aguas_de_sabor
                elif respuesta == 5:
                    precio = botanas * aumento
                    precio = precio / 100
                    precio= precio + botanas
                elif respuesta == 6:
                    precio = gelatinas * aumento
                    precio = precio / 100
                    precio= precio + gelatinas
                elif respuesta == 7:
                    precio = invitaciones * aumento
                    precio = precio / 100
                    precio= precio + invitaciones
                elif respuesta == 8:
                    precio = espectaculo * aumento
                    precio = precio / 100
                    precio= precio + espectaculo
                elif respuesta == 9:
                    precio = Musica_ambiental * aumento
                    precio = precio / 100
                    precio= precio + Musica_ambiental
                elif respuesta == 10:
                    chilidog + mas_personas * 15
                    precio = chilidog * aumento
                    precio = precio / 100
                    precio= precio + chilidog
                elif respuesta == 11:
                    hot_dog + mas_personas * 10
                    precio = hot_dog * aumento
                    precio = precio / 100
                    precio= precio + hot_dog
                elif respuesta == 12:
                    precio = pizza * aumento
                    precio = precio / 100
                    precio= precio + pizza
                elif respuesta == 13:
                    precio = marinitas * aumento
                    precio = precio / 100
                    precio= precio + marinitas
                elif respuesta == 14:
                    precio += paquete_inicial
                    print("el costo total fue de $", precio)
                    print ("y iran", personas,"personas")
                    print ("Muy bien que tenga lindo dia :D")
                    break 
                precio += paquete_inicial
                es_tematica_la_fiesta = int(input("Desea agregar otro producto? 1. si / 2.no"))         
        else: 
            if es_tematica_la_fiesta == 2:
                es_tematica_la_fiesta = "Si"
                while es_tematica_la_fiesta == "si" or es_tematica_la_fiesta == "Si" or es_tematica_la_fiesta == "SI":
                        respuesta = int(input("""Desea agregar alguno de estos servicios:
                        1.-pastel = ($250)
                        2.-piñata = ($350)
                        3.-refrescos = ($650)
                        4.-aguas_de_sabor = ($250)
                        5.-botanas = ($300)
                        6.-gelatinas = ($100)
                        7.-invitaciones = ($250)
                        8.-espectaculo = ($700)
                        9.-Musica_ambiental= ($200)
                        10.-chilidog = ($400)
                        11.-hotdog = ($300)
                        12.-pizza = ($600)
                        13.-marinitas =($450)
                        14.-Ya no quiero comprar nada
                        """))

                        if respuesta == 1:
                            precio= precio + pastel
                        elif respuesta == 2:
                            precio= precio + piñata
                        elif respuesta == 3:
                            precio= precio + refrescos
                        elif respuesta == 4:
                            precio= precio + aguas_de_sabor
                        elif respuesta == 5:
                            precio= precio + botanas
                        elif respuesta == 6:
                            precio= precio + gelatinas
                        elif respuesta == 7:
                            precio= precio + invitaciones
                        elif respuesta == 8:
                            precio= precio + espectaculo
                        elif respuesta == 9:
                            precio= precio + Musica_ambiental
                        elif respuesta == 10:
                            precio= precio + chilidog
                        elif respuesta == 11:
                            precio= precio + hot_dog
                        elif respuesta == 12:
                            precio= precio + pizza
                        elif respuesta == 13:
                            precio= precio + marinitas
                        
                        es_tematica_la_fiesta =(input("Desea agregar otro producto? si .no"))
    precio += paquete_inicial
    print("el costo total fue de $", precio)
    print ("y iran", personas,"personas")
    precio_total += precio
    respuesta = input("Hay otro cliente? en este apartado se escibe como si o no. si, no " )

print ("muy bien su costo de servicio es de $", precio_total)
print ("los clientes que se atendieron fueron ",clientes)
print ("el total de fiestas hechas fue", num_fiestas_tematicas)
print ("Muy bien que tenga lindo dia :D")