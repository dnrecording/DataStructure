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
    
    def insert(self, data):
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
                else:
                    return -1 # data has exist
            return self.root

    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)



if __name__ == "__main__":
    T1 = BST()
    T2 = BST()
    inp = input("Enter Input : ").split("/")
    k = int(inp[1])
    for i in [int(j) for j in inp[0].split()]:
        root1 = T1.insert(i)
        if i <= k:
            root2 = T2.insert(i)
        else:
            root2 = T2.insert(i*3)
    T1.printTree(root1)
    print("--------------------------------------------------")
    T2.printTree(root2)

# OUTPUT
# Enter Input : 67 102 81 35 15 7 99 196 202 152/90
#                 202
#            196
#                 152
#       102
#                 99
#            81
#  67
#       35
#            15
#                 7
# --------------------------------------------------
#                 606
#            588
#                 456
#       306
#                 297
#            81
#  67
#       35
#            15
#                 7

# Enter Input : 5 3 -1 4 7 6 8/-5
#            8
#       7
#            6
#  5
#            4
#       3
#            -1
# --------------------------------------------------
#            24
#       21
#            18
#  15
#            12
#       9
#            -3

# Enter Input : 5 3 1 4 7 6 8/4
#            8
#       7
#            6
#  5
#            4
#       3
#            1
# --------------------------------------------------
#            24
#       21
#            18
#  15
#            4
#       3
#            1