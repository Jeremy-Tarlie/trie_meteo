import bubble_sort
import insertion_sort
import quick_sort
import selection_sort
import sys
import time

class ChooseSort:
    @staticmethod
    def choose_sort(array, sort_type):
        algorithms = {
            1: ("Bubble Sort", bubble_sort.BubbleSort.bubble_sort),
            2: ("Insertion Sort", insertion_sort.InsertionSort.insertion_sort),
            3: ("Quick Sort", quick_sort.QuickSort.quick_sort),
            4: ("Selection Sort", selection_sort.SelectionSort.selection_sort),
            5: ("Quit", sys.exit)
        }

        if sort_type in algorithms:
            name, sort_function = algorithms[sort_type]
            print(f"Tri sélectionné : {name}")
            
            start_time = time.time()
            sorted_array = sort_function(array.copy())  
            end_time = time.time()

            execution_time = (end_time - start_time) * 1000  
            print(f"Tri effectué en {execution_time:.2f} ms")
            print("Résultat trié :", sorted_array)
        else:
            print("Type de tri invalide.")
