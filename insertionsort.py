import time

max_time = 0.250

def insertionSort(arr, display, speedInput, pauseBool):

    global worse, best, average
    comparisonCount = 0
    swapCount = 0
    N = len(arr)
    for i in range(1, N):
        key = arr[i]
        j = i - 1

        colorArray = ['#E06469'] * N
        colorArray[:i] = ['#539165'] * i
        display(arr, colorArray, swapCount,   comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swapCount += 1

            colorArray = ['#E06469'] * N
            colorArray[j + 1] = '#70A1D7'
            display(arr, colorArray, swapCount,   comparisonCount)
            time.sleep(max_time - (speedInput() * max_time / 100))
            comparisonCount += 1

        arr[j + 1] = key

        colorArray = ['#E06469'] * N
        colorArray[:i + 1] = ['#539165'] * (i + 1)
        display(arr, colorArray, swapCount,   comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

    colorArray = ['#539165'] * N
    display(arr, colorArray, swapCount, comparisonCount)
    print("Sorted arr:", arr)

    


