from GamePlayers import HeartsPlayer
from Deck import Deck, Card
import random

players = [
    HeartsPlayer("Alice"),
    HeartsPlayer("Bob"),
    HeartsPlayer("Charlie"),
    HeartsPlayer("David")
]

deck = Deck()
deck.shuffle()

for player in players:
    player.receive_cards(deck.draw(13))
    player.sort_hand()
    
starting_player = players[random.randrange(4)]

starting_index = players.index(starting_player)
reordered_players = players[starting_index:] + players[:starting_index]

for player in reordered_players:
    rank, of, suit = input(f"{player}, play a card: ").split()
    player.play_card(Card(suit, rank))
