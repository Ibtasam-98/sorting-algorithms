import matplotlib.pyplot as plt
import numpy as np

def heapify(arr, n, i, bars):
    largest = i; l = 2 * i + 1; r = 2 * i + 2
    if l < n and arr[i] < arr[l]: largest = l
    if r < n and arr[largest] < arr[r]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        bars[i].set_height(arr[i])
        bars[largest].set_height(arr[largest])

        bars[i].set_color('red')
        bars[largest].set_color('red')
        plt.pause(0.1)

        bars[i].set_color('blue')
        bars[largest].set_color('blue')
        heapify(arr, n, largest, bars)

def heap_sort_visualized(arr):
    n = len(arr); fig, ax = plt.subplots()
    bars = ax.bar(np.arange(n), arr, color='blue')
    ax.set_xlim(-1, n); ax.set_ylim(0, max(arr) * 1.1)
    ax.set_title("Heap Sort")

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, bars)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]; bars[i].set_height(arr[i]); bars[0].set_height(arr[0])
        bars[i].set_color('green'); bars[0].set_color('green'); plt.pause(0.2)
        heapify(arr, i, 0, bars); bars[i].set_color('blue')
    plt.show()

if __name__ == "__main__":
    data = np.random.randint(1, 100, 20);
    print("Original data", data)
    heap_sort_visualized(data.copy()); print("Sorted data:", data)
