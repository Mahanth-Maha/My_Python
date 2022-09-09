""" implementation of heaps : (from : https://docs.python.org/3/library/heapq.html)
import heapq        

To create a heap, use a list initialized to [], or you can transform a populated list into a heap via function heapify().

> heapq.heappush(heap, item)
        Push the value item onto the heap, maintaining the heap invariant.
> heapq.heappop(heap)
        Pop and return the smallest item from the heap, maintaining the heap invariant. 
        If the heap is empty, IndexError is raised. 
        To access the smallest item without popping it, use heap[0].
> heapq.heappushpop(heap, item)
        Push item on the heap, then pop and return the smallest item from the heap. 
        The combined action runs more efficiently than heappush() followed by a separate call to heappop().

> heapq.heapify(x)
        Transform list x into a heap, in-place, in linear time.

> heapq.heapreplace(heap, item)
        Pop and return the smallest item from the heap, and also push the new item. 
        The heap size doesn’t change. If the heap is empty, IndexError is raised.

The module also offers three general purpose functions based on heaps.
* heapq.merge(*iterables, key=None, reverse=False)
* heapq.nlargest(n, iterable, key=None)
* heapq.nsmallest(n, iterable, key=None)

"""


import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


def main():
    l = [3,4,2,6,1,7,9]
    p = []
    for i in l:
        heapq.heappush(p,i)
    heapq.heapify(l)
    minheap = l.copy()
    heapq._heapify_max(l)
    maxheap = l.copy()
    print(f'{minheap=}\n{maxheap=}')
    print('min heap : ', p)
    print(f'extract min : {heapq.heappop(p)}\t\t-> heap = {p}')
    print(f'extract min : {heapq.heappop(p)}\t\t-> heap = {p}')
    print(f'extract min : {heapq.heappop(p)}\t\t-> heap = {p}')
    print(f'increase key : {heapq.heappushpop(p,8)}\t-> heap = {p}')

if __name__ == '__main__':
    main()