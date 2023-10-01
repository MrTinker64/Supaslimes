from GamePlayers import BridgePlayer
from Deck import Deck
from Player import Player
import random
from BotInterface import discordPrint

class runBridgeGame():
    players = []
    teams = []
    teamIndexes = [[0, 2], [1, 3]]
    def __init__(self, playerNames):
        self.players = [
            BridgePlayer(playerNames[0]),
            BridgePlayer(playerNames[1]),
            BridgePlayer(playerNames[2]),
            BridgePlayer(playerNames[3]),
        ]
        self.teams = [[self.players[0], self.players[2]], [self.players[1], self.players[3]]]

    def initialTeamPointSum(self, teamNumber):
        return self.teams[teamNumber][0].add_points_from_hand() + self.teams[teamNumber][1].add_points_from_hand()

    def outputHand(self, player):
        return ", ".join([f"{card.rank} of {card.suit}" for card in self.players[player].hand])

    def trickRound(self, startingPlayer):
        card1 = self.players[startingPlayer % 4].playTrick("n")
        previousSuit = card1.suit
        card2 = self.players[(startingPlayer + 1) % 4].playTrick(previousSuit)
        card3 = self.players[(startingPlayer + 2) % 4].playTrick(previousSuit)
        card4 = self.players[(startingPlayer + 3) % 4].playTrick(previousSuit)
        playerOrder = [self.players[(startingPlayer) % 4], self.players[(startingPlayer + 1) % 4], self.players[(startingPlayer + 2) % 4], self.players[(startingPlayer + 3) % 4]]
        cardsPlayed = [card1, card2, card3, card4]
        cardValues = []
        for card in cardsPlayed:
            if card.suit == self.alephSuit:
                cardValues.append(Deck.RANKS.index(card.rank) + 20)
            elif card.suit == previousSuit:
                cardValues.append(Deck.RANKS.index(card.rank))
            else:
                cardValues.append(0)
        playerOrder[cardValues.index(max(cardValues))].add_points(1)
        
    def gameOver(self):
        return any([len(player.hand) == 0 for player in self.players])
        

    async def startGame(self):
        deck = Deck()
        while self.initialTeamPointSum(0) == self.initialTeamPointSum(1):
            deck.resetDeck()
            deck.shuffle()
            for player in self.players:
                player.receive_cards(deck.draw(13))
                player.sort_hand()
            self.declaringSide = 0 if self.initialTeamPointSum(0) > self.initialTeamPointSum(1) else 1
            self.declarer = 0 if self.teams[self.declaringSide][0].add_points_from_hand() > self.teams[self.declaringSide][1].add_points_from_hand() else 1
        
        while not self.gameOver():
            self.alephSuit = self.teams[self.declaringSide][self.declarer].fromContract()
            self.trickRound(self.teamIndexes[self.declaringSide][self.declarer] + 1)
        
        highestScore = max([player.points for player in self.players])
        winners = [player for player in self.players if player.points == highestScore]

        # print out winners to discord
        print()
        print("Winners: ")
        await discordPrint("Winners: ")
        for winner in winners:
            print(f"{winner.name} won with {winner.points} points!!")
            await discordPrint(f"{winner.name} won with {winner.points} points!!")


    def AI_turn_easy(self,player_number):
        self.players[player_number].play_card(random.choice(self.players[player_number].hand))

if __name__ == "__main__":
    bridgeGame = runBridgeGame(["1", "2", "3", "4"])
    test = bridgeGame.startGame()