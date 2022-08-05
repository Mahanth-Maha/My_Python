import time


class TreeNode:
    def __init__(self, d=0, R=None, L=None) -> None:
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

    def insert(self, data):
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

    def delete(self, target):
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
        side = None
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

    def max_subtree(self, p):
        if p == None:
            return None
        while p.rc:
            p = p.rc
        return p.d

    def min_subtree(self, p):
        if p == None:
            return None
        while p.lc:
            p = p.lc
        return p.d

    def BinarySearch(self, target):
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
        print('inorder :', end='')
        self.inorder(self.root)
        print()

    def traverse_preorder(self):
        if self.root == None:
            return None
        print('preorder :', end='')
        self.preorder(self.root)
        print()

    def traverse_postorder(self):
        if self.root == None:
            return None
        print('postorder :', end='')
        self.postorder(self.root)
        print()

    def inorder(self, q):
        if q:
            self.inorder(q.lc)
            print(q.d, end=',')
            self.inorder(q.rc)

    def preorder(self, q):
        if q:
            print(q.d, end=',')
            self.preorder(q.lc)
            self.preorder(q.rc)

    def postorder(self, q):
        if q:
            self.postorder(q.lc)
            self.postorder(q.rc)
            print(q.d, end=',')

    def numberOfNodes(self, p):
        if p == None:
            return 0
        return 1 + self.numberOfNodes(p.rc) + self.numberOfNodes(p.lc)

    def height(self, p):
        if p == None:
            return 0
        return 1 + max(self.height(p.rc), self.height(p.lc))


class AVLTree(BinarySearchTree):

    def balanceFactor(self, n):
        if n == None:
            return 0
        if n.rc == None and n.lc == None:
            return 0
        return self.height(n.rc) - self.height(n.lc)

    def insert(self, data):
        if self.root == None:
            self.root = TreeNode(data)
            return
        q = self.root
        stack = [self.root]
        while q:
            if q.d < data:
                if q.rc == None:
                    q.rc = TreeNode(data)
                    stack.append(q.rc)
                    break
                q = q.rc
            elif q.d > data:
                if q.lc == None:
                    q.lc = TreeNode(data)
                    stack.append(q.lc)
                    break
                q = q.lc
            stack.append(q)
        if len(stack) in (0, 1):
            return
        s2 = []
        for _ in range(1, len(stack)+1):
            w = self.balanceFactor(stack[-_])
            if w in (1, 0, -1):
                s2.append((stack[-_], w))
            else:
                s2.append((stack[-_], w))
                break
        if s2[-1][1] in (1, 0, -1):
            return
        n1 = s2[-1][0]
        n2 = s2[-2][0]
        n3 = s2[-3][0]
        rt = False
        if stack[0] == n1:
            parent = self.root
            rt = True
        else:
            parent = stack[-(_+1)]
        if parent == n1:
            parent_side = None
        elif parent.rc == n1:
            parent_side = 'R'
        elif parent.lc == n1:
            parent_side = 'L'

        rot = ''
        if n1.rc == n2:
            rot += 'R'
        elif n1.lc == n2:
            rot += 'L'
        if n2.rc == n3:
            rot += 'R'
        elif n2.lc == n3:
            rot += 'L'
        if rot[0] == rot[1] and rot[0] == 'R':
            # balance RR
            if rt == False:
                parent, n1, n2 = self.__RR(parent, n1, n2, parent_side)
            else:
                self.root, n1, n2 = self.__RR(parent, n1, n2, parent_side)
            return
        elif rot[0] == rot[1] and rot[0] == 'L':
            # balance LL
            if rt == False:
                parent, n1, n2 = self.__LL(parent, n1, n2, parent_side)
            else:
                self.root, n1, n2 = self.__LL(parent, n1, n2, parent_side)
            return
        elif rot[0] == 'L' and rot[1] == 'R':
            # balance LR
            n1, n2, n3 = self.__LR(n1, n2, n3)
            if rt == False:
                parent, n1, n2 = self.__LL(parent, n1, n2, parent_side)
            else:
                self.root, n1, n2 = self.__LL(parent, n1, n2, parent_side)
            return
        elif rot[0] == 'R' and rot[1] == 'L':
            # balance RL
            n1, n2, n3 = self.__RL(n1, n2, n3)
            if rt == False:
                parent, n1, n2 = self.__RR(parent, n1, n2, parent_side)
            else:
                self.root, n1, n2 = self.__RR(parent, n1, n2, parent_side)
            return

    def __RR(self, parent, n1, n2, parent_side):
        if parent_side == None:
            self.root = n2
            n1.rc = n2.lc
            n2.lc = n1
            return self.root, n1, n2
        if parent_side == 'L':
            parent.lc = n2
        else:
            parent.rc = n2
        n1.rc = n2.lc
        n2.lc = n1
        return parent, n1, n2

    def __LL(self, parent, n1, n2, parent_side):
        if self.root == n1:
            self.root = n2
            n1.lc = n2.rc
            n2.rc = n1
            return self.root, n1, n2
        if parent_side == 'L':
            parent.lc = n2
        else:
            parent.rc = n2
        n1.lc = n2.rc
        n2.rc = n1
        return parent, n1, n2

    def __LR(self, n1, n2, n3):
        n2.rc = n2.rc.lc
        n1.lc = n3
        n3.lc = n2
        return n1, n3, n2

    def __RL(self, n1, n2, n3):
        n1.rc = n3
        n2.lc = n3.rc
        n3.rc = n2
        return n1, n3, n2

class K_aryTreeNode:
    def __init__(self, d=0 ,k = 2,pointers = None) -> None:
        self.d = d
        self.k = k
        self.pointers = [ None for _ in self.k ]
        for i in range(len(pointers)):
            self.pointers[i] = pointers[i]


def main_BS():
    """ Helo """
    # BS = BinarySearchTree(debug=True)
    # BS.traverse_inorder()
    # BS.traverse_preorder()
    # BS.traverse_postorder()
    # print(BS.BinarySearch(25))

    # BS.insert(25)
    # print(BS.BinarySearch(25))
    # BS.traverse_inorder()

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


def main():
    AVL = AVLTree()
    ins = [21, 26, 30, 9, 4, 14, 28, 18, 15, 10, 2, 3, 7]
    ins2 = [50, 20, 60, 10, 8, 15, 32, 46, 11, 48]
    for i in ins:
        print(f'\n{i=}\n')
        AVL.insert(i)
        AVL.traverse_preorder()
        AVL.traverse_inorder()
        AVL.traverse_postorder()
    AVL = AVLTree()
    print(f'\nNEW AVL with INPUT = {ins}\n')
    for i in ins:
        AVL.insert(i)
    AVL.traverse_preorder()
    AVL.traverse_inorder()
    AVL.traverse_postorder()


if __name__ == '__main__':
    main()
