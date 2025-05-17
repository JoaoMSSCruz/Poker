from classes.game import Game

def main():
    game = Game()

    game.create_game()

    game.inicial_round()
    game.flop_round()
    game.turn_round()
    game.river_round()    


    players = game.get_players()

    player_values = []
    for player in players:
        total_value = player.get_total_value()
        player_values.append(total_value)
    player_values = list(set(player_values))
    player_values = sorted(player_values)


    for c in range(len(player_values)):
        print("\n\nPlace {}:".format(c+1))
        for player in players:
            if player.get_total_value() == player_values[len(player_values) - c - 1]:
                print("\nPlayer {}: {}".format(player.get_player_num(), player.get_total_value()))
                player.show_combinations()

main()
