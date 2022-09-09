# Done

# 0. LINKED LIST
from SingleLinkedListADT import singleLinkedList
from DoubleLinkedListADT import doubleLinkedList
from CircularLinkedList import CircularLinkedList

# 0.1 STACK
from stack_ARR import StackADT
from stack_SLL import SLL_Stack, StackSLL

# 0.2 QUEUE
from queue_ARR import QueueADT
from queue_SLL import SLL_Queue, QueueSLL

# 1. Tree
#  1.1 BinaryTree
import BinaryTree

#  1.2 BinarySearchTree
from BinaryTree import BinarySearchTree

#  1.3 BalancedBinarySearchTree - AVL
from BinaryTree import AVLTree

#  1.4 K_ary_Tree
from BinaryTree import K_aryTreeNode

# TODO
# 2. Graph
#  2.1 Graph
from Graph import GraphLinkedList, GraphMatrix

#  2.2 BreadthFirstSearch
from Graph import BFS

#  2.3 DepthFirstSearch
from Graph import DFS

# 3. Hashing
#  3.1 DirectAddressTable
#    3.1.1 DirectAddressTable_Chaining
#    3.1.2 DirectAddressTable_OpenAdressing
#        3.1.2.1 DirectAddressTable_OpenAdressing-LinearProbing
#        3.1.2.2 DirectAddressTable_OpenAdressing-QuadraticProbing
#        3.1.2.3 DirectAddressTable_OpenAdressing-DoubleHashing
class hashing(dict) :
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

# 4. SET
#  4.1 DisjointSets
class sets(set):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

# 5. Heap
#  5.1 BinaryHeap-MinHeap
#  5.2 BinaryHeap-MaxHeap

import heapq
