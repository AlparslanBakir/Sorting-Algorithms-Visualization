import time
import keyboard
max_time = 0.250
# compares neighbouring elements in the array
def bubbleSort(arr, display, speedInput, pauseBool):

    swapCount = 0
    comparisonCount = 0
    
    N = len(arr)
    for i in range(N):
        swapped = False

        for j in range(N - 1):
            comparisonCount += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapCount += 1
                colorArray = ['#E06469'] * N
                colorArray[j] = '#70A1D7'
                colorArray[j + 1] = '#70A1D7'
                if i:
                    colorArray[-i:] = ['#539165'] * i

                display(arr, colorArray, swapCount,  comparisonCount)
                time.sleep(max_time - (speedInput() * max_time / 100))
                swapped = True
        
        if not swapped:
            break

    colorArray = ['#539165'] * N
    display(arr, colorArray, swapCount,   comparisonCount)
    print("Sorted arr : ",arr)
        


# arr = [2, 10,11,25,13,78,1,7,80]
#
# print(bubbleSort(arr))
