class SortingAlgorithm:
    def bubble_sort(self, arr):
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    
        return arr
        
sorting = SortingAlgorithm()
print(sorting.bubble_sort([5, 10, 3, 4, 2, 8, 6, 1]))