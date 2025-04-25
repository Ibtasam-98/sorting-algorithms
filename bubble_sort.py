import time
import random
import matplotlib.pyplot as plt
import  matplotlib.animation as animation

def bubble_sort_visualization(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1]  =data[ j+ 1], data[j]
                swapped = True
            yield list(data)
        if not swapped:
            break

if __name__ == "__main__":
    n = 20
    data = random.sample(range(1,n+1),n)
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort")
    bars = ax.bar(range(n), data, align="center")

    def update(frame_data):
        for bar, val in zip(bars, frame_data):
            bar.set_height(val)
        return bars

    ani = animation.FuncAnimation(fig, update,
                                  frames=bubble_sort_visualization(data),
                                  interval=100,repeat=False)
    plt.show()
    print(f"Sorted: {data}")

