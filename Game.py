import Player
import Deck

players = [
    Player(),
    Player(),
    Player(),
    Player(),
]

teams = [[players[0], players[2]], [players[1], players[3]]]

deck = Deck()
deck.shuffle()

for player in players:
    player.recieve_cards(deck.draw(13))




