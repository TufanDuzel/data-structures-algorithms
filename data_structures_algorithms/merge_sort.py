class SortingAlgorithm:
    def merge(self, arr1, arr2):
        first_pointer = 0
        second_pointer = 0
        merged_list = []

        while first_pointer < len(arr1) and second_pointer < len(arr2):
            if arr1[first_pointer] < arr2[second_pointer]:
                merged_list.append(arr1[first_pointer])
                first_pointer += 1
            else:
                merged_list.append(arr2[second_pointer])
                second_pointer += 1
        
        while first_pointer < len(arr1):
            merged_list.append(arr1[first_pointer])
            first_pointer += 1

        while second_pointer < len(arr2):
            merged_list.append(arr2[second_pointer])
            second_pointer += 1

        return merged_list
    
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])

        return self.merge(left_half, right_half)
    
sorting = SortingAlgorithm()
print(sorting.merge_sort([5, 10, 3, 4, 2, 8, 6, 1]))