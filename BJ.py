from random import *
from collections import *



cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            ]


shuffle(cardList)
print (cardList)


def rozdanie (lista):
    deck = []
    for i in range (5):
        x=lista.pop()
        deck.append(x)
    return deck


reka1 = rozdanie(cardList)
reka2 = rozdanie(cardList)