class QueueADT:
    def __init__(self,size=10) -> None:
        self.MAX = size
        self.queue = []
        self.top = 0
        # self.front = 0
        # self.rear = 0

    def enq(self,data):
        if self.top != self.MAX :
            self.queue.append(data)
            self.top +=1
            return self.queue
        return -1
    
    def deq(self):
        if self.top == 0:
            return -1
        self.top -= 1
        return self.queue.pop(0)
    
    def __len__(self):
        return self.top
    
    def __str__(self) -> str:
        s = 'Z |\t'
        for i in self.queue:
            s += str(i) + '\t'
        return s + ' <TOP'

def main():
    S = QueueADT(5)
    print(f'{S.enq(10)=}')
    print(f'{S.enq(20)=}')
    print(f'{S.enq(30)=}')
    print(f'{S.enq(40)=}')
    print(f'{S.enq(50)=}')
    print(f'{S.enq(60)=}')
    print(f'{S.deq()=}')
    print(f'{S.deq()=}')
    print(f'{S.deq()=}')
    print(f'{S.deq()=}')
    print(f'{S.enq(80)=}')
    print(f'{S.enq(90)=}')
    print(f'{len(S)=}')
    print(S)
    print(f'{S.enq(60)=}')
    print(f'{S.deq()=}')
    print(f'{S.deq()=}')
    print(f'{S.deq()=}')
    print(f'{S.deq()=}')
    print(f'{S.deq()=}')
    


if __name__ == '__main__':
    main()
