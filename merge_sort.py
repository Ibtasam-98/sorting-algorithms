import random
import time
import matplotlib.pyplot as plt

# Visualize Merge Sort
def merge_sort_visualized_short(data, ax):
    n = len(data)
    if n <= 1:
        return data
    mid = n // 2
    left = merge_sort_visualized_short(data[:mid], ax)
    right = merge_sort_visualized_short(data[mid:], ax)
    return merge_two_sorted_lists_visualized_short(left, right, data, ax)

# Merge two sorted lists with visualization
def merge_two_sorted_lists_visualized_short(left, right, original, ax):
    merged = []
    i = j = k = 0
    temp = list(original)

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            temp[k] = left[i]
            i += 1
        else:
            merged.append(right[j])
            temp[k] = right[j]
            j += 1
        k += 1
        ax.clear()
        ax.bar(range(len(temp)), temp, color='blue')
        ax.set_title("Merging...")
        plt.pause(0.1)

    while i < len(left):
        merged.append(left[i])
        temp[k] = left[i]
        i += 1; k += 1
        ax.clear()
        ax.bar(range(len(temp)), temp, color='blue')
        ax.set_title("Merging...")
        plt.pause(0.1)

    while j < len(right):
        merged.append(right[j])
        temp[k] = right[j]
        j += 1; k += 1
        ax.clear()
        ax.bar(range(len(temp)), temp, color='blue')
        ax.set_title("Merging...")
        plt.pause(0.1)

    return merged

if __name__ == "__main__":
    # Generate random data
    unsorted = [random.randint(1, 100) for _ in range(10)]
    print("Unsorted Data:", unsorted)

    # Initial plot
    fig, ax = plt.subplots()
    ax.bar(range(len(unsorted)), unsorted, color='gray')
    ax.set_title("Initial Data")
    plt.pause(1)

    # Start merge sort with visualization
    sorted_data = merge_sort_visualized_short(list(unsorted), ax)
    print("Sorted Data:", sorted_data)

    # Final plot
    ax.clear()
    ax.bar(range(len(sorted_data)), sorted_data, color='green')
    ax.set_title("Sorted Data")
    plt.show()
