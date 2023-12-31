from GamePlayers import HeartsPlayer
from Deck import Deck, Card
import random

class HeartsGame():
    def __init__(self, playerNames):
        self.players = [
            HeartsPlayer(playerNames[0]),
            HeartsPlayer(playerNames[1]),
            HeartsPlayer(playerNames[2]),
            HeartsPlayer(playerNames[3]),
        ]

    def run_game(self):
        deck = Deck()
        deck.shuffle()

        for player in self.players:
            player.receive_cards(deck.draw(13))
            player.sort_hand()
            
        starting_player = self.players[random.randrange(4)]
        
        first_player = self.trick(self.players.index(starting_player))

        for i in range(12):
            first_player = self.trick(self.players.index(first_player))

        for player in self.players:
            print(player.name, player.points)

    def check_suit(self, cards, suit):
        list = []
        for card in cards:
            if card.suit == suit:
                list.append(card)
        return list

    def count_points_for(self, player, trick):
        for card in trick:
            if card.suit == "Hearts":
                player.add_points(1)
            if card.suit == "Spades" and card.rank == "Queen":
                player.add_points(13)

    def get_highest_card(self, trick, lead_suit):
        highest_card_value = max(card.numrank for card in trick if card.suit == lead_suit)
        for card in trick:
            if card.numrank == highest_card_value:
                return card

    def trick(self, starting_index):
        trick = []
        lead_suit = ""
        count = 1
        player_to_win_trick = self.players[0]
        
        reordered_players = self.players[starting_index:] + self.players[:starting_index]

        for player in reordered_players:
            # rank, of, suit = input(f"{player}, play a card: ").split()
            played_card = random.choice(player.hand)
            rank, suit = played_card.rank, played_card.suit
            player.play_card(Card(suit, rank))
            trick.append(Card(suit, rank))
            if count == 1:
                lead_suit = suit
            count += 1
        
        print(trick)
        print([player.name for player in reordered_players])
        suited_trick = self.check_suit(trick, lead_suit)
        highest_card = self.get_highest_card(suited_trick, lead_suit)
        player_to_win_trick = reordered_players[trick.index(highest_card)]
        print(f"{player_to_win_trick.name} won the trick")
        self.count_points_for(player_to_win_trick, trick)
        trick.clear
        count = 1
        return player_to_win_trick  
        
    # of Spades