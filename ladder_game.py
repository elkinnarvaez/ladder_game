from sys import stdin
import os
import random


class Player:
    def __init__(self):
        self.cell = 0
        self.dice = None

    def roll_dice(self):
        self.dice = random.randint(1, 6)
        return self.dice


def clear():
    if (os.name == 'posix'):
        return os.system('clear')


def start_game(ladders, snakes, num_players, goal):
    clear()
    players = [Player() for _ in range(num_players)]
    current_player = 0
    winner = False
    while (not winner):
        print("Es el turno del jugador #{0}".format(current_player + 1))
        print("Presion cualquier tecla tirar el dado...")
        players[current_player].roll_dice()
        current_player = (current_player + 1) % num_players


def help():
    clear()
    print("Reglas del juego:")
    print("1.  El tablero tiene 25 cuadros, y el objetivo es llegar o superar el cuadro 25.")
    print("2. El cuadro inicial es el 0, el cual se encuentra por fuera del tablero a la izquierda del cuadro 1.")
    print("3. En cada turno usted tira un dado de 6 lados y mueve el número de cuadrados siguiendo la línea punteada de la imagen.")
    print("4. Si su turno termina en la parte inferior de una escalera, sube por la escalera.")
    print("5. Si su turno termina en la cabeza de una serpiente, baja por la serpiente.")
    print("6. Recuerde que un dado solo puede caer entre los números 1 a 6")
    print("")
    input("Presione Enter para volver al menú inicial...")
    clear()


def main():
    clear()
    valid = False
    while (not valid):
        print("Bienvendio al Juuego de la Escalera")
        print("1. Iniciar Juego")
        print("2. Ayuda")
        print("3. Salir")
        print("Seleccione una opción: ", end="")
        option = None
        try:
            option = int(input())
            if (option <= 0 or option > 3):
                raise Exception("Opción por fuera de los límites.")
            else:
                valid = True
                if (option == 1):
                    num_rows, num_columns = 5, 5
                    num_players = 2
                    ladders = {3: 11, 6: 17, 9: 18, 10: 12}
                    snakes = {14: 4, 19: 8, 22: 20, 24: 16}
                    start_game(ladders, snakes, num_players,
                               num_rows*num_columns)
                elif (option == 2):
                    help()
                    valid = False
                else:
                    print("Gracias por jugar!")
        except Exception as err:
            print(err)
            print("Por favor ingrese una opción correcta.")
            print()


if __name__ == '__main__':
    main()
