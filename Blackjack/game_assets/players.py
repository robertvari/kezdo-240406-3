import random

class PlayerBASE:
    def __init__(self):
        # First attributes
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

        # Then method calls
        self.__create()

    def __create(self):
        self.__credits = random.randint(10, 100)

    @staticmethod
    def get_random_name():
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"


class Player(PlayerBASE):
    pass

class AIPlayer(PlayerBASE):
    pass

if __name__ == "__main__":
    player = Player()
    ai_player = AIPlayer()

    pass