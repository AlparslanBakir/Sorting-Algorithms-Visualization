import time

max_time = 0.250
swapCount = 0
iterationCount = 0
comparisonCount = 0

##---to reset swap count
def mergeSort(arr, display, speedInput, pauseBool):
    global swapCount, iterationCount, comparisonCount
    swapCount = 0
    start, end = 0, len(arr) - 1
    _merge_sort(arr, display, speedInput, pauseBool, start, end)


# divides the array recursively into two parts then sorts
def _merge_sort(arr, display, speedInput, pauseBool, start, end):
    if start < end:
        mid = (start + end) // 2
        _merge_sort(arr, display, speedInput, pauseBool, start, mid)
        _merge_sort(arr, display, speedInput, pauseBool, mid + 1, end)
        _merge(arr, display, speedInput, pauseBool, start, mid, end)


def _merge(arr, display, speedInput, pauseBool, start, mid, end):
    global swapCount, iterationCount, comparisonCount

    N = len(arr)
    #--highlight the left and the right parts of the array
    colorArray = ['#E06469'] * N
    colorCoords = ((start, mid + 1, '#FFFDB7'), (mid + 1, end + 1, '#70A1D7'))
    for lower, upper, color in colorCoords:
        colorArray[lower:upper] = [color] * (upper - lower)

    display(arr, colorArray, swapCount, iterationCount, comparisonCount)
    time.sleep(max_time - (speedInput() * max_time / 100))

    arrL = arr[start:mid+1]
    arrR = arr[mid + 1:end + 1]

    i, j, k = 0, 0, start # i->arrL;   j->arrR;   k->arr

    while (i < len(arrL) and j < len(arrR)):
        if arrL[i] < arrR[j]:
            arr[k] = arrL[i]
            i += 1
        else:
            arr[k] = arrR[j]
            j += 1

        swapCount += 1
        colorArray[start:k] = ['#539165'] * (k - start)
        display(arr, colorArray, swapCount, iterationCount, comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))
        iterationCount += 1  
        comparisonCount += 1  

        k += 1

    #check if anything left
    while i < len(arrL):
        arr[k] = arrL[i]
        i += 1
        k += 1
        swapCount += 1
        colorArray[start:k] = ['#539165'] * (k - start)
        display(arr, colorArray, swapCount, iterationCount, comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))
        iterationCount += 1

    while j < len(arrR):
        arr[k] = arrR[j]
        j += 1
        k += 1
        swapCount += 1
        colorArray[start:k] = ['#539165'] * (k - start)
        display(arr, colorArray, swapCount, iterationCount, comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))
        iterationCount += 1
    print("Sorted arr : ", arr)
