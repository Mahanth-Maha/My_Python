class Q:
    def __init__(self,s):
        self.size = s
        self.ptr = -1
        self.Q = [-1] * s
    def enq (self, d):
        if self.ptr != self.size -1:
            self.ptr += 1
            self.Q[self.ptr] = d
            return 1
        return -1
    def deq(self):
        if self.ptr != -1:
            k = self.Q[0]
            for i in range(self.size - 1):
                self.Q[i] = self.Q[i+1]
            self.Q[self.size - 1] = -1
            self.ptr -=1
            return k
        return -1
    def display(self):
        for i in self.Q:
            print(i,end = '\t')
        print('\n')

def FIFO(seq,l,size):
    buff = [-1]*size
    hit = 0
    fault = 0
    j = 0
    for i in seq:
        if i in buff:
            hit += 1
        else:
            fault +=1
            buff[j] = i
            j = (j+1)%3
    print('PAGE \nfaults :',fault,'\nHit :',hit,'\nmiss rate :',fault/l*100)

def LRU(seq,l,size):
    buff = [-1]*size
    hit = 0
    fault = 0
    j = 0
    for i in seq:
        if i in buff:
            hit += 1
        else:
            fault +=1
            buff[j] = i
        j = (j+1)%3

    print('PAGE \nfaults :',fault,'\nHit :',hit,'\nmiss rate :',fault/l*100)

def LFU(seq,l,size):
    buff = [-1]*size
    hit = 0
    fault = 0
    j = 0
    dic = dict()
    for i in seq:
        dic[i] = 0
    for i in seq:
        print(dic)
        if i in buff:
            hit += 1
            dic[i] +=1
        else:
            fault +=1
            if dic[i] == 0:
                dic[i]+=1
                buff[j] = i
            else:
                w = []
                for a in dic:
                    if dic[a] != 0:
                        w.append(a)

                for a in w:
                    buff[j] = i
    print('PAGE \nfaults :',fault,'\nHit :',hit,'\nmiss rate :',fault/l*100)

def LFU_2(seq,l,size):
    buff = [-1]*size
    hit = 0
    fault = 0
    j = 0
    for i in seq:
        if i in buff:
            hit += 1
        else:
            fault +=1
            buff[j] = i
        j = (j+1)%3

    print('PAGE \nfaults :',fault,'\nHit :',hit,'\nmiss rate :',fault/l*100)

if __name__ == '__main__':
    seq = [4,7,6,1,7,6,1,2,7,2]
    seq2 = [1,2,3,4,2,1,5,3,2,4,6]
    seq3 = [1,2,3,2,4,1,3,2,4,1]
    l = len(seq)
    size = 3
    #print('Uncomment one of PRA')
    FIFO(seq3, l,size)
    LRU(seq3, l,size)
    LFU_2(seq3, l,size)