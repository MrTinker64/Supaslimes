from GamePlayers import BridgePlayer
from Deck import Deck
from Player import Player
import random

class runBridgeGame():
    players = []
    def __init__(self, playerNames):
        self.players = [
            BridgePlayer(playerNames[0]),
            BridgePlayer(playerNames[1]),
            BridgePlayer(playerNames[2]),
            BridgePlayer(playerNames[3]),
        ]
    teams = [[players[0], players[2]], [players[1], players[3]]]

    def startGame(self):
        deck = Deck()
        while sum(self.teams[0]) == sum(self.teams[1]):
            deck.resetDeck()
            deck.shuffle()
            for player in self.players:
                player.receive_cards(deck.draw(13))
            self.declaringSide = 0 if sum(self.teams[0]) > sum(self.teams[1]) else 1


    def AI_turn(self,player_number):
        self.players[player_number].play_card(random.choice(self.players[player_number].hand))

if __name__ == "__main__":
    bridgeGame = runBridgeGame(["1", "2", "3", "4"])
    bridgeGame.startGame()
    bridgeGame.AI_turn(1)

