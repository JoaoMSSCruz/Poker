from functions.sorting_alg.heap_sort.heap_sort import heap_sort
from functions.sorting_alg.binary_search_sort.binary_insertion_sort import binary_insertion_sort
from functions.sorting_alg.merge_sort.merge_sort import merge_sort
from functions.sorting_alg.quick_sort.quick_sort import quick_sort
import random

def choose_sorting_algorithm(hand):
    while True:
        number = random.choice([1, 2, 3, 4])
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

    return hand