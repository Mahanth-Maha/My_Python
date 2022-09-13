# Basic

basically, any Algorithm requires a Data Structure most probably which performs a Search or a Sort or both 

## Search

### Linear

* Time  - O(n)
* Space - O(1) 
* inplace

### Binary
"Required to be sorted already -> best known O(n<sup>2</sup>)"
* Time  - O(log<sub>2</sub>n)
* Space - O(1) 
* inplace

## Sort

### selectionSort 

* Time  - O(n<sup>2</sup>)
* Space - O(1) 
* inplace
* Stable - YES

### insertionSort

* Time  - O(n<sup>2</sup>)
* Space - O(1) 
* inplace
* Stable - YES

### bubbleSort

* Time  - O(n<sup>2</sup>)
* Space - O(1) 
* inplace
* Stable - YES

### quickSort

* Time  - O(n^2^)
* Space - O(1) 
* inplace
* Stable - NO

### mergeSort

* Time  - O(n log<sub>2</sub>n)
* Space - O(n) 
* outplace
* Stable - YES

### heapSort

* Time  - O(n log<sub>2</sub>n)
* Space - O(1) 
* outplace
* Stable - NO

### countingSort
//dependent on Range
* Time  - O(n)     
* Space - O(Range) 
* inplace ( -consider stable sort)
* Stable - YES 

### timSort
'A combination of Insertion sort on small parts and merge sort to get result'

* Time  - O(n log<sub>2</sub>n)
* Space - O(n) 
* outplace
* Stable - YES


## TIME ANALYSIS - benchmarking of sorts 

Sorting Algo's fastest : [Testesd on unsorted array of size 10<sup>5</sup> of numbers in range(10<sup>7</sup>) ]

1. heapSort > 
2. quickSort > 
3. mergeSort > 
4. countingSort > 
5. selectionSort > 
6. insertionSort > 
7. bubbleSort