class StackADT:
    def __init__(self,size=10) -> None:
        self.MAX = size
        self.stack = []
        self.top = 0

    def mpush(self,data):
        if self.top != self.MAX :
            self.stack.append(data)
            self.top +=1
            return self.stack
        return -1
    
    def mpop(self):
        if self.top == 0:
            return -1
        self.top -=1
        return self.stack.pop()
    
    def __len__(self):
        return self.top
    
    def __str__(self) -> str:
        s = 'Z |\t'
        for i in self.stack:
            s += str(i) + '\t'
        return s + ' <TOP'


def main():
    S = StackADT(5)
    print(f'{S.mpush(10)=}')
    print(f'{S.mpush(20)=}')
    print(f'{S.mpush(30)=}')
    print(f'{S.mpush(40)=}')
    print(f'{S.mpush(50)=}')
    print(f'{S.mpush(60)=}')
    print(f'{S.mpop()=}')
    print(f'{S.mpop()=}')
    print(f'{S.mpop()=}')
    print(f'{S.mpop()=}')
    print(f'{S.mpush(40)=}')
    print(f'{S.mpush(50)=}')
    print(f'{len(S)=}')
    print(S)
    print(f'{S.mpush(60)=}')
    print(f'{S.mpop()=}')
    print(f'{S.mpop()=}')
    print(f'{S.mpop()=}')
    print(f'{S.mpop()=}')
    print(f'{S.mpop()=}')
    


if __name__ == '__main__':
    main()
