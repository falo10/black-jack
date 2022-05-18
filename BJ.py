from random import *
from collections import *

""" the goal of the game is to get the number of points as close as possible to 21
punctation: 
1. Cards from two to ten have a value equal to the number of the card
2. The Jack, Queen and King are worth 10 points
3. The ace is worth 1 or 11, whichever is better for the player.

Start of a game:

Player options:

hit - if you want another card to gain a number of points as close as possible to 21
stand - if you don't want another card 

Dealer options:
The dealer's rules of play are predetermined!
If the amount of his points is under 17 he has to hit next card.
If the number of points is equal to 17 or more, then he has to stand.


Results:

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
            "Jack hearts":10, "Jack diamonds":10, "Jack spades":10, "Jack clubs":10,
            "Queen hearts":10, "Queen diamonds":10, "Queen spades":10, "Queen clubs":10,
            "King hearts":10, "King diamonds":10, "King spades":10, "King clubs":10,
            "Ace hearts":11, "Ace diamonds":11, "Ace spades":11, "Ace clubs":11}
            


def first_deal (deck):
    selectedCard=deck.pop()
    return selectedCard



def give_number_of_points (cardsHeld, pointsOwned):
    for card in cardsHeld:
        for cards, punctuation in cardPointsToUse:
            if (card == cards):
                pointsOwned.append(punctuation)
    return (pointsOwned)

def play_black_jack (sumOfPoints, cards, newCardPoints):
    while True:
        if (sumOfPoints > 21):
                print ('You lost! Try next time!')
                return (sumOfPoints)
        elif (sumOfPoints == 21):
            print ('BLACKJACK! - your total points are 21!')
            return sumOfPoints
        else:
            choice = input(f"""Your number of points is: {sumOfPoints}. What do you want to do next? Write:
            hit - if you want another card
            stand - if you don't want another card  """)
            if (choice.upper() == 'HIT'):
                newCard.append(first_deal(cardList))
                print (f"Your new card is {newCard}")
                newCardPoints = give_number_of_points(newCard, newCardPoints)
                newCardPointsToAdd = sum(newCardPoints)  # need int to add to our points
                cards.extend(newCard)
                sumOfPoints += newCardPointsToAdd
                newCardPointsToAdd = []
                newCardPoints.clear()
                newCard.clear()
                if (sumOfPoints == 21):
                    print ('BLACKJACK! - your total points are 21!')
                    return (sumOfPoints)
                elif (sumOfPoints > 21):
                    print (f"Number of your points are: {sumOfPoints}!")
                    print ('You lost! Try next time!')
                    return (sumOfPoints)
            elif (choice.upper() == 'STAND'):
                return (sumOfPoints)
            else:
                print("""Invalid command! Try again! Write:
                    hit - if you want another card
                    stand - if you don't want another card
                """)

def make_dealer_move (pointsScored, dealerCards, sumOfDealerPoints, newDealersCardPoints):
    if (pointsScored <= 21):
        print (f"The dealer's cards are: {dealerCards} and the number of his points is {sumOfDealerPoints}")
        while True:
            if (sumOfDealerPoints < 17):
                newDealersCard.append(first_deal(cardList))
                print (f"The dealer's next card is {newDealersCard}")
                newDealersCardPoints = give_number_of_points(newDealersCard, newDealersCardPoints)
                newDealersCardPointsToAdd = sum(newDealersCardPoints)  
                dealerCards.extend(newDealersCard)
                sumOfDealerPoints += newDealersCardPointsToAdd
                newDealersCardPoints.clear()
                newDealersCardPointsToAdd = []
                newDealersCard.clear()
                print (f"Now, the dealer's cards are: {dealerCards} and the number of his points is {sumOfDealerPoints}")
            else:
                break
        if (sumOfDealerPoints > 21):
            print ('Congratulations, you managed to win!')
            return (sumOfDealerPoints)
        elif (sumOfDealerPoints < pointsScored):
            print ('Congratulations, you managed to win!')
            return (sumOfDealerPoints)
        elif (sumOfDealerPoints > pointsScored):
            print ('You lost! Try next time!')
            return (sumOfDealerPoints)
        elif (sumOfDealerPoints == pointsScored):
            print ('It is a draw!')
            return (sumOfDealerPoints)
    elif (pointsScored > 21):
        return (sumOfDealerPoints)


playerCards= []
dealerCards = []
playerPoints =[]
dealerPoints=[]
cardPointsToUse = cardPoints.items()
newCard=[]        
newCardPoints =[]
newDealersCard=[]        
newDealersCardPoints =[]



#START OF THE GAME

shuffle(cardList)

for deal in range (2):
    playerCards.append(first_deal(cardList))
    dealerCards.append(first_deal(cardList))

print(f"Your cards are: {playerCards}")
print(f"First dealer card is: {dealerCards[0]}")

sumOfPlayerPoints = sum(give_number_of_points(playerCards, playerPoints ))
sumOfDealerPoints = sum(give_number_of_points(dealerCards, dealerPoints ))

#CHECK IF PLAYER CAN SPLIT

firstCard = [playerCards[0]]
secondCard = [playerCards[1]]

firstCardPunctation = sum(((give_number_of_points(firstCard, []))))
secondCardPunctation = sum(((give_number_of_points(secondCard, []))))

if (firstCardPunctation < 10 or firstCardPunctation == 11):
    if (firstCardPunctation == secondCardPunctation):
        decisionToSplit = input ('Do you want to split? yes/no: ')
    else:
        decisionToSplit = 'no'
elif (firstCardPunctation == 10):       #many cards has value of 10 (check if the player has same card but diffrent colour to splt) 
    if ("10" in firstCard[0] and "10" in secondCard[0]):
        decisionToSplit = input ('Do you want to split? yes/no: ')
    elif ("Jack" in firstCard[0] and "Jack" in secondCard[0]):
        decisionToSplit = input ('Do you want to split? yes/no: ')
    elif ("Queen" in firstCard[0] and "Queen" in secondCard[0]):
        decisionToSplit = input ('Do you want to split? yes/no: ')
    elif ("King" in firstCard[0] and "King" in secondCard[0]):
        decisionToSplit = input ('Do you want to split? yes/no: ')
    else:
        decisionToSplit = 'no'
else:
    decisionToSplit = 'no'




if (decisionToSplit.upper() == 'YES'):
    #player's turn when split
    print ('!!!!!FIRST SPLIT-HAND!!!!!')
    pointsScoredOnFirstHand = play_black_jack(firstCardPunctation, firstCard, newCardPoints)
    print ('!!!!!SECOND SPLIT-HAND!!!!!')
    pointsScoredOnSecondHand = play_black_jack(secondCardPunctation, secondCard, newCardPoints)
    #dealer's turn when split
    if (pointsScoredOnFirstHand <= 21 or pointsScoredOnSecondHand <= 21):
        print('Now let\'s check the dealers cards!')
    if (pointsScoredOnFirstHand <= 21):
        print ('For first split hand: ') 
    sumOfDealerPoints = make_dealer_move (pointsScoredOnFirstHand, dealerCards, sumOfDealerPoints, newDealersCardPoints)
    if (pointsScoredOnSecondHand <= 21):
        print ('FOR second split hand: ') 
    make_dealer_move (pointsScoredOnSecondHand, dealerCards, sumOfDealerPoints, newDealersCardPoints)
else:
    #player's turn
    pointsScored = play_black_jack(sumOfPlayerPoints, playerCards, newCardPoints)
    #dealer's turn when split
    if (pointsScored <= 21):
        print('Now let\'s check the dealers cards!')
    make_dealer_move (pointsScored, dealerCards, sumOfDealerPoints, newDealersCardPoints)

    

    
