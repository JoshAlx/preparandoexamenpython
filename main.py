bandas = []

# Construyendo la interfaz
print("---------------------------")
print("-----ALTAVOZ ES TU VOZ-----")
print("---------------------------")

opcion = 0
while(opcion != 5):
    print("1. Registrar banda")
    print("2. Buscar información de una banda")
    print("3. Agenda del evento")
    print("4. Modificar una banda")
    print("5. Eliminar una banda")
    print("6. SALIR")

    opcion = int(input("Digita una opción: "))

    if(opcion == 1):
        
        banda = {}
        # creando los datos del diccionario
        banda["id"]=int(input("Digita el id: "))
        banda["nombre"]=input("Digite el nombre de la banda: ")
        banda["genero"]=input("Digite el género: ")
        banda["clasificación"]=input("Clasificación: ")
        banda["tiempo"]=int(input("Tiempo: "))
        banda["costo"]=int(input("Costo: ($)"))
        bandas.append(banda)
    
    elif(opcion == 2):
        
        bandaBuscada = input("Digita el nombre de la banda que estas buscando: ")
        for bandaAuxiliar in bandas:
            if(bandaAuxiliar["nombre"] == bandaBuscada):
                # Como lo encontré, muestro los datos de bandAuxiliar
                print(f"id: {bandaAuxiliar["id"]} --- nombre: {bandaAuxiliar["nombre"]} ")
            else:
                print("Parce, siga buscando...")

    elif(opcion == 3):

        print(bandas)
    
    elif(opcion == 4):
        pass
    
    elif(opcion == 5):
        pass
    
    elif(opcion == 6):
        print("Gracias por participar. Te esperamos de nuevo")
    
    else:
        print("Opción inválida (Digite opción 1 a 6)")