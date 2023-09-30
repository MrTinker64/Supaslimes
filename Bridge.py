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
    declaringSide = 0

    def startGame(self):
        deck = Deck()
        
        deck.shuffle()
        for player in self.players:
            player.receive_cards(deck.draw(13))
        self.declaringSide = 0 if sum(self.teams[0]) > sum(self.teams[1]) else 1


    def AI_turn(player):
        Player.play_card(player, random.choice(Player.cards))
