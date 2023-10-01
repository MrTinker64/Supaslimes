from Player import Player
import random
from Deck import Card
from BotInterface import discordPrint

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
    
    async def playTrick(self, suitIn):
        if suitIn == "n":
            # kyle have them pick a card from their hand
            print(self)
            await discordPrint(self)
            
            while True:
                try:
                    rank, of, suit = input(f"{self.name}, play a card: ").split()
                    cardToPlay = self.play_card(Card(suit, rank))
                    if cardToPlay:
                        return cardToPlay
                    else:
                        print("sorry that card is not valid")
                        await discordPrint("sorry that card is not valid")
                except:
                    pass
                
                
        else:
            # have them pick a card from their hand
            # require them to pick a card with suit matching suit variable
            print(self)
            await discordPrint(self)
            
            while True:
                try:
                    rank, of, suit = input(f"{self.name}, play a card: ").split()
                    cardToPlay = self.play_card(Card(suit, rank))
                    if cardToPlay and ((not any([card.suit  == suitIn for card in self.hand])) or (cardToPlay.suit == suitIn and any([card.suit  == suitIn for card in self.hand]))):
                        return cardToPlay
                    else:
                        print("sorry that card is not valid")
                        await discordPrint("sorry that card is not valid")
                except:
                    pass

        

                
class HeartsPlayer(Player):
    pass
