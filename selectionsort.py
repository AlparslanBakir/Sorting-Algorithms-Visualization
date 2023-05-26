import time

max_time = 0.250

#finds the minimum value of the remaining array everytime
def selectionSort(arr, display, speedInput, pauseBool):
    swapCount = 0
    comparisonCount = 0
    N = len(arr)
    for i in range(N):
        min_ind = i
        for j in range(i + 1, N):
            
            comparisonCount += 1

            if arr[j] < arr[min_ind]:
                min_ind = j

                colorArray = ['#E06469'] * N
                colorArray[:i] = ['#539165'] * i
                colorArray[j] = '#70A1D7'
                colorArray[min_ind] = '#70A1D7'

                display(arr, colorArray, swapCount,   comparisonCount)
                time.sleep(max_time - (speedInput() * max_time / 100))

        arr[i], arr[min_ind] = arr[min_ind], arr[i]
        swapCount += 1
        # colorArray = ['green' if x<=i else 'red' for x in range(len(arr))]
        colorArray = ['#E06469'] * N
        colorArray[0:i + 1] = ['#539165'] * (i + 1)
        display(arr, colorArray, swapCount,  comparisonCount)
        colorArray = ['#E06469'] * N
        colorArray[0:i + 1] = ['#539165'] * (i + 1)
        display(arr, colorArray, swapCount,   comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

    colorArray = ['#539165'] * N
    display(arr, colorArray, swapCount,   comparisonCount)
    colorArray = ['#539165'] * N
    display(arr, colorArray, swapCount,  comparisonCount)
    print("Sorted arr : ", arr)
