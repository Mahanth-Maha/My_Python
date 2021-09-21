def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                break
    print(" Proc No.\tProc Size\tBlock no.")
    for i in range(n):
        print(" ", i + 1, "\t\t", processSize[i], end="\t\t")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

def worstFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        j = blockSize.index(max(blockSize))
        if blockSize[j] >= processSize[i]:
            allocation[i] = j
            blockSize[j] -= processSize[i]
    print(" Proc No. Proc Size   Block no.")
    for i in range(n):
        print(" ", i + 1, "\t\t", processSize[i], end="\t\t")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        temp = []
        for t in blockSize:
            temp.append(t)
        c = processSize[i]
        temp.append(c)
        temp.sort()
        print(temp)
        if temp.index(c) != len(temp):
            if temp[0] == c:
                if temp[1] == c :
                    j = blockSize.index(c)
                    allocation[i] = j
                    blockSize[j] -= processSize[i]
            else:
                j = temp.index(c) + 1
                j = blockSize.index(temp[j])
                allocation[i] = j
                blockSize[j] -= processSize[i]
    print(" Proc No. Proc Size   Block no.")
    for i in range(n):
        print(" ", i + 1, "\t\t", processSize[i], end="\t\t")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


if __name__ == '__main__':
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)
    print('Uncomment one of fit')
    #firstFit(blockSize, m, processSize, n)
    #worstFit(blockSize,m,processSize,n)
    #bestFit(blockSize,m,processSize,n)
