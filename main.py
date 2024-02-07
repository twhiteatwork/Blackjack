import os
import deckofcards

deck = deckofcards.deckofcardsblackjack(True)
nextcard = 0

dealercards = []
playercards = []

# returns a dictionary representing next card from deck
def drawcardfromdeck(deck, nextcard):
    returnval = {
        "cardsuit": deck["cardsuits"][nextcard],
        "cardrank": deck["cardranks"][nextcard],
        "cardname": deck["cardnames"][nextcard],
        "cardvalue": deck["cardvalues"][nextcard]
    }

    return returnval

# returns total value of cards in a hand
# Aces count as 11 unless they will cause total to exceed 21 in which case they count as 1
def cardvaluetotal(cards):
    returnval = 0
    acecount = 0

    # add up total value of cards excluding Aces and keep track of the number of Aces
    for card in cards:
        if card["cardrank"] == "Ace":
            acecount += 1
        else:
            returnval += card["cardvalue"]
    
    # there can be at most 1 ace counted as 11 without going bust
    # therefore the contribution of aces to the score is either
    # acecount x 1 or acecount x (11 + (acecount = 1)
    # add the highest of the two possible aces values without exceeding 21
    acesvaluelow = acecount * 1
    acesvaluehigh = acecount * (11 + (acecount - 1))

    if returnval + acesvaluehigh <= 21:
        returnval += acesvaluehigh
    else:
        returnval += acesvaluelow

    return returnval

# returns True if total value of cards exceeds 21, otherwise return False
def isbust(cards):
    if cardvaluetotal(cards) > 21:
        return True
    else:
        return False
    
# returns True if total value of cards is less than or equal to 17
def islteseventeen(cards):
    returnval = False

    return returnval

# returns a string representing cards in a hand
def cardsinhand(cards, hidefirstcard = False):
    returnval = ""

    for cardindex in range(0, len(cards)):
        if cardindex == 0 and hidefirstcard == True:
            # first ouput, append 'Hidden Card' to returnval
            returnval = returnval + "Hidden Card"
        elif cardindex == 0 and hidefirstcard == False:
            # first output, append just the card name to returnval
            returnval = returnval + cards[cardindex]["cardname"]
        else:
            # beyond first output, append a comma and the card name to returnval
            returnval = returnval + ", " + cards[cardindex]["cardname"]

    return returnval

def clearterminal():
    clear = lambda: os.system('cls')
    clear()

def outputtablestate(dealercards, playercards, isplayerturn):
    print("-----\n\n")
    dealercardsinhand = cardsinhand(dealercards, isplayerturn)
    playercardsinhand = cardsinhand(playercards, False)
    print(f"Dealer has: {dealercardsinhand}")
    print(f"You have: {playercardsinhand}")

# game logic
# welcome player
clearterminal()
print("Welcome to blackjack!")
deal = input("Type (Y)es to play or (N)o to exit: ")

# initial deal
if deal == "Y":
    print("Dealing...")
    gameover = False
    dealercards.append(drawcardfromdeck(deck, nextcard))
    nextcard += 1
    playercards.append(drawcardfromdeck(deck, nextcard))
    nextcard += 1
    dealercards.append(drawcardfromdeck(deck, nextcard))
    nextcard += 1
    playercards.append(drawcardfromdeck(deck, nextcard))
    outputtablestate(dealercards, playercards, True)
else:
    print("Exiting...")
    gameover = True

dealerisbust = False
playerisbust = False
hitorstay = "H"
# if player has blackjack following initial deal, game is over
playercardvaluetotal = cardvaluetotal(playercards)
if playercardvaluetotal == 21:
    print("Blackjack!")
    gameover = True
# Loop for player until they bust or stay
while gameover == False and playerisbust == False and hitorstay == "H":
    hitorstay = input("Would you like to (H)it or (S)tay? ")
    if hitorstay == "H": # player elected to hit
        print("You draw.")
        nextcard += 1
        playercards.append(drawcardfromdeck(deck, nextcard))
        outputtablestate(dealercards, playercards, True)
        playerisbust = isbust(playercards)
        playercardvaluetotal = cardvaluetotal(playercards)
        if playerisbust == True:
            print(f"You have busted with a score of {playercardvaluetotal}.")
            print("You lose!")
            gameover = True
    else: # player elected to stay
        print(f"You have stayed with a score of {playercardvaluetotal}")

# Loop for dealer until they bust, tie (push), or win
while gameover == False and dealerisbust == False:
    outputtablestate(dealercards, playercards, False)
    dealercardvaluetotal = cardvaluetotal(dealercards)
    playercardvaluetotal = cardvaluetotal(playercards)
    if dealercardvaluetotal == playercardvaluetotal and dealercardvaluetotal > 17:
        print(f"Dealer has tied your score of {playercardvaluetotal} with a score of {dealercardvaluetotal}.")
        print("Push!")
        gameover = True
    elif dealercardvaluetotal <= playercardvaluetotal and dealercardvaluetotal <= 17:
        #must draw
        print("Dealer draws.")
        nextcard += 1
        dealercards.append(drawcardfromdeck(deck, nextcard))
    else:
        #dealer cannot draw when their score is higher than 17, determine game outcome
        dealerisbust = isbust(dealercards)
        if dealerisbust == True:
            print(f"Dealer has busted with a score of {dealercardvaluetotal}.")
            print("You win!")
            gameover = True
        else:
            print(f"Dealer final score: {dealercardvaluetotal}.")
            print(f"Player final score: {playercardvaluetotal}.")
            if dealercardvaluetotal > playercardvaluetotal:
                print("You lose!")
            else:
                print("You win!")
            gameover = True

# Game has ended
print("Game over.")
