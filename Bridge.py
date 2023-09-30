from GamePlayers import BridgePlayer
from Deck import Deck
from Player import Player
import random

class runBridgeGame():
    players = []
    teams = []
    teamIndexes = [[0, 2], [1, 3]]
    def __init__(self, playerNames):
        self.players = [
            BridgePlayer(playerNames[0]),
            BridgePlayer(playerNames[1]),
            BridgePlayer(playerNames[2]),
            BridgePlayer(playerNames[3]),
        ]
        self.teams = [[self.players[0], self.players[2]], [self.players[1], self.players[3]]]

    def initialTeamPointSum(self, teamNumber):
        return self.teams[teamNumber][0].add_points_from_hand() + self.teams[teamNumber][1].add_points_from_hand()

    def outputHand(self, player):
        return ", ".join([f"{card.rank} of {card.suit}" for card in self.players[player].hand])

    def fromContract(self):
        # needs to show declarer other team person's hand and then let them choose suit or no suit and part-score or game
        # put string output into userinput variable
        userInput = input("click suit button")

        userInput = userInput.lower()
        if "no trump" in userInput:
            self.numTricks = 9
        elif "spades" in userInput or "hearts" in userInput:
            self.numTricks = 10
        elif "clubs" in userInput or "diamonds" in userInput:
            self.numTricks = 11

    def trickRound(self, startingPlayer):
        startingPlayer % 4

    def startGame(self):
        deck = Deck()
        while self.initialTeamPointSum(0) == self.initialTeamPointSum(1):
            deck.resetDeck()
            deck.shuffle()
            for player in self.players:
                player.receive_cards(deck.draw(13))
                player.sort_hand()
            self.declaringSide = 0 if self.initialTeamPointSum(0) > self.initialTeamPointSum(1) else 1
            self.declarer = 0 if self.teams[self.declaringSide][0].add_points_from_hand() > self.teams[self.declaringSide][1].add_points_from_hand() else 1
        
        self.fromContract()

        self.trickRound(self.teamIndexes[self.declaringSide][self.declarer] + 1)


    def AI_turn_easy(self,player_number):
        self.players[player_number].play_card(random.choice(self.players[player_number].hand))

if __name__ == "__main__":
    bridgeGame = runBridgeGame(["1", "2", "3", "4"])
    bridgeGame.startGame()
    print(bridgeGame.outputHand(1))
    bridgeGame.AI_turn_easy(1)