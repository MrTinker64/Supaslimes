from Deck import Deck

#game code begins
class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = []
        self.dealer_hand = []

    def deal_initial_cards(self):
        self.player_hand = self.deck.draw(2)
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

    def display_hands(self, show_dealer=False):
        #player:
        print("\nPlayer's Hand:")
        for card in self.player_hand:
            print(card)
        print("Total Value:" + str(self.calculate_hand_value(self.player_hand)))
       
        #dealer:
        print("\nDealer's Hand:")
        if show_dealer:
            for card in self.dealer_hand:
                print(card)
            print("Total Value:" + str(self.calculate_hand_value(self.dealer_hand)))
        else:
            print(str(self.dealer_hand[0])) #shows dealer's first card
            print("Total Value: ???") #it's a mystery

#playing
    def play(self):
        #Let the games begin
        self.deal_initial_cards()
        self.display_hands()

        #Player's turn
        while self.calculate_hand_value(self.player_hand) < 21:
            choice = input("Do you want to 'Hit' or 'Stand'? ").lower()
            if choice == 'hit':
                self.player_hand.extend(self.deck.draw(1))
                self.display_hands()
            elif choice == 'stand':
                break
            else:
                print("Invalid choice. Please enter 'Hit' or 'Stand'.")

        # Dealer's turn
        while self.calculate_hand_value(self.dealer_hand) < 17: #dealer needs to hit until they have 17+ points
            self.dealer_hand.extend(self.deck.draw(1))

        # Display the final hands
        self.display_hands(show_dealer=True)

        # Determining the winner winner chicken dinner (bakaw)
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        if player_value > 21:
            print("Player busts! Dealer wins.")
            #player_points+=1
        elif dealer_value > 21:
            print("Dealer busts! Player wins.")
            #dealer_points+=1
        elif player_value > dealer_value:
            print("Player wins!")
            #player_points+=1
        elif dealer_value > player_value:
            print("Dealer wins.")
            #dealer_points+=1
        else:
            print("It's a tie!")
            #player_points+=0.5
            #dealer_points+=0.5
#player_points=0
#dealer_points=0
if __name__ == "__main__":
    game = Blackjack()
    game.play()
    #print("player points: " + str(player_points))
    #print("dealer points: " + str(dealer_points))