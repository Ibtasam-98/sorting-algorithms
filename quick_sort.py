import matplotlib.pyplot as plt
import numpy as np

def quicksort(arr, low, high, sorted_idx=set()):
    """Recursive quicksort with visualization tracking"""
    if low < high:
        pi = partition(arr, low, high)  # Get pivot index
        sorted_idx.add(pi)  # Mark pivot as sorted
        visualize(arr, low, high, pi, sorted_idx)
        # Recursively sort elements before and after pivot
        quicksort(arr, low, pi-1, sorted_idx)
        quicksort(arr, pi+1, high, sorted_idx)
        sorted_idx.update(range(low, high+1))  # Mark current segment as sorted

def partition(arr, low, high):
    """Partitioning logic - places pivot in correct position"""
    pivot = arr[high]  # Choose last element as pivot
    i = low  # Pointer for smaller elements
    
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]  # Swap if smaller than pivot
            i += 1
    # Place pivot in correct position
    arr[i], arr[high] = arr[high], arr[i]
    return i  # Return pivot index

def visualize(arr, low, high, pivot_idx, sorted_idx):
    """Visualize sorting progress with colors"""
    plt.clf()  # Clear previous frame
    colors = ['black'] * len(arr)  # Default: unsorted = black
    
    # Current partition being processed = red
    for i in range(low, high+1):
        colors[i] = 'red'
    colors[pivot_idx] = 'red'  # Highlight pivot
    
    # Mark sorted elements = green
    for i in sorted_idx:
        colors[i] = 'green'
    
    plt.bar(range(len(arr)), arr, color=colors)
    plt.pause(0.3)  # Control animation speed

if __name__ == "__main__":
    data = np.random.randint(1, 100, 50)  # Generate random array
    plt.ion()  # Enable interactive mode
    quicksort(data, 0, len(data)-1)  # Start sorting
    plt.ioff()
    plt.show()  # Keep window open
