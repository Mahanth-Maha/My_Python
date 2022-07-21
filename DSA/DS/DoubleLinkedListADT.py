class DLLNode:
    def __init__(self,data=None, next=None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    '''
    def __str__(self) -> str:
        if self.next == None:
            return str(self.data)
        s = str(self.data)
        t = self.next
        while(t != None):
            s += '->' + str(t.data) 
            t = t.next
        return s
    '''

class doubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_node(self, newData, index_at: int = 0):
        if self.head == None:
            self.head = DLLNode(newData)
            return self
        if index_at == 0: 
            self.head.prev = DLLNode(newData,self.head)
            self.head = self.head.prev
            return self
        t = self.head
        i = 1
        while(t.next and i < index_at):
            i += 1
            t = t.next
        if t.next == None:
            t.next = DLLNode(newData, t.next, t)
        else:
            t.next = DLLNode(newData, t.next, t)
            t.next.next.prev = t.next
        return self

    def delete_node(self, index_at: int = 0):
        if self.head == None:
            return None
        if index_at == 0 or index_at == 1:
            d = self.head.data
            t = self.head
            if self.head.next != None:
                self.head = self.head.next
                self.head.prev.next = None
                self.head.prev = None
            del t
            return d
        t = self.head
        i = 2
        while(t.next and i != index_at):
            if t.next == None:
                return -1
            t = t.next
            i += 1
        temp = t.next
        if t.next == None:
            t.next = None
        else:
            t.next = t.next.next
            if t.next != None:
                t.next.prev = t
        sdata = temp.data
        temp.prev = None
        del temp
        return sdata

    def insert_at_first(self, newData):
        self.insert_node(newData, 0)

    def insert_after_index(self, newData, index_at: int):
        self.insert_node(newData, index_at)

    def insert_at_last(self, newData):
        self.insert_node(newData, len(self))

    def delete_at_first(self):
        return self.delete_node(0)

    def delete_at_index(self, i: int):
        return self.delete_node(i)

    def delete_at_last(self):
        return self.delete_node(len(self))

    def __str__(self) -> str:
        if self.head == None:
            return str("-No Nodes-")
        t = self.head
        s = str(t.data)
        t = t.next
        while(t != None):
            s += '->' + str(t.data)
            t = t.next
        return s

    def __len__(self) -> int:
        if self.head == None:
            return 0
        c = 0
        t = self.head
        while(t != None):
            c += 1
            t = t.next
        return c
    
    def rev_str(self) -> str:
        if self.head == None:
            return str("-No Nodes-")
        t = self.head
        # s = str(t.data)
        s = '\nForward :'
        while(t.next != None):
            s += '->' + str(t.data)
            t = t.next
        s += '->' + str(t.data)
        s += '\nBackward :'
        s += '<-' + str(t.data) 
        t = t.prev
        while(t != None):
            s += '<-' + str(t.data)
            t = t.prev
        return s

def main():
    root = doubleLinkedList()
    '''
    root.insert_node(10)
    root.insert_node(20)
    root.insert_node(30)
    root.insert_node(40)
    root.insert_node(50)
    root.insert_node(60)
    root.insert_node(25,4)
    print(len(root))
    print(root.rev_str())
    print("Deleted:", root.delete_node(0))
    print(root.rev_str())
    print("Deleted:", root.delete_node(4))
    print(root.rev_str())
    print("Deleted:", root.delete_node(len(root)))
    print(root.rev_str())
    '''
    root.insert_at_first(10)
    print(root.rev_str())
    root.insert_at_last(20)
    print(root.rev_str())
    root.insert_after_index(15, 1)
    print(root.rev_str())
    root.insert_after_index(17, 2)
    print(root.rev_str())
    root.insert_at_last(50)
    print(root.rev_str())
    root.insert_at_first(5)
    print(root.rev_str())
    root.insert_after_index(30, 5)
    print(root.rev_str())
    print("Deleted:", root.delete_at_first())
    print(root.rev_str())
    print("Deleted:", root.delete_at_index(1))
    print(root.rev_str())
    print("Deleted:", root.delete_at_last())
    print(root.rev_str())

if __name__ == '__main__':
    main()
