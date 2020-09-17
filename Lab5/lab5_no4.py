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
    
    def isEmpty(self):
        return self.head == None

    def sizes(self):
        return self.size

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

    def add_before(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.size += 1
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.size += 1

    def insert(self, index, data):
        if 0 < index < self.size:
            pre = self.head
            for i in range(index-1):
                pre = pre.next
            aft = pre.next
            newNode = Node(data)
            newNode.next = aft
            aft.prev = newNode
            pre.next = newNode
            newNode.prev = pre
            self.size += 1 
        elif index == self.size:
            self.append(data)
        elif index == 0:
            self.add_before(data)

    def delhead(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

    def deltail(self):
        if self.head is None:
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1

    def delindex(self, index):
        pre = self.head
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.delhead()
        elif index == self.size:
            self.deltail()
        else:
            for i in range(index-1):
                pre = pre.next
            pre.next = pre.next.next
            # delnode = pre.next
            # aft = delnode.next
            # pre.next = aft
            # aft.prev = pre
            self.size -= 1

    def index(self, data):
        current = self.head
        i = 0
        while current:
            if current.data == data:
                return i 
            i += 1
            current = current.next
        else:
            return -1

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return self.index(data)
            current = current.next
        else:
            return -1
        
ls = Doubly()
n = input("Enter Input : ").split(",")
for i in n:
    if i.startswith("I"):
        if ls.isEmpty():
            ls.append(i[2:])
            ls.append("|")
        else:
            index = ls.search("|")
            ls.insert(index, i[2:])
    elif i.startswith("L"):
        index1 = ls.search("|")
        if ls.isEmpty():
            pass
        elif index1 > 0:
            ls.delindex(index1)
            ls.insert(index1-1, "|")
        else:
            pass
    elif i.startswith("R"):
        index2 = ls.search("|")
        if ls.isEmpty():
            pass
        elif index2 < ls.size:
            ls.delindex(index2)
            ls.insert(index2+1, "|")
        else:
            pass
    elif i.startswith("B"):
        if ls.isEmpty():
            pass
        else:
            index3 = ls.search("|")
            ls.delindex(index3-1)
    elif i.startswith("D"):
        if ls.isEmpty():
            pass
        else:
            index4 = ls.search("|")
            ls.delindex(index4+1)
print(ls)

# OUTPUT

# Enter Input : I Apple,I Bird,I Cat
# Apple Bird Cat | 

# Enter Input : I Apple,I Bird,I Cat,L
# Apple Bird | Cat 

# Enter Input : I Apple,I Bird,I Cat,L,L
# Apple | Bird Cat 

# Enter Input : I Apple,I Bird,I Cat,L,L,L,L,L
# | Apple Bird Cat 

# Enter Input : I Apple,I Bird,I Cat,L,L,R
# Apple Bird | Cat 

# Enter Input : I Apple,I Bird,I Cat,L,L,R,B
# Apple | Cat 

# Enter Input : I Apple,I Bird,L,L,R,D,D
# Apple | 

# Enter Input : I I,I KMITL,L,L,R,I Love
# I Love | KMITL 

# Enter Input : I I,I KMITL,L,L,R,I Love,D,I DataStructure,L,L,R,L,R,B,I Hate
# I Hate | DataStructure 

