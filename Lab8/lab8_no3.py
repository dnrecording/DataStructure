class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)  

class BST:
    def __init__(self):
        self.root = None

    def insert(self,node, data):

        if(not node):
            return Node(data)

        if(data >= node.data):
            node.right = self.insert(node.right,data)
        else:
            node.left  = self.insert(node.left,data)

        self.updateHeight(node)
        return node
        


    def updateHeight(self,node):
        node.height =  self.getHeight(node.left) + self.getHeight(node.right) + 1

    def getHeight(self,node):
        if(not node):
            return 0
        
        return node.height    
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
  
    def find(self,root,data):
        
        if(not root):
            return 0
        ptr = root
        s   = 0
        while(ptr != None):
            if(data == ptr.data):
                return s + self.getHeight(ptr.left) + 1
            if(data > ptr.data): # go right
                if(not ptr.right):
                    return s + self.getHeight(ptr.left) + 1
                s  += self.getHeight(ptr.left) + 1
                ptr = ptr.right
                

            if(data < ptr.data): # go left
                if(ptr.left != None and data <= ptr.left.data):
                    ptr = ptr.left
                else:
                    if(ptr.left == None):
                        return  s
                    elif(data > ptr.left.data):
                        return  self.getHeight(ptr) - self.getHeight(ptr.left) - 1
            
                        
        return s
         


T = BST()

raw = input('Enter Input : ').split("/")

[inp,val] = raw
val = int(val)
inp = [int(i) for i in inp.split()]
root = None
for i in inp:
    root = T.insert(root,i)

T.printTree(root)
print("--------------------------------------------------")
print("Rank of",val,":",T.find(root,val))

# OUTPUT
# Enter Input : 1 2 5 4 3 -2/4
#            5
#                 4
#                      3
#       2
#  1
#       -2
# --------------------------------------------------
# Rank of 4 : 5

# Enter Input : 7 4 3 1 2 6 9 12 5 11/10
#            12
#                 11
#       9
#  7
#            6
#                 5
#       4
#            3
#                      2
#                 1
# --------------------------------------------------
# Rank of 10 : 8

# Enter Input : 7 4 2 1 9 8 11/5
#            11
#       9
#            8
#  7
#       4
#            2
#                 1
# --------------------------------------------------
# Rank of 5 : 3

# Enter Input : 1 2 4 9 8 5 3/0
#                 9
#                      8
#                           5
#            4
#                 3
#       2
#  1
# --------------------------------------------------
# Rank of 0 : 0

# Enter Input : 1 2 4 9 8 5 3/10
#                 9
#                      8
#                           5
#            4
#                 3
#       2
#  1
# --------------------------------------------------
# Rank of 10 : 7
