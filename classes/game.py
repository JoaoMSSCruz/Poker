from classes.deck import Deck
from global_variables.global_var import ranks, suits
from classes.card import Card
from classes.player import Player
from global_variables.hand_stats import *
import random

class Game:
    def __init__(self):
        self.state = ""
        self.deck = []
        self.players = []
        self.game_cards = []

    def get_state(self):
        return self.state

    def get_deck(self):
        return self.deck
    
    def get_players(self):
        return self.players

    def get_game_cards(self):
        return self.game_cards

    def get_player(self, number):
        return self.get_players()[number]

    def get_player_action(self):
        return self.player_action

    def set_player_action(self, player_id):
        self.player_action = player_id

    def set_state(self, state):
        self.state = state

    def set_deck(self, deck):
        self.deck = deck

    def set_players(self, players):
        self.players = players

    def remove_player(self, player):
        players = self.get_players()
        players.remove(player)
    
    def add_game_cards(self, cards):
        self.game_cards = cards

    def create_total_cards(self):
        total_cards = []
        for value, rank in enumerate(ranks):
            for suit in suits:
                card = Card(rank, suit, value+1)
                total_cards.append(card)
        return total_cards

    def create_game(self):
        deck = Deck(self.create_total_cards())
        deck.shuffle_cards()
        self.set_deck(deck)

    def draw_cards_player(self):
        players_number = int(input("How many players will play? "))

        players = []
        for player_num in range(players_number):
            player_cards = self.get_deck().draw_cards(2)
            players.append(Player(player_cards, player_num+1))

        self.set_players(players)

    def draw_game_cards(self, number):
        self.add_game_cards(self.get_deck().draw_cards(number))

    def handle_round(self, current_hand):
        current_player = 0
        check_counter = 0

        print("Round:")
        while True:
            if current_player == len(self.get_players()):
                current_player = 0

            player = self.get_player(current_player)

            if player.get_player_state() == "fold":
                player.set_total_value(0)
                current_player += 1
                continue

            player_id = player.get_player_num()

            # Avaliação da mão
            if player.get_total_value() < current_hand[0]:
                player.set_hand_strenght("weak")
                probabilities = weak_hand
            elif player.get_total_value() <= current_hand[1]:
                player.set_hand_strenght("medium")
                probabilities = medium_hand
            else:
                player.set_hand_strenght("hard")
                probabilities = strong_hand

            action = random.choices(actions, probabilities)[0]

            # Processar ação
            if action == "fold" and self.get_state() == "":
                action = "check"
                self.set_player_action(player_id)
                check_counter += 1
            elif action == "fold" and self.get_state() == "check":
                action = "check"
                check_counter += 1
            elif action == "fold":
                player.set_player_state("fold")
                player.set_total_value(0)
                # Não incrementa o check_counter!
            elif action == "raise" and self.get_state() == "raise":
                action = "check"
                check_counter += 1
            elif action == "raise":
                self.set_state("raise")
                self.set_player_action(player_id)
                check_counter = 1  # reinicia contador
            elif action == "check" and self.get_state() not in ["raise", "check"]:
                self.set_player_action(player_id)
                check_counter += 1
            else:
                check_counter += 1  # ação neutra (como check com state já existente)

            print("Player {}: {};".format(player_id, action))
            current_player += 1

            # Verificação de fim de ronda (todos os ativos já agiram)
            active_players = [p for p in self.get_players() if p.get_player_state() != "fold"]
            if check_counter >= len(active_players):
                self.set_player_action(0)
                self.set_state("")
                break


    def inicial_round(self):
        self.draw_cards_player()
        for player in self.get_players():
            player.add_cards(self.get_game_cards())
            player.update_poker_hands()

        print("Initial Round:")
        self.handle_round(inicial_hand)
            
    def flop_round(self):
        self.draw_game_cards(3)

        for player in self.get_players():
            player.add_cards(self.get_game_cards())
            player.update_poker_hands()

        print("Flop Round:")
        self.handle_round(flop)

    def turn_round(self):
        self.draw_game_cards(1)

        for player in self.get_players():
            player.add_cards(self.get_game_cards())
            player.update_poker_hands()

        print("Turn Round:")
        self.handle_round(turn)

    def river_round(self):
        self.draw_game_cards(1)

        for player in self.get_players():
            player.add_cards(self.get_game_cards()) 
            player.update_poker_hands()

        print("River Round:")
        self.handle_round(river)