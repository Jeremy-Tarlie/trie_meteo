class LinearSearch:
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1