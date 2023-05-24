import time

max_time = 0.250

#finds the minimum value of the remaining array everytime
def selectionSort(arr, display, speedInput, pauseBool):
    swapCount = 0
    iterationCount = 0
    comparisonCount = 0
    N = len(arr)
    for i in range(N):
        min_ind = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_ind]:
                min_ind = j

                colorArray = ['red'] * N
                colorArray[:i] = ['green'] * i
                colorArray[j] = 'blue'
                colorArray[min_ind] = 'blue'

                display(arr, colorArray, swapCount, iterationCount, comparisonCount)
                time.sleep(max_time - (speedInput() * max_time / 100))

        arr[i], arr[min_ind] = arr[min_ind], arr[i]
        swapCount += 1
        # colorArray = ['green' if x<=i else 'red' for x in range(len(arr))]
        colorArray = ['red'] * N
        colorArray[0:i + 1] = ['green'] * (i + 1)
        display(arr, colorArray, swapCount, iterationCount, comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

    colorArray = ['green'] * N
    display(arr, colorArray, swapCount, iterationCount, comparisonCount)
    print("Sorted arr : ", arr)
