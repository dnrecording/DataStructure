# Queue Class
class Queue:
    def __init__(self, lst=None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def enQueue(self, i):
        self.items.append(i)  # insert i ที่ท้าย list

    def deQueue(self):
        self.items.pop(0)  # pop out index 0
        # print(self.items[0])

    def isEmpty(self):
        return self.items == []  # return len(self.items) == 0

    def size(self):
        return len(self.items)

####################################################################

# Function
# เพิ่มค่าตามเลข ascii
def encodemsg(q1, q2):
    temp = 0
    length = len(q1.items)
    s = ''
    for i in range(len(q1.items)):
        temp = ord(q1.items[i])
        if temp < 123 and temp > 96:
            temp += q2.items[i]
            if temp >= 123:
                temp -= 26
                s = chr(temp)
                q1.enQueue(s)
                q2.enQueue(q2.items[i])
            else:
                s = chr(temp)
                q1.enQueue(s)
                q2.enQueue(q2.items[i])
        elif temp < 91 and temp > 64:
            temp += q2.items[i]
            if temp >= 91:
                temp -= 26
                s = chr(temp)
                q1.enQueue(s)
                q2.enQueue(q2.items[i])
            else:
                s = chr(temp)
                q1.enQueue(s)
                q2.enQueue(q2.items[i])
    for d in range(length):
        q1.deQueue()
    print('Encode message is : ', q1.items)

# ลดค่าตามเลข ascii
def decodemsg(q1, q2):
    temp = 0
    length = len(q1.items)
    s = ''
    for i in range(len(q1.items)):
        temp = ord(q1.items[i])
        if temp < 123 and temp > 96:
            temp -= q2.items[i]
            if temp <= 96:
                temp += 26
                s = chr(temp)
                q1.enQueue(s)
            else:
                s = chr(temp)
                q1.enQueue(s)
        elif temp < 91 and temp > 64:
            temp -= q2.items[i]
            if temp <= 64:
                temp += 26
                s = chr(temp)
                q1.enQueue(s)
            else:
                s = chr(temp)
                q1.enQueue(s)
    for d in range(length):
        q1.deQueue()
    print('Decode message is : ', q1.items)

####################################################################

# Main
m, n = input('Enter String and Code : ').split(',')
string = []
number = []
for i in m:
    if i != ' ':
        string.append(i)
for j in n:
    number.append(int(j))

q1 = Queue(string)
q2 = Queue(number)
encodemsg(q1, q2)
decodemsg(q1, q2)

####################################################################

# OUTPUT
# Enter String and Code : i love Python,256183
# Encode message is :  ['k', 'q', 'u', 'w', 'm', 'S', 'a', 'y', 'n', 'p', 'v']
# Decode message is :  ['i', 'l', 'o', 'v', 'e', 'P', 'y', 't', 'h', 'o', 'n']

# Enter String and Code : KMITL,2
# Encode message is :  ['M', 'O', 'K', 'V', 'N']
# Decode message is :  ['K', 'M', 'I', 'T', 'L']

# Enter String and Code : zzzzzzzzz,123456789
# Encode message is :  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# Decode message is :  ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']

# Enter String and Code : I Love Data Structures But I Hate Bug,999997
# Encode message is :  ['R', 'U', 'x', 'e', 'n', 'K', 'j', 'c', 'j', 'B', 'c', 'y', 'd', 'l', 'c', 'd', 'a', 'l', 'b', 'K', 'd', 'c', 'R', 'O', 'j', 'c', 'n', 'K', 'd', 'n']
# Decode message is :  ['I', 'L', 'o', 'v', 'e', 'D', 'a', 't', 'a', 'S', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 's', 'B', 'u', 't', 'I', 'H', 'a', 't', 'e', 'B', 'u', 'g']

# Enter String and Code : SawaddeeKub,55555
# Encode message is :  ['X', 'f', 'b', 'f', 'i', 'i', 'j', 'j', 'P', 'z', 'g']
# Decode message is :  ['S', 'a', 'w', 'a', 'd', 'd', 'e', 'e', 'K', 'u', 'b']
