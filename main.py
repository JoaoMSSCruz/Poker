from classes.deck import Deck
from functions.poker_default.create_total_cards import create_total_cards
from functions.poker_default.draw_cards_player import draw_cards_player
from functions.poker_default.draw_cards_game import draw_cards_game

def main():
    deck = Deck(create_total_cards())
    deck.shuffle_cards()

    players_number = int(input("How many players will play? "))

    players = draw_cards_player(deck, players_number)

    game_cards = draw_cards_game(deck)

    for player in players:
        player.add_cards(game_cards)
        player.update_poker_hands()

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
