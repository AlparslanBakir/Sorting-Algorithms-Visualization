import time

max_time = 0.250
swapCount = 0

comparisonCount = 0


def quickSort(arr, display, speedInput, pauseBool):
    global swapCount, comparisonCount
    swapCount = 0
    low, high = 0, len(arr) - 1
    _quick_sort(arr, display, speedInput, pauseBool, low, high)


def _quick_sort(arr, display, speedInput, pauseBool, low, high):
    if low < high:
        #--partition index
        partInd = _partition(arr, display, speedInput, pauseBool, low, high)

        _quick_sort(arr, display, speedInput, pauseBool, low, partInd-1)
        _quick_sort(arr, display, speedInput, pauseBool, partInd+1, high)


##--taking last element as pivot
##--separates smaller elements to the left and larger to the right
def _partition(arr, display, speedInput, pauseBool, low, high):
    global swapCount, comparisonCount

    pointer = low
    count = high - low
    pivots = sorted(
        ((arr[low + i], low + i) for i in (0, count // 4, count // 2, 3 * count // 4, count))
    )
    # pivot = arr[high]
    pivot, pivot_pos = pivots[2]
    if pivot_pos != high:
        arr[pivot_pos], arr[high] = arr[high], arr[pivot_pos]
        swapCount += 1
        

    display(arr, generateColorArray(low, high, pointer, pointer, len(arr), False), swapCount, comparisonCount)
    time.sleep(max_time - (speedInput() * max_time / 100))

    for j in range(low, high):
        comparisonCount += 1

        if arr[j] < pivot:
            display(arr, generateColorArray(low, high, pointer, j, len(arr), True), swapCount, comparisonCount)
            time.sleep(max_time - (speedInput() * max_time / 100))

            arr[j], arr[pointer] = arr[pointer], arr[j]
            pointer += 1
            swapCount += 1

        display(arr, generateColorArray(low, high, pointer, j, len(arr), False), swapCount, comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

    display(arr, generateColorArray(low, high, pointer, high, len(arr), False), swapCount, comparisonCount)
    time.sleep(max_time - (speedInput() * max_time / 100))

    arr[high], arr[pointer] = arr[pointer], arr[high]
    swapCount += 1

    colorArray = ['#539165'] * len(arr)
    display(arr, colorArray, swapCount,   comparisonCount)
    

    colorArray = ['#539165'] * len(arr)
    display(arr, colorArray, swapCount, comparisonCount)

    return pointer


def generateColorArray(low, high, pointer, curr_ind, n, swapping):
    colorArray = ['#94B49F'] * n
    colorArray[low:high + 1] = ['#F6F49D'] * (high - low + 1)
    colorArray[pointer] = '#9BA4B5'
    colorArray[high] = '#E06469'
    colorArray[curr_ind] = '#70A1D7'

    if swapping:
        colorArray[curr_ind] = '#539165'
        colorArray[pointer] = '#539165'
    return colorArray
