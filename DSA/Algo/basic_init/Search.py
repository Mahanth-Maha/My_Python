class mSearch():
    #linear Search
    def linearSearch(itter,item):
        # for i in range(len(itter)):
        #     if itter[i] == item:
        #         return i
        # return None
        return None if item not in itter else itter.index(item)
    
    #Binary Search - itterative
    def BinarySearch(itter,item):
        l = 0
        h = len(itter)-1
        while(l <= h):
            mid = (l+h)//2
            if itter[mid] == item: 
                return mid
            elif itter[mid] > item:
                h = mid - 1
            else:
                l = mid + 1 
        return None 
    
    #Binary Search - Recursive
    def BinarySearchRec(itter,item):
        l = 0
        h = len(itter)-1
        return recbin(itter,item,l,h)
    
def recbin(itter,item,l,h):
    mid = (l+h)//2
    if itter[mid] == item: 
        return mid
    return recbin(itter,item,l,mid - 1) if itter[mid] > item else recbin(itter,item,mid + 1,h)
    
        

def main():
    import random
    l = [ random.randint(0,1000) for i in range(10)]
    r = random.randint(0,9)
    item = l[r]
    # what is the random number generated
    print("LS OK") if r == mSearch.linearSearch(l,item) else print("LS FAIL")
    l.sort()
    print("BS OK") if l.index(item) == mSearch.BinarySearch(l,item) else print("BS FAIL")
    print("BS REC OK") if l.index(item) == mSearch.BinarySearchRec(l,item) else print("BS REC FAIL")
        


if __name__ == '__main__':
    main()