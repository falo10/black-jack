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
            "Jack hearts":10, "Jack diamonds":10, "Jack spades":10, "Jack clubs":11,
            "Queen hearts":10, "Queen diamonds":10, "Queen spades":10, "Queen clubs":11,
            "King hearts":10, "King diamonds":10, "King spades":10, "King clubs":10,
            "Ace hearts":11, "Ace diamonds":11, "Ace spades":11, "Ace clubs":11}
            
shuffle(cardList)
print (cardList)

"""playerCards = []
selectedCard=cardList.pop()
playerCards.append(selectedCard)
print (playerCards)
"""

def first_deal (deck):
    selectedCard=deck.pop()
    return selectedCard


playerCards= []
croupierCards = []
playerPoints =[]
croupierPoints=[]

for deal in range (2):
    playerCards.append(first_deal(cardList))
    croupierCards.append(first_deal(cardList))

print(playerCards)

cardPointsToUse = cardPoints.items()
  

for card in playerCards:
    for cards, punctuation in cardPointsToUse:
        if (card == cards):
            print (punctuation)


"""print(croupierCards[0])"""
