from Bridge import runBridgeGame

async def respond(msg):
    print("test")
    # new_message = msg.lower()
    new_message = "$bridge initialize game bridge a b c d"
    split_message = new_message.split()
    #initializing game

    #test
    # bridgeGame = runBridgeGame(["1", "2", "3", "4"])
    # await bridgeGame.startGame()

    if split_message[1] + split_message[2] == ('initialize game'):
        if split_message[3] == 'bridge' or 'hearts' or 'blackjack' and len(split_message) == 8:
            player1 = split_message[4]
            player2 = split_message[5]
            player3 = split_message[6]
            player4 = split_message[7]
            game = split_message[3]
            return(f'{split_message[3]} Started! Good luck players!')
    else:
        return("Please input a valid game and 4 players!")


if __name__ == "__main__":
    test = respond("$bridge initialize game bridge a b c d")
