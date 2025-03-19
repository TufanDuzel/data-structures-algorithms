class SortingAlgorithm:
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            while temp < arr[j] and j > -1:
                arr[j + 1] = arr[j] 
                arr[j] = temp
                j -= 1
        return arr
    
sorting = SortingAlgorithm()
print(sorting.insertion_sort([5, 10, 3, 4, 2, 8, 6, 1]))