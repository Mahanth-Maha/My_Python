from SingleLinkedListADT import singleLinkedList, SLLNode


class StackSLL(singleLinkedList):
    def __init__(self) -> None:
        super().__init__()

    ''' Implementation Using LIFO # I mean from first '''

    def push(self, sdata):
        self.insert_at_first(sdata)

    def pop(self):
        ret = self.delete_at_first()
        if ret == None:
            return -1
        return ret

    ''' Implementation Using FILO # I mean the other way from last onlr worst case impl
    def push(self,sdata):
        self.insert_at_last(sdata)
    
    def pop(self):
        return self.delete_at_last()
    '''


class SLL_Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, ndata) -> None:
        self.head = SLLNode(ndata, self.head)

    def pop(self) -> int:
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
    s = StackSLL()
    s.push(20)
    s.push(30)
    s.push(40)
    print(s)
    print(s.pop())
    print(s)
    print(s.pop())
    print(s.pop())
    print(s.pop())

    s = SLL_Stack()
    s.push(20)
    s.push(30)
    s.push(40)
    print(s)
    print(s.pop())
    print(s)
    print(s.pop())
    print(s.pop())
    print(s.pop())


if __name__ == '__main__':
    main()
