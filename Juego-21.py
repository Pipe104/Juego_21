import random

# Reglas
print("Bienvenido al juego de 21")
print("Las instrucciones para jugar son las siguientes:")
print("1-Te vas a enfrentar a la computadora en un 1 vs 1")
print("2-A la computadora y a ti se les entregaran dos cartas y tu podrás ver una de las cartas de la computadora")
print("3-El objetivo del juego es que con 2 o más cartas sumes 21 o quedes cerca de este número, es decir que el que quede más cerca o complete 21 gana")
print("4-En el caso en que con las dos cartas que tienes no alcances a sumar 21 o estas muy lejos del número lo que tienes que hacer es pedirle una carta a la casa (en este caso la computadora), puedes pedir las cartas quieras, además no se turnaran la computadora y tu para pedir, tu pides las cartas que quieras y luego pide la computadora.")
print("5-Entonces te preguntaras ¿Qué pasa si me paso de 21?, y la respuesta es que pierdes automáticamente")
print("6-Hay cartas que son letras como bien lo recordaras, entonces ¿cuál es el valor de ellas?")
print("El A o as vale uno u once según como tu decidas usarla, las letras J, Q, K valen 10 cada una")
print("8-En caso de que queden en empate la computadora y el jugador, automáticamente gana la computadora")


def cartas(NR, cartasFormadas):
    for i, carta in enumerate(cartasFormadas):
        if i == NR:
            return carta


valNumerico = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
valSimbolo = [" ♣", " ♥", " ♠", " ♦"]

# Lista por compresión (acá formamos todas las tarjetas)
cartasFormadas = [(num, sim) for num in valNumerico for sim in valSimbolo]

# Reparto inicial
cartasJ = [0] * 2
cartasC = [0] * 2
cartas_usadas = []

nr1 = random.randint(0, 51)
nr2 = random.randint(0, 51)

while True:
    if nr1 in cartas_usadas:
        nr1 = random.randint(0, 51)
    else:
        cartas_usadas.append(nr1)
        break

while True:
    if nr2 in cartas_usadas:
        nr2 = random.randint(0, 51)
    else:
        cartas_usadas.append(nr2)
        break

cartasJ[0] = cartas(nr1, cartasFormadas)
cartasJ[1] = cartas(nr2, cartasFormadas)

nr1 = 0
nr2 = 0

while True:
    if nr1 in cartas_usadas:
        nr1 = random.randint(0, 51)
    else:
        cartas_usadas.append(nr1)
        break

while True:
    if nr2 in cartas_usadas:
        nr2 = random.randint(0, 51)
    else:
        cartas_usadas.append(nr2)
        break

cartasC[0] = cartas(nr1, cartasFormadas)
cartasC[1] = cartas(nr2, cartasFormadas)

print(f"Estas son tus cartas {cartasJ}")
print(f"Esta es una de las cartas de la computadora {cartasC[0]}")

# Suma de cartas del jugador
sumaste = 0
for carta in cartasJ:
    # Obtener el valor de la carta
    valor = carta[0]

    # Si la carta es un número, suma su valor directamente
    if isinstance(valor, int):
        sumaste += valor

    # Si la carta es una letra, aplica el valor correspondiente
    elif valor in ("J", "Q", "K"):
        sumaste += 10

    # Si la carta es un As, pregunta al usuario si vale 1 u 11
    elif valor == "A":
        sumaste += 1

# Si hay Ases y la suma con 11 no pasa de 21, entonces se toma como 11
for s in cartasJ:
    valor = s[0]
    if sumaste + 10 <= 21 and valor == "A":
        sumaste += 10

print(f"Tu suma actual es: {sumaste}")

while True:
    tomar = input(
        "Si quieres comer más cartas escribe 'si', si no escribe 'no': ")
    if tomar.lower() == "si":
        NR = 0
        while True:
            NR = random.randint(1, 51)
            if NR not in cartas_usadas:
                cartas_usadas.append(NR)
                break
        carta_nueva = cartas(NR, cartasFormadas)
        cartasJ.append(carta_nueva)
        sumaste = 0
        for carta in cartasJ:
            # Obtener el valor de la carta
            valor = carta[0]

            # Si la carta es un número, suma su valor directamente
            if isinstance(valor, int):
                sumaste += valor

            # Si la carta es una letra, aplica el valor correspondiente
            elif valor in ("J", "Q", "K"):
                sumaste += 10

            # Si la carta es un As, pregunta al usuario si vale 1 u 11
            elif valor == "A":
                sumaste += 1
        for s in cartasJ:
            valor = s[0]
            if sumaste + 10 <= 21 and valor == "A":
                sumaste += 10
        if sumaste > 21:
            print(f"Tus cartas son {cartasJ}")
            print(f"Tu suma actual es: {sumaste}")
            print("Perdiste, te pasaste de 21")
            break
        print(f"Tus cartas son {cartasJ}")
        print(f"Tu suma actual es: {sumaste}")
    elif tomar.lower() == "no":
        print("Turno de la computadora")

        while True:
            # Suma para ver si la computadora toma más cartas o si se planta
            sum_computadora = 0
            for carta in cartasC:
                # Obtener el valor de la carta
                valor = carta[0]

                # Si la carta es un número, suma su valor directamente
                if isinstance(valor, int):
                    sum_computadora += valor

                # Si la carta es una letra, aplica el valor correspondiente
                elif valor in ("J", "Q", "K"):
                    sum_computadora += 10

                # Si la carta es un As vale 1 u 11
                elif valor == "A":
                    if sum_computadora < 11:
                        sum_computadora += 11
                    else:
                        sum_computadora += 1

            if sum_computadora < 16:
                NR = 0
                while True:
                    NR = random.randint(1, 51)
                    if NR not in cartas_usadas:
                        cartas_usadas.append(NR)
                        break
                carta_nueva = cartas(NR, cartasFormadas)
                cartasC.append(carta_nueva)
            else:
                print("La computadora se planta")
                print(f"Cartas de la computadora {cartasC}")
                print(f"Suma de la computadora: {sum_computadora}")
                if sum_computadora > 21:
                    print("La computadora pierde")
                elif sum_computadora < sumaste:
                    print("¡Gana el jugador!")
                elif sum_computadora >= sumaste:
                    print("¡Gana la computadora!")
                break
        break
