import random


def juego_adivinanza():
    # generar un número del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("bienvenido al juego de adivinanza")
    print("Debes adivinar un número del 1 al 100")

    while not adivinado:
        # solicitar un numero
        adivinanza = input("Introduzca un numero del 1 al 100: ")

        # verificar que la entrada sea un numero
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # lo estamos pasando de string a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}")
            else:
                print(
                    f"Felicitaciones has ganado! El numero {adivinanza} es el secreto y lo has logrado en {intentos} intentos"
                )
        else:
            print("Por favor introduzca un numero válido entre el 1 al 100")


juego_adivinanza()
