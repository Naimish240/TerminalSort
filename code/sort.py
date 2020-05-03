# -----------------------------------------------------------
# Creator : Naimish Mani B
# Date    : 3rd May 2020
# -----------------------------------------------------------
# Implementing the various sorting algorithms and visualising them
# Timing each algorithm with time
# Initialising arrays and shuffling them with random
# Clear Screen function with os
# -----------------------------------------------------------
# Import Statements
import time
import os
import random
# -----------------------------------------------------------
# Dictionary storing algorithm and average time complexity
details = {
    'Selection Sort' : 'n^2',
    'Cocktail Sort'  : 'n^2',
    'Quick Sort'     : 'n log (n)',
    'Bogo Sort'      : '(n+1)!',
    'Bubble Sort'    : 'n^2',
    'Insertion Sort' : 'n^2',
    'Comb Sort'      : 'n^2/2^p',
    'Shell Sort'     : 'n (log n)^2'
}
# -----------------------------------------------------------
# Function to Clear the Screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# -----------------------------------------------------------
# Visualises sorting algorithm, used only by bogo sort tho.
def update_screen(arr, algo):
    global vis
    if vis:
        clear_screen()
        to_show = []
        print("> Algorithm  : {}".format(algo))
        print("> Complexity : θ({})".format(details[algo]))
        print('********************************************')
        for i in arr:
            if int(i) < 10:
                to_show.append('[{}]  : {}'.format(i, '#'*i))    
            else:
                to_show.append('[{}] : {}'.format(i, '#'*i))
        for i in to_show:
            print(i)
        print('********************************************')
        time.sleep(0.10)        
# -----------------------------------------------------------
# Visualises comparing
def compare_screen(arr, algo, j, k):
    global vis
    if vis:
        clear_screen()
        to_show = []
        print("> Algorithm  : {}".format(algo))
        print("> Complexity : θ({})".format(details[algo]))
        print('********************************************')
        for i in arr:
            # Element to be compared
            if i == j or i == k:
                if int(i) < 10:
                    to_show.append('[{}]  : \033[33m{}\033[00m'.format(i, '#'*i))    
                else:
                    to_show.append('[{}] : \033[33m{}\033[00m'.format(i, '#'*i))
            else:
                if int(i) < 10:
                    to_show.append('[{}]  : {}'.format(i, '#'*i))    
                else:
                    to_show.append('[{}] : {}'.format(i, '#'*i))
        for i in to_show:
            print(i)
        print('********************************************')
        time.sleep(0.25)
# -----------------------------------------------------------
# Visualises swapping
def swap_screen(arr, algo, j, k):
    global vis
    if vis:
        clear_screen()
        to_show = []
        print("> Algorithm  : {}".format(algo))
        print("> Complexity : θ({})".format(details[algo]))
        print('********************************************')
        for i in arr:
            # Element to be compared
            if i == j or i == k:
                if int(i) < 10:
                    to_show.append('[{}]  : \033[34m{}\033[00m'.format(i, '#'*i))    
                else:
                    to_show.append('[{}] : \033[34m{}\033[00m'.format(i, '#'*i))
            else:
                if int(i) < 10:
                    to_show.append('[{}]  : {}'.format(i, '#'*i))    
                else:
                    to_show.append('[{}] : {}'.format(i, '#'*i))
        for i in to_show:
            print(i)
        print('********************************************')
        time.sleep(0.25)
# -----------------------------------------------------------
# Riff
# Function to give colors to the riff
def colored(arr, i):
    a = []
    for j in range(1, i+1):
        if j < 10:
            a.append('[{}]  : \033[32m{}\033[00m'.format(j, '#'*j))    
        else:
            a.append('[{}] : \033[32m{}\033[00m'.format(j, '#'*j))
    for j in range(i+1, len(arr)+1):
        if j < 10:
            a.append('[{}]  : {}'.format(j, '#'*j))  
        else:
            a.append('[{}] : {}'.format(j, '#'*j))
    return a
# Event loop for the riff
def riff(arr, algo):
    global vis
    if vis:
        to_show = []
        for i in range(1, len(arr)+1):
            clear_screen()
            to_show = colored(arr, i)
            print("> Algorithm  : {}".format(algo))
            print("> Complexity : θ({})".format(details[algo]))
            print('********************************************')
            for i in to_show:
                print(i)
            print('********************************************')
            time.sleep(0.1)
# -----------------------------------------------------------
# Selection Sort
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        flag = i
        for j in range(i+1, n):
            compare_screen(arr, "Selection Sort", arr[flag], arr[j])
            if arr[flag] > arr[j]:
                flag = j
        arr[i], arr[flag] = arr[flag], arr[i]
        swap_screen(arr, "Selection Sort", arr[i], arr[flag])
    riff(arr, "Selection Sort")
# -----------------------------------------------------------
# Cocktail Sort
def cocktailSort(arr):
    n = len(arr)
    swap = True
    start = 0
    end = n-1
    while(swap):
        swap = False
        # Forward pass
        for i in range(start, end):
            compare_screen(arr, "Cocktail Sort", arr[i], arr[i+1])
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_screen(arr, "Cocktail Sort", arr[i], arr[i+1])
                swap = True
        if not swap:
            break
        end -= 1
        # Backwards pass
        for i in range(end-1, start-1, -1):
            compare_screen(arr, "Cocktail Sort", arr[i], arr[i+1])
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_screen(arr, "Cocktail Sort", arr[i], arr[i+1])
                swap = True
        start += 1
    riff(arr, "Cocktail Sort")
# -----------------------------------------------------------
# Quick Sort
def quickSort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSort(less)+equal+quickSort(greater) 
    else:
        return arr
# -----------------------------------------------------------
# Bogo Sort
def bogoSort(arr):
    while(not sorted(arr)):
        arr = shuffle(arr)
        update_screen(arr, "Bogo Sort")
    riff(arr, "Bogo Sort")
    return arr
# Function to check if array is sorted or not
def sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
# -----------------------------------------------------------
# Bubble Sort
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1):
            compare_screen(arr, "Bubble Sort", arr[j], arr[j+1])
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_screen(arr, "Bubble Sort", arr[j], arr[j+1])
    riff(arr, "Bubble Sort")
# ----------------------------------------------------------- 
# Insertion Sort
def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] :
            compare_screen(arr, "Insertion Sort", arr[j], arr[j+1])
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key
    riff(arr, "Insertion Sort")
# ----------------------------------------------------------- 
# Comb Sort
# To find next gap from current 
def getNextGap(gap): 
    # Shrink gap by Shrink factor 
    gap = (gap * 10)//13
    if gap < 1: 
        return 1
    return gap 
def combSort(arr): 
    n = len(arr) 
    gap = n 
    swapped = True
    while gap !=1 or swapped == 1:
        gap = getNextGap(gap)  
        swapped = False
        for i in range(n-gap):
            compare_screen(arr, "Comb Sort", arr[i], arr[i + gap])
            if arr[i] > arr[i + gap]: 
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swap_screen(arr, "Comb Sort", arr[i], arr[i + gap])
                swapped = True
    riff(arr, "Comb Sort")
# ----------------------------------------------------------- 
# Shell Sort
def shellSort(arr): 
    n = len(arr) 
    gap = n//2
    while gap > 0: 
        for i in range(gap,n): 
            temp = arr[i] 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
                compare_screen(arr, "Shell Sort", arr[j], arr[j+1])
            arr[j] = temp 
        gap //= 2
    riff(arr, "Shell Sort")
# ----------------------------------------------------------- 
def shuffle(arr):
    for i in range(len(arr)):
        r = random.randint(0, len(arr)-1)
        arr[i], arr[r] = arr[r], arr[i]
    return arr
# ----------------------------------------------------------- 
# Generate Array
def genArr(n):
    arr = [i for i in range(1, n+1)]
    arr = shuffle(arr)
    return arr
# ----------------------------------------------------------- 
# Times each sorting algorithm
def sorts(n):
    # Quick sort
    t0 = time.time()
    quickSort(genArr(n))
    t1 = time.time()
    print("Quick sort took:     {} seconds.".format(t1-t0))
    time.sleep(0.1)
    # Selection sort
    t0 = time.time()
    selectionSort(genArr(n))
    t1 = time.time()
    time.sleep(0.1)
    print("Selection sort took: {} seconds.".format(t1-t0))
    # Cocktail sort
    t0 = time.time()
    cocktailSort(genArr(n))
    t1 = time.time()
    time.sleep(0.1)
    print("Cocktail sort took:  {} seconds.".format(t1-t0))
    # Bogo sort
    # Only on small arrays. You'd have to be stupid to use it in the real world
    if n < 11:
        t0 = time.time()
        bogoSort(genArr(n))
        t1 = time.time()
        print("Bogo sort took:      {} seconds.".format(t1-t0))
    else:
        time.sleep(3)
        print("Bogo sort took:      Too many seconds.")
    time.sleep(0.1)
    # Bubble sort
    t0 = time.time()
    bubbleSort(genArr(n))
    t1 = time.time()
    time.sleep(0.1)
    print("Bubble sort took:    {} seconds.".format(t1-t0))
    # Insertion sort
    t0 = time.time()
    insertionSort(genArr(n))
    t1 = time.time()
    time.sleep(0.1)
    print("Insertion sort took: {} seconds.".format(t1-t0))
    # Comb sort
    t0 = time.time()
    combSort(genArr(n))
    t1 = time.time()
    time.sleep(0.1)
    print("Comb sort took:      {} seconds.".format(t1-t0))
    # Shell sort
    t0 = time.time()
    shellSort(genArr(n))
    t1 = time.time()
    print("Shell sort took:     {} seconds.".format(t1-t0))
    time.sleep(0.1)
# ----------------------------------------------------------- 
# Function to compare runtime of algorithms on random arrays
def compare():
    # Comparing each algorithm's execution time
    print('************************************')
    print("For a small array of 10 elements")
    sorts(10)
    print('************************************')
    print("For a medium array of 100 elements")
    sorts(100)
    print('************************************')
    print("For a large array of 10000 elements")
    sorts(10000)
    print('************************************')
# ----------------------------------------------------------- 
# Main function
def main():
    global vis, row
    while True:
        clear_screen()
        print("'1' for Selection Sort")
        print("'2' for Cocktail Sort")
        print("'3' for Bogo Sort")
        print("'4' for Bubble Sort")
        print("'5' for Insertion Sort")
        print("'6' for Comb Sort")
        print("'7' for Shell Sort")
        print("'8' to view comparision")
        print("'9' to quit")
        ch = int(input("> Enter Your Choice : "))
        if ch == 1:
            selectionSort(genArr(row-6))
            time.sleep(1)
        if ch == 2:
            cocktailSort(genArr(row-6))
            time.sleep(1)
        if ch == 3:    
            bogoSort(genArr(5))
            time.sleep(1)
        if ch == 4:
            bubbleSort(genArr(row-6))
            time.sleep(1)
        if ch == 5:
            insertionSort(genArr(row-6))
            time.sleep(1)
        if ch == 6:
            combSort((genArr(row-6)))
            time.sleep(1)
        if ch == 7:
            shellSort(genArr(row-6))
            time.sleep(1)
        if ch == 8:
            vis = False
            compare()
            vis = True
            time.sleep(5)
        if ch == 9:
            break
    clear_screen()
# ----------------------------------------------------------- 
# Global Variables
# Visualise?
vis = True
# Determines number of rows supported by the open window
row = os.get_terminal_size()[1]
# ----------------------------------------------------------- 
if __name__ == '__main__':
    main()
# -----------------------------------------------------------