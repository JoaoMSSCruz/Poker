from  classes.card import Card
from classes.deck import Deck
from classes.hand import Hand
from global_variables.global_var import ranks, suits, total_poker_hands
    

def create_total_cards():
    total_cards = []
    for value, rank in enumerate(ranks):
        for suit in suits:
            card = Card(rank, suit, value+1)
            total_cards.append(card)
    return total_cards

def draw_cards(deck):
    while True:
        number_of_cards_to_be_drawn = int(input("How many cards would you like to draw? "))
        if 3 <= number_of_cards_to_be_drawn <= 15:
            return deck.draw_cards(number_of_cards_to_be_drawn)
        else:
            print("Please choose a number between 3 and 15.")

def heapify(hand, hand_size, i):
    largest = i          # Assume que o maior é a raiz
    left = 2 * i + 1      # Índice do filho à esquerda
    right = 2 * i + 2     # Índice do filho à direita

    # Se o filho da esquerda for maior que a raiz
    if left < hand_size and hand.get_card_value(left) > hand.get_card_value(largest):
        largest = left

    # Se o filho da direita for maior que o maior até agora
    if right < hand_size and hand.get_card_value(right) > hand.get_card_value(largest):
        largest = right

    # Se o maior não for a raiz
    if largest != i:
        hand.switch_cards(i, largest)
        heapify(hand, hand_size, largest)  # Aplica heapify recursivamente

def heap_sort(hand):
    hand_size = hand.get_quantity()
        
    # 1. Constrói o max-heap (reorganiza a lista)
    for index in range(hand_size // 2 - 1, -1, -1):
        heapify(hand, hand_size, index)

    # 2. Extrai elementos um a um
    for size in range(hand_size - 1, 0, -1):
        hand.switch_cards(0, size)
        heapify(hand, size, 0)  # Reorganiza o heap com os restantes

    return hand

def binary_search(hand, val, start, end):
    while start < end:
        mid = (start + end) // 2
        if hand.get_card_value(mid) < val:
            start = mid + 1
        else:
            end = mid
    return start

def binary_insertion_sort(hand):
    for index in range(1, hand.get_quantity()):
        val = hand.get_card_value(index)
        pos = binary_search(hand, val, 0, index)
        hand = Hand(hand.get_cards(0, pos) + [hand.get_card(index)] + hand.get_cards(pos, index) + hand.get_cards(index+1, hand.get_quantity()))

    return hand

def merge(left_half, right_half):

    result = []
    i = j = 0
    
    # Junta de forma ordenada
    while i < left_half.get_quantity() and j < right_half.get_quantity():
        if left_half.get_card_value(i) <= right_half.get_card_value(j):
            result.append(left_half.get_card(i))
            i += 1
        else:
            result.append(right_half.get_card(j))
            j += 1

    # Adiciona os restantes elementos
    result.extend(left_half.get_cards(i, left_half.get_quantity()))
    result.extend(right_half.get_cards(j, right_half.get_quantity()))

    return Hand(result)

def merge_sort(hand):

    if hand.get_quantity() <= 1:
        return hand

    # Divide
    mid = hand.get_quantity() // 2
    left_half = merge_sort(Hand(hand.get_cards(0, mid)))
    right_half = merge_sort(Hand(hand.get_cards(mid, hand.get_quantity())))

    # Conquista (fusão)
    return merge(left_half, right_half)

def quick_sort(hand, low, high):
    if low < high:
        pivot_index = partition(hand, low, high)
        quick_sort(hand, low, pivot_index - 1)
        quick_sort(hand, pivot_index + 1, high)

def partition(hand, low, high):
    pivot = hand.get_card_value(high)
    i = low - 1
    for j in range(low, high):
        if hand.get_card_value(j) <= pivot:
            i += 1
            hand.switch_cards(i, j)
    hand.switch_cards(i + 1, high)
    return i + 1

def choose_sorting_algorithm(hand):
    while True:
        number = int(input("Choose the sorting algorithm:\n 1) Heap Sort;\n 2) Binary Insertion Sort;\n 3) Merge Sort;\n 4) Quick Sort;\n Choose one number: "))
        match number:
            case 1:
                hand = heap_sort(hand)
                break
            case 2:
                hand = binary_insertion_sort(hand)
                break
            case 3:
                hand = merge_sort(hand)
                break
            case 4:
                quick_sort(hand, 0, hand.get_quantity() - 1)
                break
            case _:
                print("Please type a number between 1 and 4.")

    return hand

def only_one_ace_per_hand(poker_hand):
    card_record = []
    for card in poker_hand:
        card_rep = (card.get_rank(), card.get_suit())
        if card_rep in card_record:
            return False
        card_record.append(card_rep)
    return True

def detect_straight_flush(suit_division):
    straight_flushes = []

    for suit in suit_division:
        possible_straight_flush = []
        if len(suit) < 5:
            continue
        for card in suit:
            if possible_straight_flush == [] or card.get_value() != possible_straight_flush[-1].get_value() - 1:
                possible_straight_flush = [card]
            else:
                if len(possible_straight_flush) == 4:
                    possible_straight_flush.append(card)
                    if only_one_ace_per_hand(possible_straight_flush):
                        for card_participant in possible_straight_flush:
                            card_participant.set_used()
                        straight_flushes.append(possible_straight_flush)
                    possible_straight_flush = []
                else:
                    possible_straight_flush.append(card)

    return straight_flushes

def detect_four_of_a_kind(rank_division):
    four_of_a_kinds = []

    for rank in rank_division:
        possible_four_of_a_kind = []
        if len(rank) < 4:
            continue
        for card in rank:
            if possible_four_of_a_kind == [] or card.get_rank() != possible_four_of_a_kind[-1].get_rank():
                possible_four_of_a_kind = [card]
            elif card.get_used():
                possible_four_of_a_kind = []
            else:
                if len(possible_four_of_a_kind) == 3:
                    possible_four_of_a_kind.append(card)
                    for card_participant in possible_four_of_a_kind:
                        card_participant.set_used()
                        rank.remove(card_participant)
                    four_of_a_kinds.append(possible_four_of_a_kind)
                    possible_four_of_a_kind = []
                else:
                    possible_four_of_a_kind.append(card)

    return four_of_a_kinds

def detect_full_house(rank_division):
    full_houses = []
    three_of_a_kinds = []
    pairs = []
    for rank in reversed(rank_division):
        possible_member = []
        if len(rank) < 2:
            continue
        for card in rank:
            if not card.get_used():
                possible_member.append(card)
        if len(possible_member) == 3:
            three_of_a_kinds.append(possible_member)
            pairs.append([possible_member[0], possible_member[1]])
        elif len(possible_member) == 2:
            pairs.append(possible_member)
    for three_of_a_kind in three_of_a_kinds:
        rank = three_of_a_kind[0].get_rank()
        for pair in pairs:
            if only_one_ace_per_hand(three_of_a_kind+pair):
                if pair[0].get_rank() != rank:
                    for card in three_of_a_kind:
                        card.set_used()
                    for card in pair:
                        card.set_used()
                    full_houses.append(three_of_a_kind+pair)
                    three_of_a_kinds.remove(three_of_a_kind)
                    pairs.remove(pair)
                    pairs.remove([three_of_a_kind[0], three_of_a_kind[1]])
                    break

    return full_houses

def detect_flush(suit_division):
    flushes = []

    for suit in suit_division:
        possible_flush = []
        if len(suit) < 5:
            continue
        for card in suit:
            if not card.get_used():
                possible_flush.append(card)
                if len(possible_flush) == 5:
                    if only_one_ace_per_hand(possible_flush):
                        for card_participant in possible_flush:
                            card_participant.set_used()
                        flushes.append(possible_flush)
                    possible_flush = []
    
    return flushes

def detect_straights(rank_division):
    straights = []
    capable_cards = []

    for rank in reversed(rank_division):
        not_used_cards = []
        for card in rank:
            if card.get_value():
                not_used_cards.append(card)
                
        capable_cards.append(not_used_cards)
        
    if len(capable_cards) > 4:
        number = 0
        while number <= len(capable_cards) - 5:
            group = capable_cards[number]
            for card in group:
                try:
                    # Garante que todos os grupos têm pelo menos uma carta
                    if not all(len(capable_cards[number + i]) > 0 for i in range(5)):
                        continue
                    if not all(len(capable_cards[number + i]) > 0 and not capable_cards[number + i][0].get_used() for i in range(5)):
                        continue
                    card1 = capable_cards[number+1][0]
                    card2 = capable_cards[number+2][0]
                    card3 = capable_cards[number+3][0]
                    card4 = capable_cards[number+4][0]

                    value = card.get_value()
                    if value == card1.get_value() + 1 == card2.get_value() + 2 == card3.get_value() + 3 == card4.get_value() + 4:
                        straights.append([card, card1, card2, card3, card4])
                        card.set_used()
                        card1.set_used()
                        card2.set_used()
                        card3.set_used()
                        card4.set_used()

                        capable_cards[number+1].remove(card1)
                        capable_cards[number+2].remove(card2)
                        capable_cards[number+3].remove(card3)
                        capable_cards[number+4].remove(card4)
                        capable_cards[number].remove(card)

                        # Limpa listas vazias
                        capable_cards = [group for group in capable_cards if group]
                        
                        # Recomeça do início
                        number = -1
                        break
                except IndexError:
                    pass
            number += 1
    
    return straights

def detect_three_of_a_kind(rank_division):
    three_of_a_kinds = []

    for rank in rank_division:
        possible_three_of_a_kind = []
        if len(rank) < 3:
            continue
        for card in rank:
            if possible_three_of_a_kind == [] or card.get_rank() != possible_three_of_a_kind[-1].get_rank():
                possible_three_of_a_kind = [card]
            elif card.get_used():
                possible_three_of_a_kind = []
            else:
                if len(possible_three_of_a_kind) == 2:
                    possible_three_of_a_kind.append(card)
                    for card_participant in possible_three_of_a_kind:
                        card_participant.set_used()
                        rank.remove(card_participant)
                    three_of_a_kinds.append(possible_three_of_a_kind)
                    possible_three_of_a_kind = []
                else:
                    possible_three_of_a_kind.append(card)

    return three_of_a_kinds

def detect_two_pairs_and_pairs(rank_division):
    two_pairs = []
    pairs = []

    for rank in reversed(rank_division):
        possible_pairs = []
        if len(rank) < 2:
            continue
        for card in rank:
            if card.get_used():
                possible_pairs = []
                continue
            elif possible_pairs == [] or card.get_rank() != possible_pairs[-1].get_rank():
                possible_pairs = [card] 
            else:
                if len(possible_pairs) == 1:
                    possible_pairs.append(card)
                    for card_participant in possible_pairs:
                        card_participant.set_used()
                        rank.remove(card_participant)
                    pairs.append(possible_pairs)
                    possible_pairs = []
                else:
                    possible_pairs.append(card)
    if len(pairs) > 1:
        for number in range(0, len(pairs) - 1, 2):
            if only_one_ace_per_hand(pairs[number]+pairs[number+1]):
                two_pairs.append(pairs[number]+pairs[number+1])

    for pair in two_pairs:
        pairs.remove([pair[0], pair[1]])
        pairs.remove([pair[2], pair[3]])

    return two_pairs, pairs

def detect_poker_hands(hand):
    poker_hands = []
    poker_hands_names = ["Royal Flushes", "Straight Flushes", "Four of a Kinds", "Full Houses", "Flushes", "Straights", "Three of a Kinds", "Two Pairs", "Pairs"]

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
