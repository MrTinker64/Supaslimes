from Deck import Deck
#game code begins
class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1_hand = []
        self.player2_hand = []
        self.player3_hand = []
        self.player4_hand = []
        self.dealer_hand = []

    def deal_initial_cards(self):
        self.player1_hand = self.deck.draw(2)
        self.player2_hand = self.deck.draw(2)
        self.player3_hand = self.deck.draw(2)
        self.player4_hand = self.deck.draw(2)
        self.dealer_hand = self.deck.draw(2)
    
    def get_card_value(self, card):
        if card.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif card.rank == 'Ace':
            return 11
        else:
            return int(card.rank)

    def calculate_hand_value(self, hand):
        total_value = sum(self.get_card_value(card) for card in hand)
        num_aces = sum(1 for card in hand if card.rank == 'Ace')

        #changes ace value to 1 from 11 if needed to keep total value under 21
        while num_aces > 0 and total_value > 21:
            total_value -= 10
            num_aces -= 1

        return total_value

    def display_hands(self, player=None, show_dealer=False):
        if player is not None:
            for card in self.var(player)_hand:
                print(card)
        elif show_dealer:
            for card in self.dealer_hand:
                print(card)
            print("Total Value:" + str(self.calculate_hand_value(self.dealer_hand)))
        else:
            print(str(self.dealer_hand[0])) #shows dealer's first card
            print("Total Value: ???") #it's a mystery
    
    def player_move(player):
        if self.calculate_hand_value(self.var(player)_hand) < 21:
            self.display_hands(self, player)
            choice = input(str(player) + ", do you want to 'Hit' or 'Stand'? ")
            if choice == 'Hit':
                self.var(player)_hand.extend(self.deck.draw(1))
                self.display_hands(self, player)
            elif choice == 'Stand':
                break
            else:
                print("Invalid choice. Please enter 'Hit' or 'Stand'.")
    
    def dealer_move():
        if self.calculate_hand_value(self.dealer_hand) < 17: #dealer needs to hit until they have 17+ points
            self.dealer_hand.extend(self.deck.draw(1))

#playing
    def play(self):
        current_player=#THING -- TO ADD
        #Let the games begin
        self.deal_initial_cards()

        #Players' turns
        while self.calculate_hand_value(self.player1_hand) < 21 or self.calculate_hand_value(self.player2_hand) < 21 or self.calculate_hand_value(self.player3_hand) < 21 or self.calculate_hand_value(self.player4_hand) < 21:
            player_move(self.player1) #FIX THIS SO THE INPUT IS VALID
            player_move(self.player2)
            player_move(self.player3)
            player_move(self.player4)
            dealer_move()

        # Display the final hands
        self.display_hands(self, self.player1)
        self.display_hands(self, self.player2)
        self.display_hands(self, self.player3)
        self.display_hands(self, self.player4, True)
        

        # Determining the winner winner chicken dinner (bakaw)
        player1_value = self.calculate_hand_value(self.player1_hand)
        player2_value = self.calculate_hand_value(self.player2_hand)
        player3_value = self.calculate_hand_value(self.player3_hand)
        player4_value = self.calculate_hand_value(self.player4_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        if player1_value > 21:
            print("Player busts! Dealer wins.")
        elif dealer_value > 21:
            print("Dealer busts! Player wins.")
        elif player1_value > dealer_value:
            print("Player wins!")
        elif dealer_value > player1_value:
            print("Dealer wins.")
        else:
            print("It's a tie!")
if __name__ == "__main__":
    game = Blackjack()
    game.play()