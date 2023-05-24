import time

max_time = 0.250

def insertionSort(arr, display, speedInput, pauseBool):

    global worse, best, average
    iterationCount = 0
    comparisonCount = 0
    swapCount = 0
    N = len(arr)
    for i in range(1, N):
        key = arr[i]
        j = i - 1

        colorArray = ['red'] * N
        colorArray[:i] = ['green'] * i
        display(arr, colorArray, swapCount, iterationCount, comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))
        iterationCount += 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swapCount += 1

            colorArray = ['red'] * N
            colorArray[j + 1] = 'blue'
            display(arr, colorArray, swapCount, iterationCount, comparisonCount)
            time.sleep(max_time - (speedInput() * max_time / 100))
            comparisonCount += 1

        arr[j + 1] = key

        colorArray = ['red'] * N
        colorArray[:i + 1] = ['green'] * (i + 1)
        display(arr, colorArray, swapCount, iterationCount, comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))
        iterationCount += 1

    colorArray = ['green'] * N
    display(arr, colorArray, swapCount, iterationCount, comparisonCount)
    print("Sorted arr:", arr)

    


