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

def check_suit(cards, suit):
    list = []
    for card in cards:
        if card.suit == suit:
            list.append(card)
    return list

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
    
    print(trick)
    trick = check_suit(trick, lead_suit)
    highest_card_value = max(card.numrank for card in trick if card.suit == lead_suit)
    highest_card = Card("Clubs", "2")
    for card in trick:
        if card.numrank == highest_card_value:
            highest_card = card
    print(f"{players[starting_index].name} started")
    player_to_win_trick = players[trick.index(highest_card)]
    # player_to_win_trick.recieve_trick(trick)
    print(trick)
    print(f"{player_to_win_trick.name} won the trick")
    trick.clear
    count = 1

trick(players.index(starting_player))
# for player in players:
#     player.count_points
#     print(player.name, player.points)
    
# of Spades