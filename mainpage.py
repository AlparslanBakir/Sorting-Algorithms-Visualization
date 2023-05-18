
#---start import section-------------------
import time
import math
import random

from tkinter import Canvas, Frame, StringVar, Tk, Label, Button, Scale, HORIZONTAL
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
root_width = root.winfo_screenwidth()
root_height = root.winfo_screenheight()
root.geometry(f"{root_width}x{root_height}")
root.maxsize(root_width,root_height)   #(width,height)
root.config(bg='black')

#----GLOBAL VARIABLES---------
allAlgos = (
    'Bubble Sort','Merge Sort','Quick Sort','Selection Sort', 'Heap Sort','Insertion Sort'
)
allCharts=(
    'Scatter Chart','Bar Chart','Stem Plot'
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
    lookup[chartCombo.get()](arr,arrayColor,swapCount)

def normalizeArray(arr):
    m = max(arr)
    return [i / m for i in arr]

def displayScatter(arr,arrayColor,opCount):
    outputCanvas.delete('all')
    n = len(arr)

    outputCanvasHeight = 700 - 10
    outputCanvasWidth = 1900 - 10

    barWidth = outputCanvasWidth/(n+1)
    barspace = 5
    initialspace = 10
    normalizedArr = normalizeArray(arr)

    for i, h in enumerate(normalizedArr):
        x = i * barWidth + initialspace + barspace + barWidth/2  # Sol tarafta boşluk için barWidth/2 eklendi
        y = outputCanvasHeight - h * 350
        outputCanvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=arrayColor[i])


    swapCountLabel = Label(outputCanvas,text = '#Swap Count : '+str(opCount),fg = 'white',bg = 'black',font = ('Comic Sans MS',12))
    outputCanvas.create_window(80,20,window = swapCountLabel)

    root.update()

def displayArray(arr,arrayColor,opCount):
    outputCanvas.delete('all')
    n = len(arr)

    outputCanvasHeight = 700 - 10
    outputCanvasWidth = 1800 - 20

    barWidth = outputCanvasWidth/(n+1)
    barspace = 5
    initialspace = 10
    normalizedArr = normalizeArray(arr)

    for i,h in enumerate(normalizedArr):
        #top - left                                           #|(x0,y0)-------------|
        x0 = i*barWidth+initialspace+barspace                 #|                    |
        y0 = outputCanvasHeight - h*350                       #|                    |
                                                              #|                    |
        #bottom-left                                          #|                    |
        x1 = (i+1)*barWidth+initialspace                      #|                    |
        y1 = outputCanvasHeight                               #|-------------(x1,y1)|

        outputCanvas.create_rectangle(x0,y0,x1,y1, fill = arrayColor[i])

    swapCountLabel = Label(outputCanvas,text = '#Swap Count : '+str(opCount),fg = 'white',bg = 'black',font = ('Comic Sans MS',12))
    outputCanvas.create_window(80,20,window = swapCountLabel)

    root.update()

def displayStem(arr, arrayColor, opCount):
    outputCanvas.delete('all')
    n = len(arr)

    outputCanvasHeight = 700 - 10
    outputCanvasWidth = 1800 - 20

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

    swapCountLabel = Label(outputCanvas, text='#Swap Count : ' + str(opCount), fg='white', bg='black',
                           font=('Comic Sans MS', 12))
    outputCanvas.create_window(80, 20, window=swapCountLabel)

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
    'Scatter Chart': displayScatter
}


def startSort():
    global arr
    fn = lookup[algoCombo.get()]
    fn(arr, lookup[chartCombo.get()], sortSpeed.get, pauseBool)


#----User Interface Section---------------------------------------------------------------------------------------------
inputFrame = Frame(root,height = 200,width = 950,bg = 'black')
inputFrame.grid(row = 0,column = 0,padx = 10,pady = 10)
 

outputCanvas = Canvas(root, bg='#99ffff')
outputCanvas.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)




#--input frame-------------------------------------------------------
head = Label(inputFrame,text = 'Select Algorithm -> ',fg = 'black',bg = '#ffff00',height = 1,width = 15,font = ('Comic Sans MS',14))
head.grid(row = 0,column = 0,padx = 5,pady = 5)

algoCombo = ttk.Combobox(inputFrame,values = allAlgos,width = 15,font = ('Comic Sans MS',14))
algoCombo.grid(row = 0,column = 1,padx = 5,pady = 5)
algoCombo.current()

head = Label(inputFrame,text = 'Select Chart Type -> ',fg = 'black',bg = '#ffff00',height = 1,width = 15,font = ('Comic Sans MS',14))
head.grid(row = 3,column = 0,padx = 5,pady = 5)

chartCombo = ttk.Combobox(inputFrame,values = allCharts,width = 15,font = ('Comic Sans MS',14))
chartCombo.grid(row = 3,column = 1,padx = 5,pady = 5)
chartCombo.current()

generate = Button(inputFrame,text = 'Generate',fg = 'black',bg = '#ff0000',height = 1,width = 10,font = ('Comic Sans MS',14),command = generateRandomArray )
generate.grid(row = 0,column = 2,padx = 5,pady = 5)

dataSize = Scale(inputFrame,from_ = 3,to = 100,resolution = 1,length = 400,width = 15,orient = HORIZONTAL,label = 'Data Size [n]',font = ('Comic Sans MS',10))
dataSize.grid(row = 1,column = 0,padx = 5,pady = 5,columnspan = 2)

sortSpeed = Scale(inputFrame,from_ = 1,to = 100,resolution = 0.1,length = 400,width = 15,orient = HORIZONTAL,label = 'Sorting Speed [s]',font = ('Comic Sans MS',10))
sortSpeed.grid(row = 2,column = 0,padx = 5,pady = 5,columnspan = 2)

play = Button(inputFrame,text = 'Play',fg = 'black',bg = '#00ff00',height = 5,width = 10,font = ('Comic Sans MS',14),command = startSort )
play.grid(row = 1,column = 2,padx = 5,pady = 5,rowspan = 2)

#--output frame------------------------------------------------------

root.mainloop()
