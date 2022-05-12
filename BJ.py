from random import *
from collections import *

""" the goal of the game is to get the number of points as close as possible to 21
punctation: 
1. Cards from two to ten have a value equal to the number of the card
2. The Jack, Queen and King are worth 10 points
3. The ace is worth 1 or 11, whichever is better for the player.


"""

cardList = ["2 hearts", "2 diamonds", "2 spades", "2 clubs",
            "3 hearts", "3 diamonds", "3 spades", "3 clubs",
            "4 hearts", "4 diamonds", "4 spades", "4 clubs",
            "5 hearts", "5 diamonds", "5 spades", "5 clubs",
            "6 hearts", "6 diamonds", "6 spades", "6 clubs",
            "7 hearts", "7 diamonds", "7 spades", "7 clubs",
            "8 hearts", "8 diamonds", "8 spades", "8 clubs",
            "9 hearts", "9 diamonds", "9 spades", "9 clubs",
            "10 hearts", "10 diamonds", "10 spades", "10 clubs",
            "Jack hearts", "Jack diamonds", "Jack spades", "Jack clubs",
            "Queen hearts", "Queen diamonds", "Queen spades", "Queen clubs",
            "King hearts", "King diamonds", "King spades", "King clubs",
            "Ace hearts", "Ace diamonds", "Ace spades", "Ace clubs",
            ]

cardPoints = {"2 hearts":2, "2 diamonds":2, "2 spades":2, "2 clubs":2,
            "3 hearts":3, "3 diamonds":3, "3 spades":3, "3 clubs":3,
            "4 hearts":4, "4 diamonds":4, "4 spades":4, "4 clubs":4,
            "5 hearts":5, "5 diamonds":5, "5 spades":5, "5 clubs":5,
            "6 hearts":6, "6 diamonds":6, "6 spades":6, "6 clubs":6,
            "7 hearts":7, "7 diamonds":7, "7 spades":7, "7 clubs":7,
            "8 hearts":8, "8 diamonds":8, "8 spades":8, "8 clubs":8,
            "9 hearts":9, "9 diamonds":9, "9 spades":9, "9 clubs":9,
            "10 hearts":10, "10 diamonds":10, "10 spades":10, "10 clubs":10,
            "Jack hearts":11, "Jack diamonds":11, "Jack spades":11, "Jack clubs":11,
            "Queen hearts":11, "Queen diamonds":11, "Queen spades":11, "Queen clubs":11,
            "King hearts":11, "King diamonds":11, "King spades":11, "King clubs":11,
            "Ace hearts":11, "Ace diamonds":11, "Ace spades":11, "Ace clubs":11}
            
shuffle(cardList)
print (cardList)

"""playerCards = []
selectedCard=cardList.pop()
playerCards.append(selectedCard)
print (playerCards)
"""

def firstDeal (deck):
    selectedCard=deck.pop()
    return selectedCard

playerCards = []
croupierCards = []

for deal in range (2):
    playerCards.append(firstDeal(cardList))
    croupierCards.append(firstDeal(cardList))

print(playerCards)
print(croupierCards[0])
