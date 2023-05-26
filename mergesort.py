import time

max_time = 0.250
comparisonCount = 0  # Comparison count initialization
swapCount = 0  # Swap count initialization

def mergeSort(arr, display, speedInput, pauseBool):
    global swapCount, comparisonCount
    start, end = 0, len(arr) - 1
    _merge_sort(arr, display, speedInput, pauseBool, start, end, comparisonCount, swapCount)
    


def _merge_sort(arr, display, speedInput, pauseBool, start, end, comparisonCount, swapCount):
    if start < end:
        mid = (start + end) // 2
        _merge_sort(arr, display, speedInput, pauseBool, start, mid, comparisonCount, swapCount)
        _merge_sort(arr, display, speedInput, pauseBool, mid + 1, end, comparisonCount, swapCount)
        _merge(arr, display, speedInput, pauseBool, start, mid, end, comparisonCount, swapCount)


def _merge(arr, display, speedInput, pauseBool, start, mid, end, comparisonCount, swapCount):
    N = len(arr)
    #--highlight the left and the right parts of the array
    colorArray = ['#E06469'] * N
    colorCoords = ((start, mid + 1, '#FFFDB7'), (mid + 1, end + 1, '#70A1D7'))
    colorArray = ['#E06469'] * N
    colorCoords = ((start, mid + 1, '#ffff00'), (mid + 1, end + 1, '#5200cc'))
    for lower, upper, color in colorCoords:
        colorArray[lower:upper] = [color] * (upper - lower)

    display(arr, colorArray, swapCount, comparisonCount)
    time.sleep(max_time - (speedInput() * max_time / 100))

    arrL = arr[start:mid + 1]
    arrR = arr[mid + 1:end + 1]

    i, j, k = 0, 0, start

    while i < len(arrL) and j < len(arrR):
        comparisonCount += 1  # Increment comparison count
        if arrL[i] < arrR[j]:
            arr[k] = arrL[i]
            i += 1
        else:
            arr[k] = arrR[j]
            j += 1
            swapCount += 1  # Increment swap count

        swapCount += 1
        colorArray[start:k] = ['#539165'] * (k - start)
        display(arr, colorArray, swapCount,   comparisonCount)
        colorArray[start:k] = ['#539165'] * (k - start)
        display(arr, colorArray, swapCount, comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

        k += 1

    while i < len(arrL):
        arr[k] = arrL[i]
        i += 1
        k += 1
        swapCount += 1
        colorArray[start:k] = ['#539165'] * (k - start)
        display(arr, colorArray, swapCount,   comparisonCount)
        swapCount += 1  # Increment swap count
        colorArray[start:k] = ['#539165'] * (k - start)
        display(arr, colorArray, swapCount, comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

    while j < len(arrR):
        arr[k] = arrR[j]
        j += 1
        k += 1
        swapCount += 1
        colorArray[start:k] = ['#539165'] * (k - start)
        display(arr, colorArray, swapCount,   comparisonCount)
        swapCount += 1  # Increment swap count
        colorArray[start:k] = ['#539165'] * (k - start)
        display(arr, colorArray, swapCount, comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

    print("Sorted arr:", arr)