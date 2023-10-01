from Bridge import runBridgeGame

async def respond(msg):
    new_message = msg.lower().split()

    # Verify if the message format is correct
    if len(new_message) != 8:
        return "Please input a valid game and 4 players!"
    
    game, action, game_type, player1, player2, player3, player4 = new_message[1:8]
    
    if action == 'initialize' and game_type in ['bridge', 'hearts', 'blackjack']:
        bridgeGame = runBridgeGame([player1, player2, player3, player4])
        await bridgeGame.startGame()
        return f'{game_type.capitalize()} Game Started! Good luck players!'
    
    return "Please input a valid game and 4 players!"

if __name__ == "__main__":
    test = respond("$bridge initialize game bridge a b c d")
