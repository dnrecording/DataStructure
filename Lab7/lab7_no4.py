class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def enQueue(self, data):
        return self.items.append(data)

    def deQueue(self):
        return self.items.pop(0)

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
                else: # data has exist
                    return -1
            return self.root

    def preorder(self, node):
        if node != None:
            print(node, end = " ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node, end = " ")
            self.inorder(node.right)

    def postorder(self, node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node, end = " ")

    def breadth(self, node):
        q = Queue()
        q.enQueue(self.root)
        while not q.isEmpty():
            node= q.deQueue()
            print(node, end = " ")
            if node.left is not None:
                q.enQueue(node.left)
            if node.right is not None:
                q.enQueue(node.right)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)

if __name__ == "__main__":
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        root = T.insert(i)
    # T.printTree(root)
    # print()
    print("Preorder :", end = " ")
    T.preorder(root)
    print()
    print("Inorder :", end = " ")
    T.inorder(root)
    print()
    print("Postorder :", end = " ")
    T.postorder(root)
    print()
    print("Breadth :", end = " ")
    T.breadth(root)

# OUTPUT
# Enter Input : 10 4 20 1 5
# Preorder : 10 4 1 5 20 
# Inorder : 1 4 5 10 20 
# Postorder : 1 5 4 20 10 
# Breadth : 10 4 20 1 5

# Enter Input : 0 -50 50 25 -25 13 -13 28 -38 75 -75 62 -62 100 -100
# Preorder : 0 -50 -75 -100 -62 -25 -38 -13 50 25 13 28 75 62 100 
# Inorder : -100 -75 -62 -50 -38 -25 -13 0 13 25 28 50 62 75 100 
# Postorder : -100 -62 -75 -38 -13 -25 -50 13 28 25 62 100 75 50 0 
# Breadth : 0 -50 50 -75 -25 25 75 -100 -62 -38 -13 13 28 62 100 