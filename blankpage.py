class DummyDoublyCircular:
    class Node:
        def __init__(self, value = None, prev = None, next = None):
            self.data = value
            self.prev = prev
            self.next = next

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head = self.Node()
        self.head.prev = self.head.next = self.head
        self.size = 0

    def __str__(self):
        s = str(self.head.next.data)
        cur = self.head.next
        while cur.next != self.head:
            s += ' ' + str(cur.next.data)
            cur = cur.next
        return s

    def __len__(self):
        return self.size
    
    def reverse(self):
        cur = self.head
        for i in range(len(self) + 1):
            cur.next, cur.prev = cur.prev, cur.next
            cur = cur.prev

    def nodeAt(self, index):
        cur = self.head
        for i in range(-1 , index):
            cur = cur.next
        return cur

    def insert(self, index, value):
        nodeAfter = self.nodeAt(index)
        nodeBefore = nodeAfter.prev
        newNode = self.Node(value, nodeBefore, nodeAfter)
        nodeBefore.next = nodeAfter.prev = newNode
        self.size += 1

    def append(self, value):
        self.insert(len(self), value)

    def indexOf(self, value):
        cur = self.head.next
        for i in range(len(self)):
            if cur.data == value:
                return i
            cur = cur.next
        return -1

    def remove(self, value):
        cur = self.head.next
        for i in range(len(self)):
            if cur.data == value:
                self.removeNode(cur)
                cur = cur.next

    def removeAll(self, value):
        cur = self.head.next
        for i in range(len(self)):
            if cur.data == value:
                self.removeNode(cur)
                continue
            cur = cur.next

    def pop(self, index = -1):
        if index < 0:
            index += self.size
        return self.removeNode(self.nodeAt(index))

    def removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1
        return node.data


class Queue:
    def __init__(self, li = None):
        if li == None:
            self.items = DummyDoublyCircular()
        else:
            self.items = li
    
    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def enQueue(self, value):
        self.items.append(value)

    def deQueue(self):
        return self.items.pop()
        
    def peek(self):
        return self.items.nodeAt(0).data

def get_digit(num, _round):
    for i in range(_round):
        num //= 10
    return num % 10

def get_max_digit(queue):
    max_digit = 0
    for i in range(len(queue)):
        max_digit = len(str(queue.peek())) if max_digit < len(str(queue.peek())) else max_digit
        queue.enQueue(queue.deQueue())
    return max_digit

def radix_sort(queue):
    num_digit = [Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue()]

    for i in range(get_max_digit(queue)):
        while len(queue) != 0:
            t = queue.deQueue()
            num = get_digit(t, i)
            num_digit[num].enQueue(t)
        for j in num_digit:
            while len(j) != 0:
                queue.enQueue(j.deQueue())

s  = Queue()
for i in input('Enter : ').split(', '):
    s.enQueue(int(i))
print(s)
radix_sort(s)
print(s)