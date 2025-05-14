import matplotlib.pyplot as plt
import numpy as np

def heapify(arr, n, i, bars):
    """
    Maintains the heap property for a subtree rooted at index i.

    Args:
        arr (list): The list representing the heap.
        n (int): The size of the heap.
        i (int): The index of the root of the subtree to heapify.
        bars (matplotlib.patches.Rectangle list): List of bar objects for visualization.
    """
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # Left child
    r = 2 * i + 2  # Right child

    # If left child is larger than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[largest] < arr[r]:
        largest = r

    # If largest is not root
    if largest != i:
        # Swap root with largest element
        arr[i], arr[largest] = arr[largest], arr[i]
        # Update bar heights for visualization
        bars[i].set_height(arr[i])
        bars[largest].set_height(arr[largest])

        # Highlight the swapped bars in red briefly
        bars[i].set_color('red')
        bars[largest].set_color('red')
        plt.pause(0.1)

        # Reset the color of the swapped bars to blue
        bars[i].set_color('blue')
        bars[largest].set_color('blue')

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest, bars)

def heap_sort_visualized(arr):
    """
    Performs Heap Sort on the input array and visualizes the process.

    Args:
        arr (list): The list to be sorted.
    """
    n = len(arr)
    # Create a figure and axes for the plot
    fig, ax = plt.subplots()
    # Create bar objects for each element in the array
    bars = ax.bar(np.arange(n), arr, color='blue')
    # Set the limits for the x and y axes
    ax.set_xlim(-1, n)
    ax.set_ylim(0, max(arr) * 1.1)
    # Set the title of the plot
    ax.set_title("Heap Sort")

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, bars)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Swap the root (largest element) with the last element
        arr[i], arr[0] = arr[0], arr[i]
        # Update bar heights for visualization
        bars[i].set_height(arr[i])
        bars[0].set_height(arr[0])

        # Highlight the swapped bars in green briefly
        bars[i].set_color('green')
        bars[0].set_color('green')
        plt.pause(0.2)

        # Heapify the reduced heap
        heapify(arr, i, 0, bars)
        # Reset the color of the now sorted element
        bars[i].set_color('blue')

    # Display the final sorted plot
    plt.show()

if __name__ == "__main__":
    # Generate an array of 20 random integers between 1 and 99
    data = np.random.randint(1, 100, 20)
    print("Original data", data)
    # Create a copy of the data to avoid modifying the original during visualization
    heap_sort_visualized(data.copy())
    print("Sorted data:", data)
