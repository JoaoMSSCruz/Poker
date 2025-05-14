from functions.hand_detectors.detect_straight_flush import detect_straight_flush
from functions.hand_detectors.detect_four_of_a_kind import detect_four_of_a_kind
from functions.hand_detectors.detect_full_house import detect_full_house
from functions.hand_detectors.detect_flush import detect_flush
from functions.hand_detectors.detect_straights import detect_straights
from functions.hand_detectors.detect_three_of_a_kind import detect_three_of_a_kind
from functions.hand_detectors.detect_two_pairs_and_pairs import detect_two_pairs_and_pairs
from global_variables.global_var import total_poker_hands, poker_hands_names

def detect_poker_hands(hand):
    poker_hands = []

    suit_division = [[] for _ in range(4)]    
    rank_division = [[] for _ in range(14)]   

    for number in range(hand.get_quantity()-1, -1, -1):
        card = hand.get_card(number)
        card_value = card.get_value() - 1
        card_suit = card.get_suit()

        rank_division[card_value].append(card)

        match card_suit:
            case "Clubs":
                suit_division[0].append(card)
            case "Diamonds":
                suit_division[1].append(card)
            case "Hearts":
                suit_division[2].append(card)
            case "Spades":
                suit_division[3].append(card)

    suit_division = [group for group in suit_division if group]
    rank_division = [group for group in rank_division if group]

    straight_flushes = detect_straight_flush(suit_division)
    royal_flushes = []
    
    for straight_flush in straight_flushes:
        if straight_flush[0].is_ace():
            royal_flushes.append(straight_flush)
            straight_flushes.remove(straight_flush)
    
    poker_hands.append(royal_flushes)
    poker_hands.append(straight_flushes)

    poker_hands.append(detect_four_of_a_kind(rank_division))

    poker_hands.append(detect_full_house(rank_division))

    poker_hands.append(detect_flush(suit_division))

    poker_hands.append(detect_straights(rank_division))

    poker_hands.append(detect_three_of_a_kind(rank_division))

    two_pairs, pairs = detect_two_pairs_and_pairs(rank_division)

    poker_hands.append(two_pairs)
    poker_hands.append(pairs)
    
    if poker_hands == [[] for _ in range(9)]:
        print("There are no Poker Hands in this hand.") 
    else:
        for index, poker_hand in enumerate(poker_hands):
            total_poker_hands[poker_hands_names[index]] += len(poker_hand)
            print("{}: {};".format(poker_hands_names[index], len(poker_hand)))
            if len(poker_hand) > 0:
                for index, pk in enumerate(poker_hand):
                    list = []
                    for card in pk:
                        list.append((card.get_rank(), card.get_suit()))
                    print("{}) {};".format(index+1, list))