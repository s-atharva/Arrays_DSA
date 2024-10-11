my_array = [3, 2, 1, 5, 2]

largest = my_array[0]
for num in my_array:
    if num > largest:
        largest = num
print(largest)
