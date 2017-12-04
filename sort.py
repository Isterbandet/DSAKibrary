import random, time
def bubbleSort( alist ):
    for passnum in range( len(alist)-1,0,-1 ):
        for i in range( passnum ):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp




def selectionSort( alist ):
    for start_pos in range( 0, len(alist ) ):
        positionOfMin=start_pos
        for i in range( start_pos+1, len(alist) ):
            if alist[i] < alist[positionOfMin]:
                positionOfMin=i
 # swap:
        temp = alist[positionOfMin]
        alist[positionOfMin] = alist[start_pos]
        alist[start_pos] = temp


def insertionSort( alist ):
    for index in range( 1, len( alist ) ):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position- 1] > currentvalue:
            alist[position] = alist[position- 1]
            position = position- 1
            alist[position] = currentvalue



def shellSort(array):
    # Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1.
    gap = len(array) // 2
    # loop over the gaps
    while gap > 0:
        # do the insertion sort
        for i in range(gap, len(array)):
            val = array[i]
            j = i
            while j >= gap and array[j - gap] > val:
                array[j] = array[j - gap]
                j -= gap
            array[j] = val
        gap //= 2 # ny gap


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
"""
bubblelist=[]
for i in range(8000):
    bubblelist.append( random.randint( 1,100) )
t1 = time.time()
bubbleSort( bubblelist )
t2 = time.time()
print( "Bubble sort took {:.4f} seconds".format( t2-t1 ) )

mylist=[]
for i in range(8000):
    mylist.append( random.randint( 1,100) )
t1 = time.time()
selectionSort( mylist )
t2 = time.time()
print( "selectionSort sort took {:.4f} seconds".format( t2-t1 ) )

insertionlist=[]
for i in range(8000):
    insertionlist.append( random.randint( 1,100) )
t1 = time.time()
insertionSort( insertionlist )
t2 = time.time()
print( "Insertiort sort took {:.4f} seconds".format( t2-t1 ) )

quicklist=[]
for i in range(1000000):
    quicklist.append( random.randint( 1,50000) )
t1 = time.time()
n = len(quicklist)
quickSort( quicklist,0,n-1 )
t2 = time.time()
print( "quickSort sort took {:.4f} seconds".format( t2-t1 ) )

shellist=[]
for i in range(1000000):
    shellist.append( random.randint( 1,100) )
t1 = time.time()
shellSort( shellist )
t2 = time.time()
print( "ShellSort sort took {:.4f} seconds".format( t2-t1 ) )



mergelistt=[]
for i in range(1000000):
    mergelistt.append( random.randint( 1,300) )
t1 = time.time()
n = len(mergelistt)
mergeSort( mergelistt,0,n-1 )
t2 = time.time()
print( "Merge sort took {:.4f} seconds".format( t2-t1 ) )


heaplistt=[]
for i in range(1000000):
    heaplistt.append( random.randint( 1,300) )
t1 = time.time()
n = len(heaplistt)
mergeSort( heaplistt,0,n-1 )
t2 = time.time()
print( "Heap sort took {:.4f} seconds".format( t2-t1 ) )

"""