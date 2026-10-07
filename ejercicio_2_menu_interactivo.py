# bucle infinito para pedir el comando hasta que el usuario decida salir
while True:
    print("\nOpciones:")
    print("A. Mover a la derecha")
    print("B. Mover a la izquierda")
    print("C. Mover hacia el frente")
    print("D. Mover hacia atrás")
    print("E. Apagar")
    
    comando = input("Ingrese un código de comando (A, B, C, D o E): ")
    
    match comando:
        case "A":
            print("El robot se desplazó a la derecha")
        case "B":
            print("El robot se desplazó a la izquierda")
        case "C":
            print("El robot se desplazó hacia adelante")
        case "D":
            print("El robot se desplazó hacia atrás")
        case "E":
            print("Salir del programa")
            break  
# Rompemos el bucle para apagar el robot
        case _:
            print("Comando no reconocido. Intente de nuevo.")""