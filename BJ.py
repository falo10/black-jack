from random import *
from collections import *
import rules

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

def choose_ace_value (cardsReceived):
    for card in cardsReceived:
        for cards, punctuation in cardPointsToUse:
            if (card == cards):
                if (cardPoints[card] == 11):
                    decisionForAcePunctation = input(f"If you want {card} was worth 1 point instead of 11 write \"yes\" else write \"no\" ")
                    if (decisionForAcePunctation.upper() == 'YES'):
                        cardPoints[card] = 1

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
                choose_ace_value (newCard)
                newCardPoints = give_number_of_points(newCard, newCardPoints)
                newCardPointsToAdd = sum(newCardPoints)  # need int to add to our points
                cards.extend(newCard)    
                sumOfPoints += newCardPointsToAdd
                newCardPointsToAdd = []
                newCardPoints.clear()
                newCard.clear()
                if (sumOfPoints == 21):
                    print ('Your total points are 21!')
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

def make_dealer_move (pointsScored, dealerCards, sumOfDealerPoints, newDealersCardPoints, playerCards):
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
            betForGame.append (bet)
            return (sumOfDealerPoints)
        elif (sumOfDealerPoints < pointsScored):
            if (len(playerCards) == 2 and pointsScored == 21):
                print ('Congratulations, you managed to win!')
                betForGame.append (bjBet)
                return (sumOfDealerPoints)
            else:
                print ('Congratulations, you managed to win!')
                betForGame.append (bet)
                return (sumOfDealerPoints)
        elif (sumOfDealerPoints > pointsScored):
            print ('You lost! Try next time!')
            betForGame.pop()
            return (sumOfDealerPoints)
        elif (sumOfDealerPoints == pointsScored and sumOfDealerPoints != 21):
            print ('It is a draw!')
            return (sumOfDealerPoints)
        elif (sumOfDealerPoints == pointsScored and sumOfDealerPoints == 21):
            if (len(dealerCards) == 2):
                if (len(playerCards) == 2):
                    print ('It is a draw!')
                    return (sumOfDealerPoints)
                else:
                    print ('You lost! Try next time!')
                    print ('BLACKJACK always win with 21 pts in 3 or more cards!')
                    betForGame.pop()
                    return (sumOfDealerPoints)
            elif (len(dealerCards) > 2):
                if (len(playerCards) == 2):
                    print ('Congratulations, you managed to win!')
                    print ('BLACKJACK always win with 21 pts in 3 or more cards!')
                    betForGame.append (bjBet)
                    return (sumOfDealerPoints)
                else:
                    print ('It is a draw!')
                    return (sumOfDealerPoints)
                
            
    elif (pointsScored > 21):
        betForGame.pop()
        return (sumOfDealerPoints)



#START OF THE GAME

print ("""
Welcome to BlackJack by falo10
""")


while True:
    decisionToStart = input ("""

Write:
start - if you want to play BlacJack!
rules - if you want to read the rules!
""")
    if (decisionToStart.upper() == 'START'):
        break
    elif (decisionToStart.upper() == 'RULES'):
        print (rules.rulesOfTheBlackJack)
        continue
    else:
        print ('Incorrect data was entered!Try again...')
        continue
        

        

while True:
    try:
        money = int(input('Enter the amount of money you want to enter the game with: '))
        print(f"""
There is now {money} dolars on your account!

From this amount you will be able to withdraw money for further bets!""")
        break
    except ValueError:
        print ('Incorrect value! TRY AGAIN!')


while True:

    playerCards= []
    dealerCards = []
    playerPoints =[]
    dealerPoints=[]
    cardPointsToUse = cardPoints.items()
    newCard=[]        
    newCardPoints =[]
    newDealersCard=[]        
    newDealersCardPoints =[]
    betForGame = []




    while True:
        try:
            bet = int(input(f"""
    Enter the amount of money for this bet: """))
            money -= bet
            if (money >= 0):
                print (f"""
        You bet {bet} dolars!
        On your account remains {money} dolars!
        """)
                break
            else:
                print ('You don\'t have enoug money on your account! Change amount of your bet!')
                money += bet
                print (money)
                continue
        except ValueError:
            print ('Incorrect value! TRY AGAIN!')



    bjBet = (bet * 3)/2
    betForGame.append (bet)


    shuffle(cardList)

    for deal in range (2):
        playerCards.append(first_deal(cardList))
        dealerCards.append(first_deal(cardList))

    print(f"Your cards are: {playerCards}")
    print(f"First dealer card is: {dealerCards[0]}")

    choose_ace_value (playerCards)

    sumOfPlayerPoints = sum(give_number_of_points(playerCards, playerPoints ))
    sumOfDealerPoints = sum(give_number_of_points(dealerCards, dealerPoints ))

    if (sumOfDealerPoints == 22):
        sumOfDealerPoints = 12


    #CHECK IF PLAYER CAN SPLIT

    firstCard = [playerCards[0]]
    secondCard = [playerCards[1]]

    firstCardPunctation = sum((give_number_of_points(firstCard, [])))
    secondCardPunctation = sum((give_number_of_points(secondCard, [])))

    if (firstCardPunctation < 10 or firstCardPunctation == 11):
        if (firstCardPunctation == secondCardPunctation and money - bet >= 0):
            decisionToSplit = input ('Do you want to split? yes/no: ')
        elif (firstCardPunctation == secondCardPunctation and money - bet < 0):
            print ('You have not enough money to split')
            decisionToSplit = 'no'
        else:
            decisionToSplit = 'no'
    elif (firstCardPunctation == 10):       #many cards has value of 10 (check if the player has cards with the same ranks) 
        if ("10" in firstCard[0] and "10" in secondCard[0] and money - bet >= 0):
            decisionToSplit = input ('Do you want to split? yes/no: ')
        elif ("10" in firstCard[0] and "10" in secondCard[0] and money - bet < 0):
            print ('You have not enough money to split')
            decisionToSplit = 'no'
        elif ("Jack" in firstCard[0] and "Jack" in secondCard[0] and money - bet >= 0):
            decisionToSplit = input ('Do you want to split? yes/no: ')
        elif ("Jack" in firstCard[0] and "Jack" in secondCard[0] and money - bet < 0):
            print ('You have not enough money to split')
            decisionToSplit = 'no'
        elif ("Queen" in firstCard[0] and "Queen" in secondCard[0] and money - bet >= 0):
            decisionToSplit = input ('Do you want to split? yes/no: ')
        elif ("Queen" in firstCard[0] and "Queen" in secondCard[0] and money - bet < 0):
            print ('You have not enough money to split')
            decisionToSplit = 'no'
        elif ("King" in firstCard[0] and "King" in secondCard[0] and money - bet >= 0):
            decisionToSplit = input ('Do you want to split? yes/no: ')
        elif ("King" in firstCard[0] and "King" in secondCard[0] and money - bet < 0):
            print ('You have not enough money to split')
            decisionToSplit = 'no'
        else:
            decisionToSplit = 'no'
    else:
        decisionToSplit = 'no'

    # DD

    if (decisionToSplit.upper() != 'YES' and sumOfPlayerPoints != 21):   
        if(money - bet >= 0):
            decisionToDoubleDown = input('Do you want to double your bet? yes/no ')
            if (decisionToDoubleDown.upper() == 'YES'):
                money -= bet
                print (f"""
    You bet another {bet} dolars for split cards!
    On your account remains {money} dolars!
    """)
    else:
        decisionToDoubleDown = 'no'
                   
    # Player GAME

    if (decisionToSplit.upper() == 'YES'):
        money -= bet
        betForGame.append(bet)
        print (f"""
    You bet another {bet} dolars for split cards!
    On your account remains {money} dolars!
    """)
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
        sumOfDealerPoints = make_dealer_move (pointsScoredOnFirstHand, dealerCards, sumOfDealerPoints, newDealersCardPoints, firstCard)
        if (pointsScoredOnSecondHand <= 21):
            print ('FOR second split hand: ') 
        make_dealer_move (pointsScoredOnSecondHand, dealerCards, sumOfDealerPoints, newDealersCardPoints, secondCard)
    else:

        if (decisionToDoubleDown.upper() != 'YES'):
            #player's turn
            pointsScored = play_black_jack(sumOfPlayerPoints, playerCards, newCardPoints)

            #INSURANCE
            firstDealerCard = [dealerCards[0]]
            firstDealerCardPunctation = sum((give_number_of_points(firstDealerCard, [])))
            if (firstDealerCardPunctation == 11):
                if (sumOfPlayerPoints == 21 and len(playerCards) == 2):
                    decisionToInsurance = 'no'
                else:
                    print (f"You can take INSURANCE for half of your bet, beacuse the first dealer card is an ACE")
                    decisionToInsurance = input ("If u want to, write: yes: ")
                    if (decisionToInsurance.upper() == 'YES'):
                        betInsurance = bet /2 # insurance kaska
                        money -= betInsurance
            else:
                decisionToInsurance = 'no'

            #dealer's turn
            if (pointsScored <= 21):
                print('Now let\'s check the dealers cards!')
            make_dealer_move (pointsScored, dealerCards, sumOfDealerPoints, newDealersCardPoints, playerCards)

            # INSURANCE  CHECK
            if (decisionToInsurance.upper() == 'YES'):
                if (sumOfDealerPoints == 21 and len(dealerCards) == 2):
                    print ('Dealer has Blackjack! You decided to take Insurance so we reimburse the costs of the bet!')
                    money += bet
                    money += betInsurance

        elif (decisionToDoubleDown.upper() == 'YES'):
            #player's turn
            newCard.append(first_deal(cardList))
            print (f"Your new card is {newCard}")
            choose_ace_value (newCard)
            newCardPoints = give_number_of_points(newCard, newCardPoints)
            newCardPointsToAdd = sum(newCardPoints)  # need int to add to our points
            playerCards.extend(newCard)
            sumOfPlayerPoints += newCardPointsToAdd
            newCardPointsToAdd = []
            newCardPoints.clear()
            newCard.clear()
            print (f"Your number of points is: {sumOfPlayerPoints}")
            if (sumOfPlayerPoints > 21):
                print ('You lost! Try next time!')
            else:
                print('Now let\'s check the dealers cards!')
            make_dealer_move (sumOfPlayerPoints, dealerCards, sumOfDealerPoints, newDealersCardPoints, playerCards)


    #BET RESULTS

    if (decisionToDoubleDown.upper() == 'YES'):
        betResult =  2 * sum (betForGame)
        money += betResult
        print (f"""After the game your current account is:

        {money} dolars

        """)

    else:
        betResult = sum (betForGame)
        money += betResult
        print (f"""After the game your current account is:

        {money} dolars

        """)

    if (money <= 0):
        print ('You lost your all money!')
        break
    elif (money >0):
        decisionToPlay = input("""Write:
"yes" - if you want still play
"no" - if you want to quit
""")
        if (decisionToPlay.upper() == 'NO'):
            print ('Thank you for your game!')
            break
