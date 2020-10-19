class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, data):
        return self.items.append(data)

    def pop(self):
        return self.items.pop(-1)

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

    def preorder(self, node):
        if node != None:
            print(node, end = "")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node != None:
            if node.left != None and node.right != None:
                print("(", end = "")
            self.inorder(node.left)
            print(node, end = "")
            self.inorder(node.right)
            if node.left != None and node.right != None:
                print(")", end = "")

    def postorder(self, node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node, end = " ")

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)

if __name__ == "__main__":
    operator = "+-*/^"
    T = BST()
    S = Stack()
    inp = input("Enter Postfix : ")
    for i in inp:
        if i in operator:
            rightpos = S.pop()
            leftpos = S.pop()
            newNode = Node(i, leftpos, rightpos)
            S.push(newNode)
        else:
            S.push(Node(i))
    T.root = S.pop()
    print("Tree :")
    T.printTree(T.root)
    print("--------------------------------------------------")
    print("Infix :", end = " ")
    T.inorder(T.root)
    print()
    print("Prefix :", end = " ")
    T.preorder(T.root)

# OUTPUT
# Enter Postfix : ab+cde+**
# Tree :
#                 e
#            +
#                 d
#       *
#            c
#  *
#            b
#       +
#            a
# --------------------------------------------------
# Infix : ((a+b)*(c*(d+e)))
# Prefix : *+ab*c+de