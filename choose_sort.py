import bubble_sort
import insertion_sort
import quick_sort
import selection_sort
import sys

class ChooseSort:
    def choose_sort(array, sort_type):
        match sort_type:
            case 1:
                bubble_sort.BubbleSort.bubble_sort(array)
            case 2:
                insertion_sort.InsertionSort.insertion_sort(array)
            case 3:
                quick_sort.QuickSort.quick_sort(array)
            case 4:
                selection_sort.SelectionSort.selection_sort(array)
            case 5:
                sys.exit()
            case _:
                print("Invalid sort type.")