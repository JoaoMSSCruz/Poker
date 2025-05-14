from functions.sorting_alg.heap_sort.heap_sort import heap_sort
from functions.sorting_alg.binary_search_sort.binary_insertion_sort import binary_insertion_sort
from functions.sorting_alg.merge_sort.merge_sort import merge_sort
from functions.sorting_alg.quick_sort.quick_sort import quick_sort

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