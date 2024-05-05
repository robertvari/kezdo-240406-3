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
    

if __name__ == "__main__":
    my_card_1 = Card("Spade King", 10)
    my_card_2 = Card("Club 3", 3)
    my_card_3 = Card("Spade Ace", 11)

    my_hand = [my_card_1, my_card_2, my_card_3]
    hand_value = sum([i.value for i in my_hand])
    print(my_hand, hand_value)