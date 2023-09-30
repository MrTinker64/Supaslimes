from Player import Player
import random

class BridgePlayer(Player):
    def add_points_from_hand(self):
        initialPoints = 0
        for card in self.hand:
            if card.rank == "Ace":
                initialPoints += 4
            elif card.rank == "King":
                initialPoints += 3
            elif card.rank == "Queen":
                initialPoints += 2
            elif card.rank == "Jack":
                initialPoints += 1
        return initialPoints
    
    def fromContract(self):
        # needs to show declarer other team person's hand and then let them choose suit or no suit and part-score or game
        # put string output into userinput variable
        userInput = input("enter suit (S, H, C, D) or n for no suit: ")

        userInput = userInput.lower().strip()
        suit = "None"
        if "s" == userInput:
            suit = "Spades"
        elif "c" == userInput:
           suit = "Clubs"
        elif "h" == userInput:
           suit = "Hearts"
        elif "d" == userInput:
           suit = "Diamonds"
        return suit
    
    def playTrick(self, suit):
        if suit == "n":
            # kyle have them pick a card from their hand
            trickCard = random.choice(self.hand)

            return trickCard
        else:
            trickCard = random.choice(self.hand)
            # have them pick a card from their hand
            # require them to pick a card with suit matching suit variable
            return trickCard

        

                
class HeartsPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.tricks = []
    
    def recieve_trick(self, trick):
        self.tricks += trick
        
    def count_points(self):
        for card in self.tricks:
            if card.suit == "Heart":
                self.points += 1
            if card == "Queen of Spades":
                self.points += 13
            self.tricks.clear()
