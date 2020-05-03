# TerminalSort
Sorting algorithms are one of those topics stressed upon in CS degrees, but they are also very easy to forget and also hard to understand. I personally like to visualise algorithms in an attempt to better understand them.

Most often than not, sorting algorithms are taught in CS classes when the students have just begun to work with languages like C, C++ and Python. In this primative state of programming, most studens are just comfortable with working form the terminal.

So, what better a way to visualise these important algorithms than to see them from the terminal! That's what this project set out to "see" (pun intended). The main objective of this project was to establish the fact that one need not have to use complicated tools to render and visualise sorting algorithms, but they can be easily understood from the terminal too.

# Usage
Since this program has no external dependancies, you can easily use it by cloning this repo and running "sort.py" in the code folder.

Colors have been provided by using ANSI escape codes, and should hence run on all platforms. 

# Algorithms

####1. Selection Sort
Scan all items and find the smallest. Swap it into position as the first item. Repeat the selection sort on the remaining N-1 items.

####2. Cocktail Sort
Cocktail Sort is a variation of Bubble sort. The Bubble sort algorithm always traverses elements from left and moves the largest element to its correct position in first iteration and second largest in second iteration and so on. Cocktail Sort traverses through a given array in both directions alternatively.

####3. Quick Sort
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. Given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

####4. Bogo Sort
Created as a joke. This algorithm works by randomly shuffle array and hoping it's sorted. It's bound to happen, right?

####5. Bubble Sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

####6. Insertion Sort
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than other algorithms. When people manually sort cards in a bridge hand, most use a method that is similar to insertion sort.

####7. Comb Sort
Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always compares adjacent values. So all inversions are removed one by one. Comb Sort improves on Bubble Sort by using gap of size more than 1. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1. Thus Comb Sort removes more than one inversion counts with one swap and performs better than Bubble Sort. The shrink factor has been empirically found to be 1.3 (by testing Combsort on over 200,000 random lists)

####8. Shell Sort
Shell sort is a highly efficient sorting algorithm and is based on insertion sort algorithm. This algorithm avoids large shifts as in case of insertion sort, if the smaller value is to the far right and has to be moved to the far left. This algorithm uses insertion sort on a widely spread elements, first to sort them and then sorts the less widely spaced elements. This spacing is termed as interval. This interval is calculated based on Knuth's formula.