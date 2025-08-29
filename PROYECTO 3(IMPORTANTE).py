try:
    print("-"*10 + "BIENVENIDO AL ANALIZADOR DE TEXTOS" + "-"*10)
    text = input("Introduce un texto: ")
    number = int(input("Introduce tres numeros: "))
    numero_cadena = str(number)
    numero_invertido = numero_cadena[::-1]
    numero_invertido_entero = int(numero_cadena[::-1])
    print("-"*10 + "PROCESANDO INFORMACION"+ "-"*10)
    while True:
        print("-" * 10 + "¡INFORMACION PROCESADA!" + "-" * 10)
        print("1. Contar letra\n"
              "2. Cuantas palabras hay a lo largo del texto\n"
              "3. Mostrar la primera letra del texto y la ultima letra del texto\n"
              "4. Texto invertido\n"
              "5. Numeros invertidos\n"
              "6. ¿Python se encuentra?\n"
              "7. Salir")
        option = int(input("Introduce una opcion: "))
        match option:
            case 1:
                print("-"*10+"CONTAR LETRA"+"-"*10)
                letter = input("Introduce la letra que quieres contar en el texto: ")
                numero_veces = text.count(letter)
                print(f"La letra '{letter}' aparece {numero_veces} veces en el texto!")
            case 2:
                print("-"*10 +"Palabras a lo largo del texto"+ "-"*10)
                palabras = text.split()
                numero_palabras = len(palabras)
                print(f"El texto tiene {numero_palabras} palabras en el texto!")
            case 3:
                print("-"*10+"PRIMERA Y ULTIMA PALABRA DE TEXTO!"+ "-"*10)
                first = text[0]
                last = text[-1]
                print(f"La primera letra del texto es: '{first}' y la ultima letra del texto es: '{last}'")
            case 4:
                print("-"*10+"TEXTO INVERTIDO"+ "-"*10)
                string_invertido = text [:: -1]
                print(f"El texto invertido es: {string_invertido}")
            case 5:
                print("-"*10 + "NUMEROS INVERTIDOS"+ "-"*10)
                print(f"Los numeros invertidos son: {numero_invertido_entero}")
            case 6:
                print("-"*10+ "¿Se encuentra python?"+ "-"*10)
                if "python".lower() in text.lower():
                    print("El texto 'Python' si aparece en el texto!")
                else:
                    print("El texto 'Python' no aparece en el texto!")
            case 7:
                print("-"*10+"¡Gracias por usar el programa!"+ "-"*10)
                break
            case _:
                print("Ingrese una opcion valida")
except ValueError:
    print("No se ha podido introducir un valor valido")
except KeyboardInterrupt:
    print("Se ha interrompido el programa")
except Exception as e:
    print(f"El error ha ocurrido\n"
          f"ERROR: {e}")