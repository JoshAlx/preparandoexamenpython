bandas = []

# Construyendo la interfaz
print("---------------------------")
print("-----ALTAVOZ ES TU VOZ-----")
print("---------------------------")

opcion = 0
while(opcion != 6):
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
        banda["id"]=len(bandas) + 1
        banda["nombre"]=input("Digite el nombre de la banda: ")
        banda["genero"]=input("Digite el género: ")
        banda["clasificación"]=input("Clasificación: ")
        banda["tiempo"]=int(input("Tiempo: "))
        banda["costo"]=int(input("Costo: ($)"))
        bandas.append(banda)
    
    elif(opcion == 2):
        
        bandaBuscada = input("Digita el nombre de la banda que estas buscando: ")
        bandaEncontrada = False
        for bandaAuxiliar in bandas:
            if(bandaAuxiliar["nombre"] == bandaBuscada):
                # Como lo encontré, muestro los datos de bandAuxiliar
                print(f"id: {bandaAuxiliar["id"]} --- nombre: {bandaAuxiliar["nombre"]} ")
                bandaEncontrada = True
                break
        
        if not bandaEncontrada:
            print("Parce, siga buscando...")

    elif(opcion == 3):

        if not bandas:
            print("No hay bandas registradas.")
        
        else:
            for i, banda in enumerate(bandas, start=1):
                print(f"Banda No. {i}:")
                print(f"ID: {banda['id']}")
                print(f"Nombre: {banda['nombre']}")
                print(f"Género: {banda['genero']}")
                print(f"Clasificación: {banda['clasificación']}")
                print(f"Tiempo: {banda['tiempo']}")
                print(f"Costo: {banda['costo']}")
                print()

    elif(opcion == 4):
        
        nombre_banda_modificar = input("Digite el nombre de la banda que desea modificar: ")
        banda_modificar = None
        for banda in bandas:
            if banda["nombre"] == nombre_banda_modificar:
                banda_modificar = banda
                break
    
        if banda_modificar:
            # Mostrar los datos actuales de la banda
            print("Datos actuales de la banda:")
            print(banda_modificar)

            # Solicitar los nuevos datos
            banda_modificar["nombre"] = input("Nuevo nombre de la banda: ")
            banda_modificar["genero"] = input("Nuevo género: ")
            banda_modificar["clasificación"] = input("Nueva clasificación: ")
            banda_modificar["tiempo"] = int(input("Nuevo tiempo: "))
            banda_modificar["costo"] = int(input("Nuevo costo: ($)"))
        else:
            print("La banda no se encontró en la lista.")
    
    elif(opcion == 5):
        
        nombre_banda_eliminar = input("Digite el nombre de la banda que desea eliminar: ")
        banda_eliminar = None
        for banda in bandas:
            if banda["nombre"] == nombre_banda_eliminar:
                banda_eliminar = banda
                break
    
        if banda_eliminar:
            bandas.remove(banda_eliminar)
            print(f"La banda '{nombre_banda_eliminar}' ha sido eliminada correctamente.")
        else:
            print("La banda no se encontró en la lista.")
    
    elif(opcion == 6):
        print("Gracias por consultar. Te esperamos de nuevo. ¡EN LA BUENA, PARCE!")
    
    else:
        print("Opción inválida (Digite opción 1 a 6)")