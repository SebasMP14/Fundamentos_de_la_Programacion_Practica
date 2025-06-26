import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# CONFIGURACIÓN: Cambiá esto a 'quicksort' o 'mergesort'
# algorithm_to_visualize = 'quicksort'  # o 'mergesort'
algorithm_to_visualize = 'mergesort'

# Lista aleatoria para ordenar
original_list = [random.randint(1, 50) for _ in range(20)]
default_color = 'blue'
active_color = 'red'

def animate_sort(algorithm):
    steps = []
    colors = []

    def quicksort(arr, l=0, r=None):
        if r is None:
            r = len(arr) - 1
        if l < r:
            p = partition(arr, l, r)
            quicksort(arr, l, p - 1)
            quicksort(arr, p + 1, r)

    def partition(arr, l, r):
        pivot = arr[r]
        i = l - 1
        for j in range(l, r):
            steps.append(arr[:])
            col = [default_color] * len(arr)
            col[j] = active_color
            col[r] = 'green'
            colors.append(col)
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(arr[:])
                colors.append(col[:])
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        steps.append(arr[:])
        colors.append([default_color] * len(arr))
        return i + 1

    def mergesort(arr, l=0, r=None):
        if r is None:
            r = len(arr)
        if r - l > 1:
            m = (l + r) // 2
            mergesort(arr, l, m)
            mergesort(arr, m, r)
            merge(arr, l, m, r)

    def merge(arr, l, m, r):
        left = arr[l:m]
        right = arr[m:r]
        i = j = 0
        for k in range(l, r):
            steps.append(arr[:])
            col = [default_color] * len(arr)
            col[k] = active_color
            colors.append(col)
            if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            steps.append(arr[:])
            colors.append(col[:])

    arr = original_list[:]
    if algorithm == 'quicksort':
        quicksort(arr)
    else:
        mergesort(arr)

    return steps, colors

# Preparar los datos
steps, colors = animate_sort(algorithm_to_visualize)

# Crear la figura
fig, ax = plt.subplots(figsize=(8, 4))
fig.suptitle(f"{algorithm_to_visualize.capitalize()} Animation")

bars = ax.bar(range(len(original_list)), original_list, color=default_color)
ax.set_xlim(0, len(original_list))
ax.set_ylim(0, max(original_list) + 10)

def update(frame):
    for bar, h, c in zip(bars, steps[frame], colors[frame]):
        bar.set_height(h)
        bar.set_color(c)
    return bars

ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(steps),
    interval=500,  # medio segundo por frame
    blit=True,
    repeat=False
)

plt.tight_layout()
plt.show()
