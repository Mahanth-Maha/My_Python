class mSort():
    #selection Sort
    def selectionSort(A):
        n = len(A)
        for i in range(n):
            minn = i
            for j in range(i+1,n):
                minn = j if A[j] < A[minn] else minn
            A[i],A[minn] = A[minn],A[i]
        return A
        
    #insertion Sort
    def insertionSort(A):
        for j in range(1,len(A)):
            picked = A[j]
            i = j-1
            while ( picked < A[i] and i >= 0 ):
                A[i+1] = A[i] 
                i -= 1
            A[i+1] = picked
        return A
    
        
    #Bubble Sort
    def bubbleSort(A):
        n = len(A)
        for i in range(n-1):
            flag = False
            for j in range(n-(i+1)):
                if A[j] > A[j+1]:
                    A[j],A[j+1] = A[j+1],A[j]
                    flag = True
            if flag == False:
                return A
        return A
    
    #quick sort
    def partition(A,p,r):
        pivot = A[r]
        i = p-1
        for j in range(p,r):
            if A[j] < pivot:
                i += 1
                A[i],A[j] = A[j],A[i]
        A[i+1],A[r] = A[r],A[i+1] 
        return A,i+1

    def qs(A,p,r):
        if p < r:
            A,q = mSort.partition(A,p,r)
            A = mSort.qs(A,p,q-1)
            A = mSort.qs(A,q+1,r)
        return A

    def quickSort(A):
        n = len(A)
        return mSort.qs(A,0,n-1)
    
    #merge sort
    def merge(A,p,q,r):
        L = A[p:q+1]
        L.append(float('inf'))
        R = A[q+1:r+1]
        R.append(float('inf'))
        i = 0
        j = 0
        for k in range(p,r+1):
            if L[i] < R[j]:
                A[k] = L[i]
                i+= 1
            else:
                A[k] = R[j]
                j+= 1
        return A

    def mers(A,p,r):
        if p < r:
            q = (p+r)//2
            A = mSort.mers(A,p,q)
            A = mSort.mers(A,q+1,r)
            A = mSort.merge(A,p,q,r)
        return A
        
    def mergeSort(A):
        return mSort.mers(A,0,len(A)-1)
    
    #heap sort
    def heapSort(A):
        import heapq
        n = len(A)
        heapq.heapify(A)
        B = []
        for i in range(n-1,-1,-1):
            m = heapq.heappop(A)
            B.append(m) 
        return B


    # counting Sort
    def countingSort(A):
        mini = min(A)
        maxi = max(A)
        if maxi- mini <= 10**9:
            Slots = [0 for i in range(maxi-mini+1)]
            for i in A:
                Slots[i-mini] += 1
            k = 0
            for i in range(len(Slots)):
                for j in range(Slots[i]):
                    A[k] = i + mini
                    k+=1
        return A
    
    #py sort - timsort
    def timSort(A):
        return A.sort()

def check_sort(arr,arr_act,decreasing = False):
    for i in range(len(arr) - 1):
        if decreasing:
            if arr[i] < arr[i+1]:
                return False
            return check_actual(arr,arr_act,decreasing)
        else:
            if arr[i] > arr[i+1]:
                return False
            return check_actual(arr,arr_act,decreasing)

def check_actual(arr,arr_act,dec =False):
    arr_act.sort(reverse=dec)
    for i,j in zip(arr,arr_act):
        if i!=j:
            return False
    return True
        

def main():
    print("\nAlmost All Sorting Algos i Know\n","*"*25)
    import random
    l = [ random.randint(0,1000) for _ in range(10)]    
    print("\nO(n^2) Sorting Algos... \n"+"-"*30)
    
    print("SELECTION OK") if check_sort(mSort.selectionSort(l.copy()),l) else print("SELECTION FAIL")
    l = [ random.randint(0,1000) for _ in range(10)]    
    print("INSERTION OK") if check_sort(mSort.insertionSort(l.copy()),l) else print("INSERTION FAIL")
    l = [ random.randint(0,1000) for _ in range(10)]    
    print("BUBBLE OK") if check_sort(mSort.bubbleSort(l.copy()),l) else print("BUBBLE FAIL")
    l = [ random.randint(0,1000) for _ in range(10)]    
    print("\nQUICK OK") if check_sort(mSort.quickSort(l.copy()),l) else print("\nQUICK FAIL")
    
    print("\nO(n*log(n)) Sorting Algos... \n"+"-"*30)
    l = [ random.randint(0,1000) for _ in range(10)]    
    print("MERGE OK") if check_sort(mSort.mergeSort(l.copy()),l) else print("MERGE FAIL")
    l = [ random.randint(0,1000) for _ in range(10)]    
    print("HEAP OK") if check_sort(mSort.heapSort(l.copy()),l) else print("HEAP FAIL")
    
    print("\nLess than O(n*log(n)) Sorting Algos... (Special Cases only) \n"+"-"*30)
    l = [ random.randint(0,10) for _ in range(50)]    
    print("Counting Sort OK") if check_sort(mSort.countingSort(l.copy()),l) else print("Counting Sort FAIL")

import random
from time import time_ns
def benchmark():
    # t1()
    # t2()
    t3()
    # t4()

def single_timeit(l):
    d = dict()
    s = time_ns()
    mSort.selectionSort(l.copy()) 
    e = time_ns()
    d['selectionSort'] = e-s
    print('[+] selectionSort')
    s = time_ns()
    mSort.insertionSort(l.copy()) 
    e = time_ns()
    d['insertionSort'] = e-s
    print('[+] insertionSort')
    s = time_ns()
    mSort.bubbleSort(l.copy()) 
    e = time_ns()
    d['bubbleSort'] = e-s
    print('[+] bubbleSort')
    s = time_ns()
    mSort.quickSort(l.copy())
    e = time_ns()
    d['quickSort'] = e-s
    print('[+] quickSort')
    s = time_ns()
    mSort.mergeSort(l.copy()) 
    e = time_ns()
    d['mergeSort'] = e-s
    print('[+] mergeSort')
    s = time_ns()
    mSort.heapSort(l.copy())
    e = time_ns()
    d['heapSort'] = e-s
    print('[+] heapSort')
    s = time_ns()
    mSort.countingSort(l.copy())
    e = time_ns()
    d['countingSort'] = e-s
    print('[+] countingSort')
    # py builtin sort
    s = time_ns()
    mSort.timSort(l.copy())
    e = time_ns()
    d['timSort'] = e-s
    print('[+] timSort')

    return d


def t1():
    d = {}
    print("Testing 1 : Ascending sorted array")
    t1_1 = [ i for i in range(10**3)]
    print("\teasy\t")
    d['easy'] = single_timeit(t1_1)
    print(d)
    del t1_1
    t1_2 = [ i for i in range(10**6)]
    print("\tmedium\t")
    d['medium'] = single_timeit(t1_2)
    print(d)
    del t1_2
    t1_3 = [ i for i in range(10**9)]
    print("\thard\t")
    d['hard'] = single_timeit(t1_3)
    print(d)
    del t1_3
def t2():
    print("Testing 2 : decending sorted array")
    t2_1 = [ i for i in range(10**3,0,-1)]
    print("\teasy\t")
    del t2_1
    t2_2 = [ i for i in range(10**6,0,-1)]
    print("\tmedium\t")
    del t2_2
    t2_3 = [ i for i in range(10**9,0,-1)]
    print("\thard\t")
    del t2_3
def t3():
    d = {}
    print("Testing 3 : unsorted array")
    t3_1 = [random.randint(0,10**7) for i in range(10**2)]
    print("\teasy\t")
    d['easy'] = single_timeit(t3_1)
    del t3_1
    t3_2 = [random.randint(0,10**7) for i in range(10**3)]
    print("\tmedium\t")
    d['medium'] = single_timeit(t3_2)
    del t3_2
    t3_3 = [random.randint(0,10**7) for i in range(10**4)]
    print("\thard\t")
    d['hard'] = single_timeit(t3_3)
    del t3_3
    t3_4 = [random.randint(0,10**7) for i in range(10**5)]
    print("\tultimate\t")
    d['ultimate'] = single_timeit(t3_4)
    del t3_4
    print_stats(d)
    great_sort(d)
    # print(d)
def t4():
    print("Testing 4 : Range Minimum array")
    t4_1 = [random.randint(0,10**7) for i in range(10**1)]
    print("\teasy\t")
    del t4_1
    t4_2 = [random.randint(0,10**7) for i in range(10**2)]
    print("\tmedium\t")
    del t4_2
    t4_3 = [random.randint(0,10**7) for i in range(10**3)]
    print("\thard\t")
    del t4_3

def print_stats(d):
    print(f'{"Sorting Algo":>15}',end='')
    for k in d['easy']:
        print(f'{k:>15}',end='')
    for k in d:
        print()
        print(f'{k:>15}',end='')
        for k2 in d[k]:
            print(f'{d[k][k2]:>15}',end='')

def great_sort(d:dict):
    import collections
    l = list(d.keys())[-1]
    d1 = d[l]
    # od = collections.OrderedDict(sorted(d1.items()))
    od = {k: v for k, v in sorted(d1.items(), key=lambda item: item[1])}
    # for k, v in od.items(): print(k, v , end =' > ')
    print('\n\n')
    for k, v in od.items(): print(k, end =' > ')
    print('\n\n')

if __name__ == '__main__':
    main()
    benchmark()

    # OUTPUT
    '''

Almost All Sorting Algos i Know
 *************************

O(n^2) Sorting Algos...
------------------------------
SELECTION OK
INSERTION OK
BUBBLE OK

QUICK OK

O(n*log(n)) Sorting Algos...
------------------------------
MERGE OK
HEAP OK

Less than O(n*log(n)) Sorting Algos... (Special Cases only)
------------------------------
Counting Sort OK
Testing 3 : unsorted array
        easy
[+] selectionSort
[+] insertionSort
[+] bubbleSort
[+] quickSort
[+] mergeSort
[+] heapSort
[+] countingSort
        medium
[+] selectionSort
[+] insertionSort
[+] bubbleSort
[+] quickSort
[+] mergeSort
[+] heapSort
[+] countingSort
        hard
[+] selectionSort
[+] insertionSort
[+] bubbleSort
[+] quickSort
[+] mergeSort
[+] heapSort
[+] countingSort
        ultimate
[+] selectionSort
[+] insertionSort
[+] bubbleSort
[+] quickSort
[+] mergeSort
[+] heapSort
[+] countingSort
   Sorting Algo  selectionSort  insertionSort     bubbleSort      quickSort      mergeSort       heapSort   countingSort
           easy              0              0         997200              0        1000500              0     1623692700
         medium       31907400       35937200       78731300        2029100        2958300         997400     1652584600
           hard     3077776600     3338649600     6502653400       19914500       31914600        3988200     1600772400
       ultimate   299701897800   302069763000   639551913100      236404100      317151200       66856400     1569821200


heapSort > quickSort > mergeSort > countingSort > selectionSort > insertionSort > bubbleSort 
    
    
    ''' 