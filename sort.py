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

shellist=[]
for i in range(10000):
    shellist.append( random.randint( 1,100) )
t1 = time.time()
shellSort( shellist )
t2 = time.time()
print( "ShellSort sort took {:.4f} seconds".format( t2-t1 ) )