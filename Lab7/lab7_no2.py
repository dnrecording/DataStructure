class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        cur = self.root
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            while True:
                if data < cur.data: # go left
                    if cur.left is None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left
                elif data > cur.data: # go right
                    if cur.right is None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
                else: # data has exist
                    return -1
            return self.root

    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)

    def findMin(self):
        cur = self.root
        while cur.left:
            cur =  cur.left
        return cur

    def findMax(self):
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
more = inp[0]
less = inp[0]

for i in inp:
    root = T.insert(i)

T.printTree(root)
print("--------------------------------------------------")
print("Min :", T.findMin())
print("Max :", T.findMax())


# OUTPUT
# Enter Input : 10 4 20 1 5
#       20
#  10
#            5
#       4
#            1
# --------------------------------------------------
# Min : 1
# Max : 20

# Enter Input : 4 10 3 6 13 9
#            13
#       10
#                 9
#            6
#  4
#       3
# --------------------------------------------------
# Min : 3
# Max : 13

# Enter Input : 1 2 3 4 5 6 7 9 8 0 -1 -2
#                                     9
#                                          8
#                                7
#                           6
#                      5
#                 4
#            3
#       2
#  1
#       0
#            -1
#                 -2
# --------------------------------------------------
# Min : -2
# Max : 9