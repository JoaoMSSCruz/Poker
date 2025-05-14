from functions.sorting_alg.quick_sort.partition import partition

def quick_sort(hand, low, high):
    if low < high:
        pivot_index = partition(hand, low, high)
        quick_sort(hand, low, pivot_index - 1)
        quick_sort(hand, pivot_index + 1, high)