import math

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree(object):

    def insert(self, root, key):

        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                        self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def balance(self, root):
        while math.abs(self.getBalance(root)) > 1:
            if (self.getBalance(root)) > 0:
                self.leftRotate(root)
            else:
                self.leftRotate(root)
                self.balance(root.left)
                self.balance(root.right)

    def printTree(self, root: TreeNode): 
        if root is None :
            return None
        def maxDepth(node): 
            if node is None:
                return 0 
            else :
                lDepth = maxDepth(node.left) 
                rDepth = maxDepth(node.right) 
                if (lDepth > rDepth):
                    return lDepth+1 
                else:
                    return rDepth+1
        height = maxDepth(root) - 1
        cols = pow(2, height + 1) - 1
        res = [[" " for _ in range(cols)] for _ in range(height + 1)]
        
        def dfs(node, row, col):
            if node is None : return
            res[int(row)][int(col)] = str(node.val)
            dfs(node.left, row + 1, (col - pow(2,height - row - 1))) 
            dfs(node.right, row + 1, (col + pow(2,height - row - 1)))
            
        dfs(root, 0, (cols - 1)/2) 
        for row in res:
            curr_line = "" 
            for s in row:
                curr_line += s 
            print(curr_line)
        return res


myTree = AVL_Tree()
root = None
 
root = myTree.insert(root, 1)
root = myTree.insert(root, 2)
root = myTree.insert(root, 3)
root = myTree.insert(root, 4)
root = myTree.insert(root, 5)
root = myTree.insert(root, 6)
root = myTree.insert(root, 7)
root = myTree.insert(root, 8)
root = myTree.insert(root, 9)
root = myTree.insert(root, 10)
myTree.printTree(root)