from matplotlib import pyplot as plt
from matplotlib import animation
import random

def bubbleSort(arr):
    for j in range(len(arr)):
        for i in range(0, len(arr) - 1):
            if arr[i+1] < arr[i]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
            yield arr

def selectionSort(arr):
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j         
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

def mergeSort(arr, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergeSort(arr, start, mid)
    yield from mergeSort(arr, mid + 1, end)
    yield from merge(arr, start, mid, end)
    yield arr

def merge(arr, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if arr[leftIdx] < arr[rightIdx]:
            merged.append(arr[leftIdx])
            leftIdx += 1
        else:
            merged.append(arr[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(arr[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(arr[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        arr[start + i] = sorted_val
        yield arr

def insertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key
        yield arr

def cocktailSort(arr): 
    n = len(arr) 
    swapped = True
    start = 0
    end = n-1
    while (swapped == True): 
        swapped = False
        for i in range (start, end): 
            if (arr[i] > arr[i + 1]) : 
                arr[i], arr[i + 1]= arr[i + 1], arr[i] 
                swapped = True
        if (swapped == False): 
            break
        swapped = False 
        end = end-1 
        for i in range(end-1, start-1, -1): 
            if (arr[i] > arr[i + 1]): 
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
                swapped = True
        start = start + 1
        yield arr

def bogoSort(arr): 
    n = len(arr) 
    while (is_sorted(arr)== False): 
        shuffle(arr)
        yield arr
  
def is_sorted(arr): 
    n = len(arr) 
    for i in range(0, n-1): 
        if (arr[i] > arr[i+1] ): 
            return False
    return True
  
def shuffle(arr): 
    n = len(arr) 
    for i in range (0,n): 
        r = random.randint(0,n-1) 
        arr[i], arr[r] = arr[r], arr[i] 

size = int(input("How many numbers would you like to sort: "))

x_axis = [i + 1 for i in range(size)]
random.shuffle(x_axis)
y_axis = [j + 1 for j in range(size)]

print(" (a) bubble sort\n (b) selection sort\n (c) insertion sort\n",
      "(d) cocktail sort\n (e) bogo sort\n (f) merge sort")
algo = input("What algorithm would you like? ")

if algo == "a":
    title = "Bubble Sort"
    sort = bubbleSort(x_axis)
elif algo == "b":
    title = "Selection Sort"
    sort = selectionSort(x_axis)
elif algo == "c":
    title = "Insertion Sort"
    sort = insertionSort(x_axis)
elif algo == "d":
    title = "Cocktail Sort"
    sort = cocktailSort(x_axis)
elif algo == "e":
    title = "Bogo Sort"
    sort = bogoSort(x_axis)
elif algo == "f":
    title = "Merge Sort"
    sort = mergeSort(x_axis, 0, size - 1)
else:
    print("Not valid, have a nice day!")

fig = plt.figure()

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(x_axis)), x_axis, align="center")

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, x_axis):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=sort, interval=1,
        repeat=False)
    plt.show()
