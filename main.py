from classes.deck import Deck
from classes.hand import Hand
from global_variables.global_var import total_poker_hands
from functions.poker_default.create_total_cards import create_total_cards
from functions.poker_default.draw_cards import draw_cards
from functions.hand_detectors.detect_poker_hands import detect_poker_hands
from functions.sorting_alg.choose_sorting_algorithm import choose_sorting_algorithm


def main():
    running = True
    while running:
        deck = Deck(create_total_cards())
        deck.shuffle_cards()

        hand = choose_sorting_algorithm(Hand(draw_cards(deck)))

        detect_poker_hands(hand)
        
        running_second = True
        while running_second:
            choice = int(input("Choose the next action:\n1) Show total number of Poker Hands;\n2) Deal another hand;\n3) Quit;\nChoose one number: "))

            match choice:
                case 1:
                    print("Total number of Poker Hands:")
                    for poker_hand in total_poker_hands.keys():
                        print("{}: {};".format(poker_hand, total_poker_hands[poker_hand]))
                case 2:
                    running_second = False
                case 3:
                    running_second = False
                    running = False


main()
