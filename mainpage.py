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

    arrayColor = ['#E06469']  * n

    swapCount = 0
    comparisonCount = 0
    lookup[chartCombo.get()](arr,arrayColor,swapCount, comparisonCount)

def generateManualArray():
    global arr

    arr_str = inputEntry.get()
    arr = [int(num) for num in arr_str.split(',')]
    arrayColor = ['#E06469']  * len(arr)

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
                       fg = 'black',bg='#70A1D7',font = ('Comic Sans MS',13))
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
                       fg = 'black',bg='#70A1D7',font = ('Comic Sans MS',13))
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

    countLabel = Label(outputCanvas,text = ' Değiştirme : '+ str(swapCount)+'\n Karşılaştırma : '+ str(comparisonCount),
                       fg = 'black',bg='#70A1D7',font = ('Comic Sans MS',13))
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

def get_complexity(complexity_type, algorithm_name):
    superscript_2 = "\u00B2"
    if algorithm_name == "Insertion Sort":
        if complexity_type == "best":
            return "O(n)"
        elif complexity_type == "worst":
            return "O(n"+ superscript_2+")"
        elif complexity_type == "average":
            return "O(n"+ superscript_2+")"
        elif complexity_type == "space":
            return "O(1)"
    elif algorithm_name == "Merge Sort":
        if complexity_type in ["best","worst","average"]:
            return "O(n log n)"
        elif complexity_type == "space":
            return "O(n)"
    elif algorithm_name == "Quick Sort":
        if complexity_type == "best":
            return "O(n log n)"
        elif complexity_type == "worst":
            return "O(n"+ superscript_2+")"
        elif complexity_type == "average":
            return "O(n log n)"
        elif complexity_type == "space":
            return "O(log n)"
    elif algorithm_name == "Bubble Sort":
        if complexity_type == "best":
            return "O(n)"
        elif complexity_type == "worst":
            return "O(n"+ superscript_2+")"
        elif complexity_type == "average":
            return "O(n"+ superscript_2+")"
        elif complexity_type == "space":
            return "O(1)"
    elif algorithm_name == "Heap Sort":
        if complexity_type in ["best", "worst", "average"]:
            return "O(n log n)"
        elif complexity_type == "space":
            return "O(1)"
    elif algorithm_name == "Selection Sort":
        if complexity_type in ["best", "worst","average"]:
            return "O(n"+ superscript_2+")"
        elif complexity_type == "space":
            return "O(1)"
    else:
        return "Karmaşıklık bilgisi bulunamadı."

def startSort():
    global arr, pauseBool
    pauseBool = False

    s = time.time()  # Sıralama başlangıç zamanını kaydet
    fn = lookup[algoCombo.get()]
    fn(arr, lookup[chartCombo.get()], sortSpeed.get, pauseBool)

    e = time.time()  # Sıralama bitiş zamanını kaydet
    elapsed_time = e - s  # Geçen süreyi hesapla

    # Süreyi arayüzde göster
    time_label = Label(outputCanvas, text=f"Geçen Süre: {elapsed_time:.3f} sn", fg='black', bg='#70A1D7',
                       font=('Comic Sans MS', 13))
    outputCanvas.create_window(10,10, anchor='nw', window=time_label)

    # En iyi, en kötü, ortalama ve alan karmaşıklığını çek
    algorithm_name = algoCombo.get()
    best_case = get_complexity("best", algorithm_name)
    worst_case = get_complexity("worst", algorithm_name)
    average_case = get_complexity("average", algorithm_name)
    space_complexity = get_complexity("space", algorithm_name)

    # Karmaşıklık verilerini arayüzde göster
    complexity_label = Label(outputCanvas, text="Karmaşıklık Analizi:", fg='black', bg='#70A1D7',
                             font=('Comic Sans MS', 13))
    outputCanvas.create_window(200, 10, anchor='nw', window=complexity_label)

    best_label = Label(outputCanvas, text=f"En İyi : {best_case}", fg='black', bg='#70A1D7',
                       font=('Comic Sans MS', 13))
    outputCanvas.create_window(200, 40, anchor='nw', window=best_label)

    worst_label = Label(outputCanvas, text=f"En Kötü : {worst_case}", fg='black', bg='#70A1D7',
                        font=('Comic Sans MS', 13))
    outputCanvas.create_window(200, 70, anchor='nw', window=worst_label)

    average_label = Label(outputCanvas, text=f"Ortalama : {average_case}", fg='black', bg='#70A1D7',
                          font=('Comic Sans MS', 13))
    outputCanvas.create_window(200, 100, anchor='nw', window=average_label)

    space_label = Label(outputCanvas, text=f"Alan Karmaşıklığı: {space_complexity}", fg='black', bg='#70A1D7',
                        font=('Comic Sans MS', 13))
    outputCanvas.create_window(200, 130, anchor='nw', window=space_label)

    root.update()


#----User Interface Section---------------------------------------------------------------------------------------------
inputFrame = Frame(root, height=1500, bg='#AFD3E2')
inputFrame.grid(row=0, column=0, padx=20, pady=10, sticky='w')
inputFrame.columnconfigure(0, weight=1, minsize=75)
inputFrame.columnconfigure(1, weight=1, minsize=75)
inputFrame.columnconfigure(2, weight=1, minsize=75)
inputFrame.rowconfigure(0, weight=1, minsize=50)
inputFrame.rowconfigure(1, weight=1, minsize=50)
inputFrame.rowconfigure(2, weight=1, minsize=50)
inputFrame.rowconfigure(3, weight=1, minsize=50)

outputCanvas = Canvas(root, bg='#AFD3E2') # #c8dedb
outputCanvas.grid(row=0, column=1, columnspan=2, padx=10, pady=25, sticky='nsew')
root.columnconfigure(1, weight=1, minsize=75)
root.columnconfigure(2, weight=0, minsize=75)
root.rowconfigure(0, weight=0, minsize=50)

#--input frame-------------------------------------------------------
head = Label(inputFrame, text='ALGORİTMA -> ', fg='black', bg='#AFD3E2',highlightbackground='#AFD3E2',height=1, width=20, font=('Comic Sans MS', 14,'bold'))#19A7CE
head.grid(row=0, column=0, padx=20, pady=5)

algoCombo = ttk.Combobox(inputFrame, values=allAlgos, width=10, font=('Comic Sans MS', 14))
algoCombo.grid(row=0, column=1, padx=1, pady=5)
algoCombo.current()

head = Label(inputFrame, text=' GRAFİK TÜRÜ -> ', fg='black', bg='#AFD3E2',highlightbackground='#AFD3E2', height=1, width=20, font=('Comic Sans MS', 14,'bold'))#82DBD8
head.grid(row=1, column=0, padx=20, pady=5)

chartCombo = ttk.Combobox(inputFrame, values=allCharts, width=10, font=('Comic Sans MS', 14))
chartCombo.grid(row=1, column=1, padx=1, pady=5)
chartCombo.current()#AFD3E2
#AFD3E2

sortSpeed = Scale(inputFrame, from_=1, to=100, resolution=0.1, length=400, width=15, bg='#AFD3E2',troughcolor="white",fg='black',highlightbackground='#AFD3E2', orient=HORIZONTAL, label='Hız [s]', font=('Comic Sans MS', 10,'bold'))
sortSpeed.grid( row=2, column=0, padx=50, pady=5, columnspan=2, sticky='nsew')

dataSize = Scale(inputFrame, from_=3, to=100, resolution=1, length=400, width=15,bg='#AFD3E2',troughcolor="white",fg='black',highlightbackground='#AFD3E2',  orient=HORIZONTAL, label='Veri Boyutu [n]', font=('Comic Sans MS', 10,'bold'))
dataSize.grid(row=3, column=0, padx=50, pady=5, columnspan=2, sticky='nsew')

generateRandom = Button(inputFrame, text='Rastgele Oluştur', fg='white', bg='#2155CD', height=1, width=20, font=('Comic Sans MS', 14), command=generateRandomArray)
generateRandom.grid(row=4, column=0, padx=10, pady=5, columnspan=2)

inputEntry = Entry(inputFrame, width=40, font=('Comic Sans MS', 14))
inputEntry.grid(row=5, column=0, columnspan=2, padx=50, pady=5)


generate = Button(inputFrame, text='Manual Oluştur', fg='white', bg='#04009A', height=1, width=20, font=('Comic Sans MS', 14), command=generateManualArray)
generate.grid(row=6, column=0, padx=5, pady=5, columnspan=2)

play = Button(inputFrame, text='     Başla    ', fg='white', bg='#03045E', height=1, width=10, font=('Comic Sans MS', 14), command=startSort)
play.grid(row=7, column=0, padx=20, pady=20, columnspan=2)

#--output frame------------------------------------------------------

root.rowconfigure(0, weight=1, minsize=50)
root.mainloop()
