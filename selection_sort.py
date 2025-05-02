import matplotlib.pyplot as plt
import random, time

def selection_sort(arr):
    """Visualizes selection sort."""
    for i in range(len(arr)):
        # Find index of min element in unsorted part.
        min_idx = min(range(i, len(arr)), key=arr.__getitem__)
        # Swap current with min.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        plt.clf()
        # Highlight current and min.
        colors = ['blue'] * len(arr)
        colors[i], colors[min_idx] = 'green', 'red'
        plt.bar(range(len(arr)), arr, color=colors)
        plt.title("Selection Sort Visualization")
        plt.pause(0.001)
        time.sleep(0.01)

if __name__ == "__main__":
    # Generate random array.
    arr = random.choices(range(1, 20), k=20)
    plt.figure(figsize=(12, 6))
    selection_sort(arr)
    plt.show()
    print("Sorted Array : ", arr)
