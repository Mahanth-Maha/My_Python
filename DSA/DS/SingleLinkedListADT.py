class SLLNode:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link
    '''
    def __str__(self) -> str:
        if self.link == None:
            return str(self.data)
        s = str(self.data)
        t = self.link
        while(t != None):
            s += '->' + str(t.data) 
            t = t.link
        return s
    '''


class singleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_node(self, newData, index_at: int = 0):
        if self.head == None:
            self.head = SLLNode(newData)
            return self
        if index_at == 0:
            self.head = SLLNode(newData, self.head)
            return self
        t = self.head
        i = 1
        while(t.link and i < index_at):
            i += 1
            t = t.link
        t.link = SLLNode(newData, t.link)
        return self

    def delete_node(self, index_at: int = 0):
        if self.head == None:
            return None
        if index_at == 0 or index_at == 1:
            temp = self.head
            self.head = self.head.link
            sdata = temp.data
            del temp
            return sdata
        t = self.head
        i = 2
        while(t.link and i != index_at):
            if t.link == None:
                return -1
            t = t.link
            i += 1
        temp = t.link
        if t.link == None:
            t.link = None
        else:
            t.link = t.link.link
        sdata = temp.data
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
        t = t.link
        while(t != None):
            s += '->' + str(t.data)
            t = t.link
        return s

    def __len__(self) -> int:
        if self.head == None:
            return 0
        c = 0
        t = self.head
        while(t != None):
            c += 1
            t = t.link
        return c


def main():
    root = singleLinkedList()
    print("SLL\n")
    root.insert_at_first(10)
    root.insert_at_last(20)
    root.insert_after_index(15, 1)
    root.insert_after_index(17, 2)
    root.insert_at_last(50)
    root.insert_at_first(5)
    root.insert_after_index(30, 5)
    print(root)
    print("Deleted:", root.delete_node(0))
    print(root)
    print("Deleted:", root.delete_node(1))
    print(root)
    print("Deleted:", root.delete_node(len(root)))
    print(root)


if __name__ == '__main__':
    main()
