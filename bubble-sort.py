def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # last i element are already sorted so don't need to check them
        for j in range(0, n - i - 1):
            # swap if the element found is greater then the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# example array
arr = [1, 43, 2, 4, 0, 9, 9, 5, 6, 7, 3, 4, 2, ]
bubble_sort(arr)
print("Sorted Array :", arr)
