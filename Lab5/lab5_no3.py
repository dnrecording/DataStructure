class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
    
    def __str__(self):
        s = ""
        current = self.head
        while current.next:
            s += str(current.data) + " "
            current = current.next
        s += str(current.data)
        return s

    def reverse(self):
        s = ""
        current = self.tail
        while current.prev:
            s += str(current.data) + " "
            current = current.prev
        s += str(current.data)
        return s

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.size += 1
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.size += 1

L1 = Doubly()
L2 = Doubly()
l2r = Doubly()
ans = Doubly()

n = input("Enter Input (L1,L2) : ").split()
l1word = n[0].split("->")
l2word = n[1].split("->")

print("L1    :"," ".join(l1word))
print("L2    :"," ".join(l2word))

for i in l1word:
    ans.append(i)

for j in l2word:
    l2r.append(j)

# print(l2r.reverse())
# print(ans)
# for j in l2word:

print("Merge :", ans, l2r.reverse())


# OUTPUT

# Enter Input (L1,L2) : 1 2
# L1    : 1 
# L2    : 2 
# Merge : 1 2 

# Enter Input (L1,L2) : 1->2->3 4->5
# L1    : 1 2 3 
# L2    : 4 5 
# Merge : 1 2 3 5 4 

# Enter Input (L1,L2) : I->Love->KMITL Datastruct->and
# L1    : I Love KMITL 
# L2    : Datastruct and 
# Merge : I Love KMITL and Datastruct 

# Enter Input (L1,L2) : CE->2D Lardkrabang->KMITL
# L1    : CE 2D 
# L2    : Lardkrabang KMITL 
# Merge : CE 2D KMITL Lardkrabang 