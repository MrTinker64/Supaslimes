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

def trick(starting_index):
    trick = []
    lead_suit = ""
    count = 1
    player_to_win_trick = players[0]
    
    reordered_players = players[starting_index:] + players[:starting_index]

    for player in reordered_players:
        rank, of, suit = input(f"{player}, play a card: ").split()
        player.play_card(Card(suit, rank))
        trick.append(Card(suit, rank))
        if count == 1:
            lead_suit = suit
        count += 1
        if suit == lead_suit and Card(suit, rank).numrank > max([card.numrank for card in trick]):
            player_to_win_trick = player
    
    player_to_win_trick.recieve_trick(trick)
    print(trick)
    print("Player who won: ", player_to_win_trick.name)
    trick.clear

trick(players.index(starting_player))
for player in players:
    player.count_points
    print(player.name, player.points)