# Python program to print all distinct elements in an
# array using nested loops

def find_distinct(arr):
    res = []

    for i in range(len(arr)):

        # Check if this element is included in result
        j = 0
        while j < i:
            if arr[i] == arr[j]:
                break
            j += 1

        # Include this element if not included previously
        if i == j:
            res.append(arr[i])

    return res


if __name__ == "__main__":
    arr = [12, 10, 9, 45, 2, 10, 10, 45]
    res = find_distinct(arr)
    for val in res:
        print(val, end=" ")
