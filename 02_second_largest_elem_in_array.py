def second_element_reverse_brute(arr):
    # remove duplicates and sort the array
    sorted_array = sorted(arr)
    print("Sorted array:", sorted_array)

    # if array has only two elem
    if len(sorted_array) < 2:
        print("Not enough to find second largest elem in an array.")
        return

    n = len(sorted_array)
    largest = sorted_array[n - 1]
    # Traverse the array in reverse
    for i in range(n - 1, -1, -1):
        if sorted_array[i] != largest:
            print(sorted_array[i])
            break
    print("Not Found")


def second_element_reverse_better(arr):
    # length of an array
    n = len(arr)

    if n < 2:
        print("Not enough for finding second largest elem in an array")
        return

    largest = arr[0]
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    second_largest = -1
    for i in range(n):
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    print(second_largest)


my_arr = [1, 2, 3, 4, 5]
second_element_reverse_better(my_arr)
