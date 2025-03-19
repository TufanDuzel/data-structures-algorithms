class SortingAlgorithm:
    def selection_sort(self, arr):
        for i in range(len(arr) - 1):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    
sorting = SortingAlgorithm()
print(sorting.selection_sort([5, 10, 3, 4, 2, 8, 6, 1]))