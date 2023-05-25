#---start import section-------------------
import time
import math
import random


from tkinter import Canvas, Frame, StringVar, Tk, Label, Button, Scale, Entry, HORIZONTAL
from tkinter import ttk

from mergesort import mergeSort
from quicksort import quickSort
from bubblesort import bubbleSort
from selectionsort import selectionSort
from insertionsort import insertionSort
from heapsort import heapSort

#---end import section---------------------


root = Tk()
root.title('Sorting Algorithms Visualizer')
root_width = root.winfo_screenwidth()-25
root_height = root.winfo_screenheight()-25
root.geometry(f"{root_width}x{root_height}")
root.maxsize(root_width,root_height)   #(width,height)
root.config(bg='black')

#----GLOBAL VARIABLES---------
allAlgos = (
    'Bubble Sort','Merge Sort','Quick Sort','Selection Sort', 'Heap Sort','Insertion Sort'
)
allCharts=(
    'Scatter Plot','Bar Chart','Stem Plot'
)
selectedAlgo = StringVar()
selectedCharts = StringVar()
pauseBool = False
arr = []
#-----------------------------
def generateRandomArray():
    #random array of non-repeating n elements
    global arr
    n = int(dataSize.get())
    arr = list(range(1, n + 1))
    random.shuffle(arr)

    arrayColor = ['red']  * n

    swapCount = 0
    comparisonCount = 0
    lookup[chartCombo.get()](arr,arrayColor,swapCount, comparisonCount)

def generateManualArray():
    global arr
    arr_str = inputEntry.get()
    arr = [int(num) for num in arr_str.split(',')]
    arrayColor = ['red']  * len(arr)

    swapCount = 0
    comparisonCount = 0
    lookup[chartCombo.get()](arr,arrayColor,swapCount, comparisonCount)

def normalizeArray(arr):
    m = max(arr)
    return [i / m for i in arr]

def displayScatter(arr,arrayColor,swapCount, comparisonCount):
    outputCanvas.delete('all')
    n = len(arr)

    outputCanvasWidth = outputCanvas.winfo_width() - 20
    outputCanvasHeight = outputCanvas.winfo_height() - 50

    barWidth = outputCanvasWidth/(n+1)
    barspace = 5
    initialspace = 10
    normalizedArr = normalizeArray(arr)

    for i, h in enumerate(normalizedArr):
        x = i * barWidth + initialspace + barspace + barWidth/2  # Sol tarafta boşluk için barWidth/2 eklendi
        y = outputCanvasHeight - h * 350
        outputCanvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=arrayColor[i])
        outputCanvas.create_text(x, y - 15, text=str(arr[i]), fill='black', font=('Arial', 10))


    countLabel = Label(outputCanvas,text = ' Değiştirme : '+ str(swapCount)+'\n Karşılaştırma : '+ str(comparisonCount),
                       fg = 'white',bg = 'black',font = ('Comic Sans MS',12))
    outputCanvas.create_window(80,80,window = countLabel)
    outputCanvas.create_line(initialspace, outputCanvasHeight, outputCanvasWidth, outputCanvasHeight, fill='black', width=1)

    root.update()

def displayArray(arr,arrayColor,swapCount, comparisonCount):
    outputCanvas.delete('all')
    n = len(arr)

    outputCanvasWidth = outputCanvas.winfo_width() - 20
    outputCanvasHeight = outputCanvas.winfo_height() - 50

    barWidth = outputCanvasWidth / (n + 1)
    barspace = 5
    initialspace = 10
    normalizedArr = normalizeArray(arr)

    for i, h in enumerate(normalizedArr):
        # Top-left corner
        x0 = i * barWidth + initialspace + barspace
        y0 = outputCanvasHeight - h * 350

        # Bottom-left corner
        x1 = (i + 1) * barWidth + initialspace
        y1 = outputCanvasHeight

        outputCanvas.create_rectangle(x0, y0, x1, y1, fill=arrayColor[i])
        outputCanvas.create_text((x0 + x1) / 2, y0 - 15, text=str(arr[i]), fill='black', font=('Arial', 10))

    countLabel = Label(outputCanvas,text = '#Değiştirme : '+str(swapCount)+'\n Karşılaştırma : '+ str(comparisonCount),
                       fg = 'white',bg = 'black',font = ('Comic Sans MS',12))
    outputCanvas.create_window(80,80,window = countLabel)
    outputCanvas.create_line(initialspace, outputCanvasHeight, outputCanvasWidth, outputCanvasHeight, fill='black', width=1)

    root.update()


def displayStem(arr,arrayColor,swapCount, comparisonCount):
    outputCanvas.delete('all')
    n = len(arr)

    outputCanvasWidth = outputCanvas.winfo_width() - 20
    outputCanvasHeight = outputCanvas.winfo_height() - 50

    barWidth = outputCanvasWidth / (n + 1)
    barspace = 5
    initialspace = 10
    normalizedArr = normalizeArray(arr)

    for i, h in enumerate(normalizedArr):
        x = i * barWidth + initialspace + barspace
        y = outputCanvasHeight - h * 350
        outputCanvas.create_line(x, outputCanvasHeight, x, y, fill=arrayColor[i], width=2)
        outputCanvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=arrayColor[i])
        outputCanvas.create_text(x, y - 15, text=str(arr[i]), fill='black', font=('Arial', 10))

    countLabel = Label(outputCanvas,text = '\n Değiştirme : '+ str(swapCount)+'\n Karşılaştırma : '+ str(comparisonCount),
                       fg = 'white',bg = 'black',font = ('Comic Sans MS',12))
    outputCanvas.create_window(80,80,window = countLabel)
    outputCanvas.create_line(initialspace, outputCanvasHeight, outputCanvasWidth, outputCanvasHeight, fill='black', width=1)

    root.update()



# Map from string to sorting function
lookup = {
    'Bubble Sort': bubbleSort,
    'Selection Sort': selectionSort,
    'Merge Sort': mergeSort,
    'Quick Sort': quickSort,
    'Heap Sort': heapSort,
    'Insertion Sort': insertionSort,
    'Bar Chart': displayArray,
    'Stem Plot': displayStem,
    'Scatter Plot': displayScatter
}


def startSort():
    global arr, pauseBool
    pauseBool = False

    s = time.time()  # Sıralama başlangıç zamanını kaydet
    fn = lookup[algoCombo.get()]
    fn(arr, lookup[chartCombo.get()], sortSpeed.get, pauseBool)

    e = time.time()  # Sıralama bitiş zamanını kaydet
    elapsed_time = e - s  # Geçen süreyi hesapla

    # Süreyi arayüzde göster
    time_label = Label(outputCanvas, text=f"Geçen Süre: {elapsed_time:.4f} sn", fg='white', bg='black',
                       font=('Comic Sans MS', 12))
    outputCanvas.create_window(10,10, anchor='nw', window=time_label)


#----User Interface Section---------------------------------------------------------------------------------------------
inputFrame = Frame(root, height=1500, bg='green')
inputFrame.grid(row=0, column=0, padx=0, pady=10, sticky='w')
inputFrame.columnconfigure(0, weight=1, minsize=75)
inputFrame.columnconfigure(1, weight=1, minsize=75)
inputFrame.columnconfigure(2, weight=1, minsize=75)
inputFrame.rowconfigure(0, weight=1, minsize=50)
inputFrame.rowconfigure(1, weight=1, minsize=50)
inputFrame.rowconfigure(2, weight=1, minsize=50)
inputFrame.rowconfigure(3, weight=1, minsize=50)

outputCanvas = Canvas(root, bg='#c8dedb')
outputCanvas.grid(row=0, column=1, columnspan=2, padx=10, pady=25, sticky='nsew')
root.columnconfigure(1, weight=1, minsize=75)
root.columnconfigure(2, weight=0, minsize=75)
root.rowconfigure(0, weight=0, minsize=50)

#--input frame-------------------------------------------------------
head = Label(inputFrame, text='Algoritma -> ', fg='black', bg='#ffff00', height=1, width=20, font=('Comic Sans MS', 14))
head.grid(row=0, column=0, padx=15, pady=5)

algoCombo = ttk.Combobox(inputFrame, values=allAlgos, width=10, font=('Comic Sans MS', 14))
algoCombo.grid(row=0, column=1, padx=1, pady=5)
algoCombo.current()

head = Label(inputFrame, text=' Grafik Türü -> ', fg='black', bg='#ffff00', height=1, width=20, font=('Comic Sans MS', 14))
head.grid(row=1, column=0, padx=15, pady=5)

chartCombo = ttk.Combobox(inputFrame, values=allCharts, width=10, font=('Comic Sans MS', 14))
chartCombo.grid(row=1, column=1, padx=1, pady=5)
chartCombo.current()

sortSpeed = Scale(inputFrame, from_=1, to=100, resolution=0.1, length=400, width=15, orient=HORIZONTAL, label='Hız [s]', font=('Comic Sans MS', 10))
sortSpeed.grid(row=2, column=0, padx=50, pady=5, columnspan=2, sticky='nsew')

dataSize = Scale(inputFrame, from_=3, to=100, resolution=1, length=400, width=15, orient=HORIZONTAL, label='Veri Boyutu [n]', font=('Comic Sans MS', 10))
dataSize.grid(row=3, column=0, padx=50, pady=5, columnspan=2, sticky='nsew')

generateRandom = Button(inputFrame, text='Rastgele Oluştur', fg='black', bg='#ff0000', height=1, width=20, font=('Comic Sans MS', 14), command=generateRandomArray)
generateRandom.grid(row=4, column=0, padx=10, pady=5, columnspan=2)

inputEntry = Entry(inputFrame, width=40, font=('Comic Sans MS', 14))
inputEntry.grid(row=5, column=0, columnspan=2, padx=50, pady=5)

generate = Button(inputFrame, text='Manuel Oluştur', fg='black', bg='#ff0000', height=1, width=20, font=('Comic Sans MS', 14), command=generateManualArray)
generate.grid(row=6, column=0, padx=5, pady=5, columnspan=2)

play = Button(inputFrame, text='Başla', fg='black', bg='#00ff00', height=1, width=10, font=('Comic Sans MS', 14), command=startSort)
play.grid(row=7, column=0, padx=5, pady=5, columnspan=2)


#--output frame------------------------------------------------------

root.rowconfigure(0, weight=1, minsize=50)
root.mainloop()
