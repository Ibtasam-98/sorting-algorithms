import matplotlib.pyplot as plt
import numpy as np
import time

def insertion_sort_visualized(data):
    n = len(data)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle('Insertion Sort')

    def update(arr, i, j):
        ax1.clear()
        ax1.bar(range(n), arr, color='lightblue')
        if i < n: ax1.bar(i, arr[i], color='red', label=f'Current')
        if 0 <= j < n - 1 and i < n and j >= 0 and arr[j] > arr[j + 1]:
            ax1.bar(j, arr[j], color='green', label='Compared')
            ax1.bar(j + 1, arr[j + 1], color='green')
        ax1.set_title('Unsorted')
        ax1.legend()

        sorted_part = sorted(arr[:i]) + list(arr[i:])
        ax2.clear()
        ax2.bar(range(n), sorted_part, color='lightgreen')
        ax2.set_title('Partially Sorted')
        plt.pause(0.1)

    print("Unsorted:", data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        update(list(data), i, j + 1)
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            update(list(data), i, j + 1)
        data[j + 1] = key
        update(list(data), i + 1, -2)
    print("Sorted:", data)
    plt.show()

if __name__ == "__main__":
    np.random.seed(42)
    insertion_sort_visualized(np.random.randint(1, 100, 20).copy())