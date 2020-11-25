class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def insert(self, root, key): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val:
            print("Not Balance, Rebalance!, Right Rotate") 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            print("Not Balance, Rebalance!, Left Rotate") 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val:
            print("Not Balance, Rebalance!, left and then right")  
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val:
            print("Not Balance, Rebalance!, right and then left")  
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root)
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = [int(x) for x in input("Enter Input : ").split()]
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")


# OUTPUT
# Enter Input : 1 2 3 4 5 6 7 8
# insert : 1
#  1
# ===============
# insert : 2
#       2
#  1
# ===============
# insert : 3
# Not Balance, Rebalance!
#       3
#  2
#       1
# ===============
# insert : 4
#            4
#       3
#  2
#       1
# ===============
# insert : 5
# Not Balance, Rebalance!
#            5
#       4
#            3
#  2
#       1
# ===============
# insert : 6
# Not Balance, Rebalance!
#            6
#       5
#  4
#            3
#       2
#            1
# ===============
# insert : 7
# Not Balance, Rebalance!
#            7
#       6
#            5
#  4
#            3
#       2
#            1
# ===============
# insert : 8
#                 8
#            7
#       6
#            5
#  4
#            3
#       2
#            1
# ===============

# Enter Input : 50 40 35 30 20 10 5
# insert : 50
#  50
# ===============
# insert : 40
#  50
#       40
# ===============
# insert : 35
# Not Balance, Rebalance!
#       50
#  40
#       35
# ===============
# insert : 30
#       50
#  40
#       35
#            30
# ===============
# insert : 20
# Not Balance, Rebalance!
#       50
#  40
#            35
#       30
#            20
# ===============
# insert : 10
# Not Balance, Rebalance!
#            50
#       40
#            35
#  30
#       20
#            10
# ===============
# insert : 5
# Not Balance, Rebalance!
#            50
#       40
#            35
#  30
#            20
#       10
#            5
# ===============
