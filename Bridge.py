from GamePlayers import BridgePlayer
from Deck import Deck
from Player import Player
import random

class runBridgeGame():
    players = []
    teams = []
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

    def startGame(self):
        deck = Deck()
        while self.initialTeamPointSum(0) == self.initialTeamPointSum(1):
            deck.resetDeck()
            deck.shuffle()
            for player in self.players:
                player.receive_cards(deck.draw(13))
                player.sort_hand()
            self.declaringSide = 0 if self.initialTeamPointSum(0) > self.initialTeamPointSum(1) else 1
            self.declarer = self.teams[self.declaringSide][0 if self.teams[self.declaringSide][0].add_points_from_hand() > self.teams[self.declaringSide][1].add_points_from_hand() else 1]
        # needs to show declarer other team person's hand and then let them choose suit or no suit
        


    def AI_turn_easy(self,player_number):
        self.players[player_number].play_card(random.choice(self.players[player_number].hand))

if __name__ == "__main__":
    bridgeGame = runBridgeGame(["1", "2", "3", "4"])
    bridgeGame.startGame()
    print(bridgeGame.outputHand(1))
    bridgeGame.AI_turn_easy(1)