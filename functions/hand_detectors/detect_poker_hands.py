from functions.hand_detectors.detect_straight_flush import detect_straight_flush
from functions.hand_detectors.detect_four_of_a_kind import detect_four_of_a_kind
from functions.hand_detectors.detect_full_house import detect_full_house
from functions.hand_detectors.detect_flush import detect_flush
from functions.hand_detectors.detect_straights import detect_straights
from functions.hand_detectors.detect_three_of_a_kind import detect_three_of_a_kind
from functions.hand_detectors.detect_two_pairs_and_pairs import detect_two_pairs_and_pairs
from functions.hand_detectors.detect_high_cards import detect_high_cards

def detect_poker_hands(hand):
    poker_hands = [[] for _ in range(10)] 

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
    
    poker_hands[0] = royal_flushes
    if royal_flushes != []:
        return poker_hands

    poker_hands[1] = straight_flushes
    if straight_flushes != []:
        return poker_hands

    poker_hands[2] = detect_four_of_a_kind(rank_division)
    if poker_hands[2] != []:
        poker_hands[9] = detect_high_cards(rank_division, 1)
        return poker_hands

    poker_hands[3] = detect_full_house(rank_division)
    if poker_hands[3] != []:
        return poker_hands

    poker_hands[4] = detect_flush(suit_division)
    if poker_hands[4] != []:
        return poker_hands

    poker_hands[5] = detect_straights(rank_division)
    if poker_hands[5] != []:
        return poker_hands

    poker_hands[6] = detect_three_of_a_kind(rank_division)
    if poker_hands[6] != []:
        poker_hands[9] = detect_high_cards(rank_division, 2)
        return poker_hands

    two_pairs, pairs = detect_two_pairs_and_pairs(rank_division)
    poker_hands[7] = two_pairs
    if two_pairs != []:
        poker_hands[9] = detect_high_cards(rank_division, 1)
        return poker_hands

    poker_hands[8] = pairs
    if pairs != []:
        poker_hands[9] = detect_high_cards(rank_division, 3)
        return poker_hands

    poker_hands[9] = detect_high_cards(rank_division, 5)
    
    return poker_hands