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


class Game:
    def __init__(self, num_rows=5, num_columns=5, num_players=1):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.num_players = num_players
        self.final_cell = self.num_rows * self.num_columns
        self.ladders = {3: 11, 6: 17, 9: 18, 10: 12}
        self.snakes = {14: 4, 19: 8, 22: 20, 24: 16}

    def assing_ladders_and_snakes_randomly(self):
        """This method assigns ladders and snakes randomly according to the dimensions of the board"""
        return NotImplemented


def clear():
    if (os.name == 'posix'):
        return os.system('clear')


def start_game(game):
    players = [Player() for _ in range(game.num_players)]
    current_player, winner = 0, False
    while (not winner):
        clear()

        # Start turn
        print("Es el turno del jugador #{0}".format(current_player + 1))
        input("Presione cualquier tecla tirar el dado...")

        # Roll dice and move
        dice = players[current_player].roll_dice()
        print("El dado ha arrojado el valor {0}".format(dice))
        players[current_player].cell = players[current_player].cell + dice
        print("Jugador avanza a la casilla {0}".format(
            players[current_player].cell))

        # Check final cell
        if players[current_player].cell == game.final_cell:
            winner = True
        elif players[current_player].cell > game.final_cell:
            players[current_player].cell = game.final_cell - \
                (players[current_player].cell - game.final_cell)
            print("El jugador retrocede a la casilla {0}".format(
                players[current_player].cell))

        # Player ascends by ladder
        if players[current_player].cell in game.ladders:
            players[current_player].cell = game.ladders[players[current_player].cell]
            print("El jugador avanza por la escalera al cuadro {0}".format(
                players[current_player].cell))

        # Player descends by snake
        if players[current_player].cell in game.snakes:
            players[current_player].cell = game.snakes[players[current_player].cell]
            print("El jugador desciende por la serpiente al cuadro {0}".format(
                players[current_player].cell))

        # End turn
        if winner:
            print("Has ganado el juego.")
        else:
            input("Presione cualquier tecla terminar turno...")
            current_player = (current_player + 1) % game.num_players


def help():
    clear()
    print("Reglas del juego:")
    print("1. El tablero tiene 25 cuadros, y el objetivo es llegar o superar el cuadro 25.")
    print("2. El cuadro inicial es el 0, el cual se encuentra por fuera del tablero a la izquierda del cuadro 1.")
    print("3. En cada turno usted tira un dado de 6 lados y mueve el n??mero de cuadrados siguiendo la l??nea punteada de la imagen.")
    print("4. Si su turno termina en la parte inferior de una escalera, sube por la escalera.")
    print("5. Si su turno termina en la cabeza de una serpiente, baja por la serpiente.")
    print("6. Recuerde que un dado solo puede caer entre los n??meros 1 a 6")
    print("")
    input("Presione Enter para volver al men?? inicial...")
    clear()


def main():
    clear()
    valid = False
    while (not valid):
        print("Bienvendio al Juego de las Serpientes y Escaleras")
        print("1. Iniciar Juego")
        print("2. Ayuda")
        print("3. Salir")
        print("Seleccione una opci??n: ", end="")
        option = None
        try:
            option = int(input())
            if (option <= 0 or option > 3):
                raise Exception("Opci??n por fuera de los l??mites.")
            else:
                if (option == 1):
                    # Board dimensions
                    # NOTE: the board dimensions can be safely modified (or added as user input) as long as the
                    #       assing_ladders_and_snakes_randomly method is implemented inside of the Game class.
                    num_rows = 5
                    num_columns = 5

                    # Num of players
                    num_players = int(
                        input("Seleccione el n??mero de jugadores: "))
                    if (num_players <= 0):
                        raise Exception("N??mero de jugadores inv??lido")

                    game = Game(num_rows, num_columns, num_players)
                    start_game(game)
                    valid = True
                elif (option == 2):
                    help()
                else:
                    print("Gracias por jugar!")
                    valid = True
        except Exception as err:
            print(err)
            print(
                "Los valores ingresados fueron inv??lidos, por favor vuelva a intentarlo.")
            print()


if __name__ == '__main__':
    main()
