import random

cardsuits = ["Heart", "Spade", "Diamond", "Club"]
cardranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cardvaluespoker = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
cardvaluesblackjack = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def shuffledeckofcards(deckofcards):
    # shuffle lists in dictionary syncronously
    zipped = list(zip(deckofcards["cardsuits"], deckofcards["cardranks"], deckofcards["cardnames"], deckofcards["cardvalues"]))
    random.shuffle(zipped)
    deckofcards["cardsuits"], deckofcards["cardranks"], deckofcards["cardnames"], deckofcards["cardvalues"] = zip(*zipped)
    return deckofcards

# returns a dictionary representing a deck of poker cards, shuffled by default
def deckofcardspoker(shuffled = True):
    deckofcards = {
        "cardsuits": [],
        "cardranks": [],
        "cardnames": [],
        "cardvalues": []
    }

    # populate lists in dictionary
    for cardrank in range(0, len(cardranks)):
        for cardsuit in cardsuits:
                deckofcards["cardsuits"].append(cardsuit)
                deckofcards["cardranks"].append(cardranks[cardrank])
                deckofcards["cardnames"].append(cardranks[cardrank] + " of " + cardsuit + "s")
                deckofcards["cardvalues"].append(cardvaluespoker[cardrank])

    if shuffled == True:
        deckofcards = shuffledeckofcards(deckofcards)

    return deckofcards

# returns a dictionary representing a deck of blackjack cards, shuffled by default
def deckofcardsblackjack(shuffled = True):
    deckofcards = {
        "cardsuits": [],
        "cardranks": [],
        "cardnames": [],
        "cardvalues": []
    }

    # populate lists in dictionary
    for cardrank in range(0, len(cardranks)):
        for cardsuit in cardsuits:
                deckofcards["cardsuits"].append(cardsuit)
                deckofcards["cardranks"].append(cardranks[cardrank])
                deckofcards["cardnames"].append(cardranks[cardrank] + " of " + cardsuit + "s")
                deckofcards["cardvalues"].append(cardvaluesblackjack[cardrank])

    if shuffled == True:
        deckofcards = shuffledeckofcards(deckofcards)

    return deckofcards

#print(deckofcardsblackjack(True))
#print(deckofcardspoker(True))