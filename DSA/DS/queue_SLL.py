from SingleLinkedListADT import singleLinkedList, SLLNode


class QueueSLL(singleLinkedList):
    def __init__(self) -> None:
        super().__init__()

    ''' Implementation Using FIFO '''

    def enqueue(self, sdata):
        self.insert_at_first(sdata)

    def dequeue(self):
        ret = self.delete_at_last()
        if ret == None:
            return -1
        return ret

    ''' Implementation Using LILO # The other way
    def enqueue(self,sdata):
        self.insert_at_first(sdata)
    
    def dequeue(self):
        returnF self.delete_at_last()
    '''


class SLL_Queue:
    def __init__(self) -> None:
        self.head = None
        self.end = None

    def enqueue(self, ndata) -> None:
        if self.head == None:
            self.head = SLLNode(ndata, self.head)
            self.end = self.head
            return self
        self.end.link = SLLNode(ndata)
        self.end = self.end.link

    def dequeue(self) -> int:
        if self.head == None:
            return -1
        r = self.head
        d = self.head.data
        self.head = self.head.link
        del r
        return d

    def __str__(self) -> str:
        if self.head == None:
            return str("-No Nodes-")
        t = self.head
        s = str(t.data)
        t = t.link
        while(t != None):
            s += '->' + str(t.data)
            t = t.link
        return s


def main():
    s = QueueSLL()
    s.enqueue(20)
    s.enqueue(30)
    s.enqueue(40)
    print(s)
    print(s.dequeue())
    print(s)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print('-'*20)
    s = SLL_Queue()
    s.enqueue(20)
    s.enqueue(30)
    s.enqueue(40)
    print(s)
    print(s.dequeue())
    print(s)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())


if __name__ == '__main__':
    main()
