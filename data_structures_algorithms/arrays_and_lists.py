# %% Creating a array.
import array as arr

myArray = arr.array("i", [3, 6, 9, 12])

myArray.append(15)
print(myArray)

# %% Combining the lists.
firstList = [1, 2, 3, 4, 5]
secondList = [6, 7, 8]

# The references to the values ​​of the merged list are copied and added to the other list.
firstList.extend(secondList)
print(firstList)

# %% Creating a single reference array and adding a new value.
# All fields point to reference 0.
myArr = [0] * 8
print(myArr)

# [3] Points to the reference of variable 2.
myArr[3] = 1
print(myArr)

# %% Ram Garbage Collector.
import sys

n = 30
myDynamicArray = []  # Empty array.

for i in range(n):
    arrayLength = len(myDynamicArray)  # Length of the array.
    arrayByte = sys.getsizeof(myDynamicArray)  # Byte size.

    print(f"Length: {arrayLength} Byte: {arrayByte}")

    # adding variable each time.
    myDynamicArray.append(n)
