root = None
class block:
    def __init__(self,start,end,type,next,pre):
        self.nextBlock = next
        self.preBlock = pre
        self.start = start
        self.end = end
        self.size = self.end - self.start
        if type == 1:
            self.type = 'allocated'
        else:
            self.type = 'free'
    def check(self):
        if self.size == 0:
            self.preBlock.nextBlock , self.nextBlock.preBlock = self.nextBlock, self.preBlock

    def allocate(self,s):
        new_block = block(self.start,self.start+s,1,self,self.preBlock)
        self.preBlock = new_block
        self.start = new_block.start
        self.size = self.end - self.start
        self.check()
    def allocate2(self,s,st):
        freefirst = block(self.start,self.start+st,0,self,self.preBlock)
        self.preBlock = freefirst
        self.start = freefirst.start
        self.size = self.end - self.start
        self.allocate(s)
        self.check()
def display(root):
    t = root
    print('start:', t.start, 'memory : ', t.type, 'end', t.end)
    while(t.nextBlock != None):
        print('start:',t.start,'memory : ',t.type,'end',t.end)
        t = t.nextBlock
def preAllocate(root,pre):
    for i in pre:
        root.allocate2(pre[i],i)

def main():
    root = block(0,500,0,None,None)
    preProcess = {30:25,100:57,160:60,250:143,420:40}
    preAllocate(root,preProcess)
    display(root)

if __name__ == '__main__':
    main()



