def respond(msg) -> str:
    new_message = msg.lower()

    #initializing game
    if msg.content.startswith('initialize game'):
        players_game = new_message.split()
        if players_game[3] == 'bridge' or 'hearts' or 'blackjack' and len(players_game) == 8:
            player1 = players_game[4]
            player2 = players_game[5]
            player3 = players_game[6]
            player4 = players_game[7]
            game = players_game[1]
            return(f'{players_game[1]} Started! Good luck players!')
        else:
            return("Please input a valid game and 4 players!")
        
        if players_game 