class SearchingAlgorithms:
    def sequantial_search_unordered(self, unordered_list, number):
        ix = 0
        found = False
        
        while ix < len(unordered_list) and not found:
            if unordered_list[ix] == number:
                found = True
                print("Index:", ix)
            else:
                ix += 1
        
        return found
    
    def sequantial_search_ordered(self, ordered_list, number):
        ix = 0
        found = False
        bigger = False
        
        while ix < len(ordered_list) and not found and not bigger:
            if ordered_list[ix] == number:
                found = True
                print("Index:", ix)
            else:
                if ordered_list[ix] > number:
                    bigger = True
                else:
                    ix += 1
        
        return found
    
    def binary_search(self, ordered_list, number):
        first_pointer = 0
        last_pointer = len(ordered_list) - 1
        
        found = False
        
        while first_pointer <= last_pointer and not found:
             mid_point = (first_pointer + last_pointer) // 2
             
             if ordered_list[mid_point] == number:
                 found = True
             else:
                 if ordered_list[mid_point] > number:
                     first_pointer = mid_point + 1
                 else:
                     last_pointer = mid_point - 1
                     
             return found


search = SearchingAlgorithms()
my_list = [40, 20, 10, 4, 5, 19, 80, 2, 0, 14]
print(search.sequantial_search_unordered(my_list, 10))
print(search.sequantial_search_unordered(my_list, 15))

my_list.sort()
print(search.sequantial_search_ordered(my_list, 10))
print(search.sequantial_search_ordered(my_list, 15))

print(search.binary_search(my_list, 10))
print(search.binary_search(my_list, 15))