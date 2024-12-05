import random

nombre = input("Ingresa tu nombre: ")

print(f"Hola {nombre}, espero te encuentres bien, vamos a jugar")

colores = ["rojo", "azul", "verde", "amarillo", "morado", "rosa", "blanco", "negro", "naranja", "cafe"]


def generar_lista_colores(cantidad_colores):
    return random.sample(colores, cantidad_colores)

def jugar():
    cantidad_colores = int(input("Ingresa la cantidad de colores a adivinar: "))

    if cantidad_colores < 3:
        print("Debes ingresar al menos 3 colores.")
        return
    
    colores_secretos = generar_lista_colores(cantidad_colores)
    intentos = 0
    contador_colores_correctos = 0
    contador_posicion_correcta = 0

    print(f"Listo {nombre}, colores secretos generados. ¡Intenta adivinarlos!")

    while True:
        try:
            secuencia_jugador = input("INGRESA TU SECUENIA DE COLORES: ").split()
            
            if len(secuencia_jugador) != cantidad_colores:
                print(f"Debes ingresar exactamente {cantidad_colores} colores.")
                continue
            

            colores_posicion_correcta = sum(1 for i in range(cantidad_colores) if colores_secretos[i] == secuencia_jugador[i])
            colores_secretos_restantes = [colores_secretos[i] for i in range(cantidad_colores) if colores_secretos[i] != secuencia_jugador[i]]
            secuencia_jugador_restante = [secuencia_jugador[i] for i in range(cantidad_colores) if colores_secretos[i] != secuencia_jugador[i]]
            colores_posicion_incorrecta = sum(1 for color in secuencia_jugador_restante if color in colores_secretos_restantes)
            intentos += 1

            if colores_posicion_correcta == cantidad_colores:
                print(f"Felicidades! adivinaste los {cantidad_colores} en {intentos} intentos.")
                break
            else:
                print(f"Tienes {colores_posicion_correcta} colores en la posicion correcta.")
                print(f"Tienes {colores_posicion_incorrecta} colores correctos pero en la posicion incorrecta.")

        except ValueError:
            print("Ingresa una secuencia de colores valida.")
jugar()
