import random


class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return f"Name: {self.__name} Value: {self.__value}"
    
    def __repr__(self):
        return self.__name
    
class Deck:
    def __init__(self):
        self.__cards = []
        self.__create()

    def __create(self):
        self.__cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        suits = ["Heart", "Club", "Diamond", "Spade"]

        for suit in suits:
            for card in cards:
                card_name = f"{suit} {card[0]}"
                card_value = card[1]
                new_card = Card(card_name, card_value)
                self.__cards.append(new_card)

        random.shuffle(self.__cards)

    def draw(self):
        return self.__cards.pop(0)

    def reset(self):
        self.__create()

if __name__ == "__main__":
    deck = Deck()
    deck.reset()
    pass