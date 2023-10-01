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
        if player_number is not None:
            for card in self.var(player)_hand
                print(card)
        elif show_dealer:
            self.dealer.show_hand()
        else:
            self.dealer.show_one_card()

#playing
    def play(self):
        #Let the games begin
        self.deal_initial_cards()
        self.display_hands()

        #Player's turn
        while self.calculate_hand_value(self.player1_hand) < 21: #MAKE IT ASK P1, P2, P3, P4, P1...
    
            choice = input("Do you want to 'Hit' or 'Stand'? ")=
            if choice == 'Hit':
                self.player1_hand.extend(self.deck.draw(1))
                self.display_hands()
            elif choice == 'Stand':
                break
            else:
                print("Invalid choice. Please enter 'Hit' or 'Stand'.")

        # Dealer's turn
        while self.calculate_hand_value(self.dealer_hand) < 17: #dealer needs to hit until they have 17+ points
            self.dealer_hand.extend(self.deck.draw(1))

        # Display the final hands
        self.display_hands(show_dealer=True)

        # Determining the winner winner chicken dinner (bakaw)
        player1_value = self.calculate_hand_value(self.player1_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        global player1_points
        global dealer_points

        if player1_value > 21:
            print("Player busts! Dealer wins.")
            player1_points+=1
        elif dealer_value > 21:
            print("Dealer busts! Player wins.")
            dealer_points+=1
        elif player1_value > dealer_value:
            print("Player wins!")
            player1_points+=1
        elif dealer_value > player1_value:
            print("Dealer wins.")
            dealer_points+=1
        else:
            print("It's a tie!")
            player1_points+=0.5
            dealer_points+=0.5
player1_points=0
dealer_points=0
play_again="Yes"
while play_again=="Yes":
    if __name__ == "__main__":
        game = Blackjack()
        game.play()
        print("player points: " + str(player1_points))
        print("dealer points: " + str(dealer_points))
        play_again=input("Do you want to play again ('Yes' or 'No')?")
print("dealer: " + str(dealer_points))
print("player: " + str(player1_points))
if dealer_points>player1_points:
    print("DEALER WINS, BOZO!!!")
elif dealer_points==player1_points:
    print("UNSATISFYING TIE (a bit lame)")
else:
    print("CONGRATULATIONS!!! YOU WIN!!!")