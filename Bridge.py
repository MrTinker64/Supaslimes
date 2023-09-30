from GamePlayers import BridgePlayer
from Deck import Deck
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
    
    def startGame():
        deck = Deck()
        deck.shuffle()

def Ai_turn(player):
    return(random.choice(cards))