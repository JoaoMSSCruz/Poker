from classes.player import Player

def draw_cards_player(deck, players_number):
    players = []
    for player_num in range(players_number):
        player_cards = deck.draw_cards(2)
        deck.remove_cards(player_cards)
        players.append(Player(player_cards, player_num+1))
    return players
    