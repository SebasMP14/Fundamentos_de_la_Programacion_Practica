import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time 

def draw_bars(data, ax, colors):
    ax.clear()
    ax.bar(range(len(data)), data, color=colors)
    ax.set_title("Animación de Ordenamiento")
    ax.set_ylim(0, max(data) + 1)

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
            yield data, [i if k == i else j if k == j else min_idx if k == min_idx else -1 for k in range(n)]
        data[i], data[min_idx] = data[min_idx], data[i]
        yield data, [i if k == i else min_idx if k == min_idx else -1 for k in range(n)]

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            yield data, [j, j+1]
            j -= 1
        data[j + 1] = key
        yield data, [j+1]

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data, [j, j + 1]

def animate_sorting(sort_function, title=""):
    data = [random.randint(1, 50) for _ in range(15)]
    generator = sort_function(data[:])
    
    fig, ax = plt.subplots()
    def update(frame):
        array, highlights = frame
        colors = ['orange' if i in highlights else 'skyblue' for i in range(len(array))]
        draw_bars(array, ax, colors)
    
    ani = animation.FuncAnimation(fig, update, frames=generator, repeat=False, interval=300)
    plt.show()

# animate_sorting(selection_sort, "Selection Sort")
animate_sorting(insertion_sort, "Insertion Sort")
# animate_sorting(bubble_sort, "Bubble Sort")
