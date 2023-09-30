from Deck import Deck, Card
from Player import Player
import random

class GoFishCard(Card):
    def __init__(self, suit, rank, faceup):
        super().__init__(suit, rank)
        self.faceup = faceup

class GoFishPlayer(Player):
    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def has_card(self, rank):
        for card in self.hand:
            if card.rank == rank:
                return True
        return False

    def get_books(self):
        rank_count = {}
        for card in self.hand:
            rank_count[card.rank] = rank_count.get(card.rank, 0) + 1

        books = [rank for rank, count in rank_count.items() if count == 4]
        for book in books:
            self.hand = [card for card in self.hand if card.rank != book]

        return books
    


class GoFishGame:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.current_player = 0

    def switch_to_next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def play_turn(self, target_player_index, rank):
        if self.current_player == target_player_index:
            return "You can't ask yourself for cards!"

        if not (0 <= target_player_index < len(self.players)):
            return "Invalid player index."

        target_player = self.players[target_player_index]

        if not target_player.has_card(rank):
            return f"{target_player.name} says: Go Fish!"
        else:
            self.players[self.current_player].add_card(target_player.hand.pop(target_player.hand.index(rank)))
            books = self.players[self.current_player].get_books()
            return f"{self.players[self.current_player].name} got a {rank} from {target_player.name}.{' They got a book!' if books else ''}"

    def is_game_over(self):
        return all(len(player.hand) == 0 for player in self.players) or len(self.deck.cards) == 0

# Create players
player1 = Player("Player 1")
player2 = Player("Player 2")

# Create a GoFishGame instance
game = GoFishGame([player1, player2])

# Main game loop
while not game.is_game_over():
    print("\n---")
    print(f"Current Player: {game.players[game.current_player].name}")
    print("Your hand:", ", ".join(str(card) for card in game.players[game.current_player].hand))
    
    target_player_index = int(input("Ask which player (0 or 1): "))
    rank = input("Ask for which rank: ")

    result = game.play_turn(target_player_index, rank)
    print(result)

    if result != "You can't ask yourself for cards!":
        game.switch_to_next_player()

print("\nGame over!")
