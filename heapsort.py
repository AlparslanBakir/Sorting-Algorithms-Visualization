import time

max_time = 0.250
# compares neighbouring elements in the array
def heapSort(arr, display, speedInput, pauseBool):

    swapCount = 0
    comparisonCount = 0
    
    N = len(arr)
    for heap_length in range(1, N):
        while heap_length:
            parent = (heap_length - 1) // 2
            if arr[heap_length] > arr[parent]:
                arr[parent], arr[heap_length] = arr[heap_length], arr[parent]
                swapCount += 1
                colorArray = ['#E06469'] * N
                colorArray[parent] = ['#70A1D7']
                colorArray[heap_length] = ['#F6F49D']
                display(arr, colorArray, swapCount,   comparisonCount)
                time.sleep(max_time - (speedInput() * max_time / 100))
            heap_length = parent
            

    for i in reversed(range(N)):
        arr[i], arr[0] = arr[0], arr[i]
        swapCount += 1
        colorArray = ['#E06469'] * N
        colorArray[0] = '#70A1D7'
        colorArray[i:] = ['#539165'] * (N - i)
        display(arr, colorArray, swapCount, comparisonCount)
        colorArray = ['#E06469'] * N
        colorArray[0] = '#70A1D7'
        colorArray[i:] = ['#539165'] * (N - i)
        display(arr, colorArray, swapCount,   comparisonCount)
        time.sleep(max_time - (speedInput() * max_time / 100))

        parent = 0
        while parent < i:
            indexes = (parent, 2 * parent + 1, 2 * parent + 2)
            _, highest = max(
                ((arr[index], index) for index in indexes if index < i),
                key=lambda x: x[0]
            )
            if highest != parent:
                arr[highest], arr[parent] = arr[parent], arr[highest]
                swapCount += 1
                colorArray[parent] = '#70A1D7'
                colorArray[highest] = '#F6F49D'
                display(arr, colorArray, swapCount,   comparisonCount)
                colorArray[parent] = '#70A1D7'
                colorArray[highest] = '#F6F49D'
                display(arr, colorArray, swapCount, comparisonCount)
                time.sleep(max_time - (speedInput() * max_time / 100))
            else:
                break
            parent = highest
            comparisonCount +=1

    colorArray = ['#539165'] * N
    display(arr, colorArray, swapCount,   comparisonCount)
    colorArray = ['#539165'] * N
    display(arr, colorArray, swapCount, comparisonCount)
    print("Sorted arr : ", arr)
