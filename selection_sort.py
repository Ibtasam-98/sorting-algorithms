import matplotlib.pyplot as plt
import random, time

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = min(range(i, len(arr)), key = arr.__getitem__)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        plt.clf()

        colors = ['blue'] * len(arr)
        colors[i], colors[min_idx] = 'green', 'red'
        plt.bar(range(len(arr)), arr, color=colors)
        plt.title("Selection Sort Visualization")
        plt.pause(0.001)
        time.sleep(0.01)

if __name__=="__main__":
    arr = random.choices(range(1,20), k=20)
    plt.figure(figsize=(12,6))
    selection_sort(arr)
    plt.show()
    print("Sorted Array : ", arr)
