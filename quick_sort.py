class QuickSort:
    def quick_sort(array):
        if len(array) <= 1:
            print(array)
        else:
            pivot = array[0]
            less = [x for x in array[1:] if x <= pivot]
            greater = [x for x in array[1:] if x > pivot]
            return QuickSort.quick_sort(less) + [pivot] + QuickSort.quick_sort(greater)