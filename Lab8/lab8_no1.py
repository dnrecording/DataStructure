class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        cur = self.root
        if self.root is None:
            self.root = Node(data)
            print("*", end = "")
        else:
            while True:
                if data < cur.data: # go left
                    if cur.left is None:
                        cur.left = Node(data)
                        print("L", end = "")
                        print("*", end  = "")
                        break
                    else:
                        cur = cur.left
                        print("L", end = "")
                elif data >  cur.data: # go right
                    if cur.right is None:
                        cur.right = Node(data)
                        print("R", end = "")
                        print("*", end = "")
                        break
                    else:
                        cur = cur.right
                        print("R", end = "")
                else:
                    break

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)

if __name__ == "__main__":
    tree = BST()
    inp = [int (x) for x in input("Enter Input : ").split()]
    for i in inp:
        tree.insert(i)
        print()


# OUTPUT
# Enter Input : 1 2 5 4 3 -2 -1
# *
# R*
# RR*
# RRL*
# RRLL*
# L*
# LR*

# Enter Input : 48 47 194194 3534 39 20 2014 35289 53
# *
# L*
# R*
# RL*
# LL*
# LLL*
# RLL*
# RLR*
# RLLL*
