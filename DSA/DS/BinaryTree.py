import time

class TreeNode :
    def __init__(self,d = 0,R=None,L=None) -> None:
        self.rc = R
        self.d = d
        self.lc = L


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    # def __init__(self,debug = False) -> None:
    #     if debug:
    #         self.root = TreeNode(30,TreeNode(50,TreeNode(60),TreeNode(40)),TreeNode(10,TreeNode(20),TreeNode(1)))
    #     else:
    #         self.__init__(self)
    
    def insert(self,data):
        if self.root == None:
            self.root = TreeNode(data)
            return
        q = self.root
        while q:
            if q.d < data:
                if q.rc == None:
                    q.rc = TreeNode(data)
                    return
                q = q.rc
            elif q.d > data:
                if q.lc == None:
                    q.lc = TreeNode(data)
                    return
                q = q.lc
            '''Use this to see how many times it checks the tree before inserting '''
            # self.traverse_inorder()
            # time.sleep(1)
    
    def delete(self,target):
        if self.BinarySearch(target) == False:
            return None
        if self.root.d == target:
            temp = self.root.d
            left_max = self.delete(self.max_subtree(self.root.lc))
            if left_max != None:
                self.root.d = left_max
                return temp
            right_min = self.delete(self.min_subtree(self.root.rc))
            self.root.d = right_min
            return temp
        
        q = self.root
        parent = None
        side  = None
        while q:
            if q.d == target:
                # NO Child
                if q.lc == None and q.rc == None:
                    if side == 0:
                        parent.rc = None
                    else:
                        parent.lc = None
                # One left Child
                elif q.lc != None and q.rc == None:
                    if side == 0:
                        parent.rc = q.lc
                    else:
                        parent.lc = q.lc
                # One right Child
                elif q.lc == None and q.rc != None:
                    if side == 0:
                        parent.rc = q.rc
                    else:
                        parent.lc = q.rc
                # two Child
                elif q.lc == None and q.rc == None:
                    deleted = self.delete(self.max_subtree(q.lc))
                    if left_max == None:
                        deleted = self.delete(self.min_subtree(q.rc))
                    if side == 0:
                        parent.rc.d = deleted
                    else:
                        parent.lc.d = deleted
                return q.d
            parent = q
            if q.d < target:
                q = q.rc
                side = 0
            elif q.d > target:
                q = q.lc
                side = 1
            
        return None

    def max_subtree(self,p):
        if p == None:
            return None
        while p.rc:
            p = p.rc
        return p.d

    def min_subtree(self,p):
        if p == None:
            return None
        while p.lc:
            p = p.lc
        return p.d

    def BinarySearch(self,target):
        if target == None:
            return False 
        if self.root == None:
            return False
        q = self.root
        while q:
            if q.d == target:
                return True
            if q.d < target:
                q = q.rc
            elif q.d > target:
                q = q.lc
        return False

    def traverse_inorder(self):
        if self.root == None:
            return None
        print('inorder :',end='')
        self.inorder(self.root)
        print()

    def traverse_preorder(self):
        if self.root == None:
            return None
        print('preorder :',end='')
        self.preorder(self.root)
        print()

    def traverse_postorder(self):
        if self.root == None:
            return None
        print('postorder :',end='')
        self.postorder(self.root)
        print()

    def inorder(self,q):
        if q:
            self.inorder(q.lc)
            print(q.d,end=',')
            self.inorder(q.rc)
        
    
    def preorder(self,q):
        if q:
            print(q.d,end=',')
            self.preorder(q.lc)
            self.preorder(q.rc)

    def postorder(self,q):
        if q:
            self.postorder(q.lc)
            self.postorder(q.rc)
            print(q.d,end=',')
    
    def numberOfNodes(self,p):
        if p == None:
            return 0
        return  1 + self.numberOfNodes(p.rc) + self.numberOfNodes(p.lc)
    
    def height(self,p):
        if p == None:
            return 0
        return  1 + max(self.height(p.rc),self.height(p.lc))

class AVLTree(BinarySearchTree):
    
    def balanceFactor(self,n):
        if n == None:
            return 0
        if n.rc == None and n.lc == None:
            return 0
        return self.height(n.lc) - self.height(n.lc)   

    def insert(self,data):
        if self.root == None:
            self.root = TreeNode(data)
            return
        q = self.root
        while q:
            if q.d < data:
                if q.rc == None:
                    q.rc = TreeNode(data)
                    return
                q = q.rc
            elif q.d > data:
                if q.lc == None:
                    q.lc = TreeNode(data)
                    return
                q = q.lc


        

            
def main():
    # BS = BinarySearchTree(debug=True)
    # BS.traverse_inorder()
    # BS.traverse_preorder()
    # BS.traverse_postorder()
    # print(BS.BinarySearch(25))

    # BS.insert(25)
    # print(BS.BinarySearch(25))
    # BS.traverse_inorder()
    
    """Problem in BST without balancing """
    # BS = BinarySearchTree()
    # for i in range(1,10):
    #     BS.insert(i*100)
    # BS.traverse_inorder()
    # BS.traverse_preorder()
    # BS.traverse_postorder()

    # print(BS.max_subtree(BS.root))
    # print(BS.min_subtree(BS.root))
    # BS.traverse_inorder()    
    # print(BS.delete(34))
    # BS.traverse_inorder()
    # print(BS.delete(1))
    # BS.traverse_inorder()
    # print(BS.delete(60))
    # BS.traverse_inorder()
    # print(BS.delete(30))
    # BS.traverse_inorder()
    # print(BS.delete(10))
    # BS.traverse_inorder()
    # print(BS.delete(20))
    # BS.traverse_inorder()
    # print(BS.delete(25))
    # BS.traverse_inorder()
    # print(BS.delete(40))
    # BS.traverse_inorder()
    # print(BS.delete(50))
    # BS.traverse_inorder()
    AVL = AVLTree()
    AVL.traverse_inorder()
    AVL.insert(20)
    print(AVL.height(AVL.root))
    AVL.traverse_inorder()

if __name__ == '__main__':
    main()
