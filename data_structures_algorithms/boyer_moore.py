myList = [8, 9, 10, 10, 10, 10, 2, 8, 9, 10, 8, 9, 10, 10]

# Boyer Moore
def boyerMoore():
    result = 0
    count = 0

    for num in myList:
        if count == 0:
            result = num
        count +=1 if num == result else -1
    return result

print(boyerMoore())