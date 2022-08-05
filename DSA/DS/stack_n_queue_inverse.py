from stack_ARR import StackADT
from queue_ARR import QueueADT


class Stack_using_Queue:
    def __init__(self, max=10) -> None:
        self.Q1 = QueueADT(10)
        self.Q2 = QueueADT(10)

    def mpush(self):
        pass

    def mpop(self):
        pass


class Queue_using_Stack:
    def __init__(self, max=10) -> None:
        self.S1 = StackADT(10)
        self.S2 = StackADT(10)

    def menq(self):
        pass

    def mdeq(self):
        pass
