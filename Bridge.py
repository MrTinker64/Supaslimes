from GamePlayers import BridgePlayer
from Deck import Deck

players = [
    BridgePlayer(),
    BridgePlayer(),
    BridgePlayer(),
    BridgePlayer(),
]

teams = [[players[0], players[2]], [players[1], players[3]]]

deck = Deck()
deck.shuffle()

for player in players:
    player.receive_cards(deck.draw(13))

def Ai_turn(player):
    return(random.choice(player_hand))