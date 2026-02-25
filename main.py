from game import Game


def main():
    # Initialize the game with the required text files
    trivia_game = Game("domande.txt", "punti.txt")

    # Start the game
    trivia_game.play()

if __name__ == "__main__":
    main()