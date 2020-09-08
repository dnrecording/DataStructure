class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

r, b = input("Enter Input (Red, Blue) : ").split()

redremain = []
blue = []
blueremain = []

explosion = [0,0]
miss = 0

for i in b:
    if len(blueremain) == 0:
        blueremain.append([i, 1])
    else:
        b_last = blueremain[-1]
        if b_last[0] == i:
            if b_last[1] == 2:
                explosion[1] += 1
                blue.append(i)
                blueremain.append(i)
                for j in range(3):
                    blueremain.pop()
            else:
                blueremain.append([i,2])
        else:
            blueremain.append([i,1])

# print(blueremain)
# print(blue)

for i in r:
    if len(redremain) == 0:
        redremain.insert(0,[i,1])
    else:
        last = redremain[-1]
        if last[0] == i:
            if last[1] == 2 and len(blue) > 0:
                insertbomb = blue[-1]
                if insertbomb == last[0]:
                    miss += 1
                    redremain.append([i,1])
                    redremain.pop()
                    redremain.pop()
                    blue.pop()
                else:
                    redremain.append([insertbomb, 1])
                    redremain.append([i,1])
                    blue.pop()
                continue
            elif last[1] == 2:
                explosion[0] += 1
                redremain.pop()
                redremain.pop()
                continue

            redremain.append([i,2])
        else:
            redremain.append([i,1])
# print(redremain)
# print(blue)

redlst = []
print("Red Team :")
print(len(redremain))
if len(redremain) > 0:
    for i in redremain:
        redlst.append(i[0])
    red = redlst.reverse()
    print("".join(redlst))
else:
    print("Empty")
print(explosion[0],"Explosive(s) ! ! ! (HEAT)")
if(miss):
    print("Blue Team Made (a) Mistake(s)",miss,"Bomb(s)")
print("----------TENETTENET----------")
print(": maeT eulB")
print(len(blueremain))
if(len(blueremain) > 0):
    for i in blueremain:
        print(i[0], end='', sep='')
    print('')
else:
    print("ytpmE")
print("(EZEERF) ! ! ! (s)evisolpxE",explosion[1])

#OUTPUT
# Enter Input (Red, Blue) : AAABBBCDEE HHH
# Red Team :
# 8
# EEDCAHAA
# 1 Explosive(s) ! ! ! (HEAT)
# ----------TENETTENET----------
# : maeT eulB
# 0
# ytpmE
# (EZEERF) ! ! ! (s)evisolpxE 1

# Enter Input (Red, Blue) : AAABBBCDEE FGHHHIOPPP
# Red Team :
# 12
# EEDCBHBBAPAA
# 0 Explosive(s) ! ! ! (HEAT)
# ----------TENETTENET----------
# : maeT eulB
# 4
# FGIO
# (EZEERF) ! ! ! (s)evisolpxE 2

# Enter Input (Red, Blue) : AAABBBCDDDEE BBBTENETAAA
# Red Team :
# 5
# EECBA
# 1 Explosive(s) ! ! ! (HEAT)
# Blue Team Made (a) Mistake(s) 2 Bomb(s)
# ----------TENETTENET----------
# : maeT eulB
# 5
# TENET
# (EZEERF) ! ! ! (s)evisolpxE 2

# Enter Input (Red, Blue) : AAABBBDDD TENET
# Red Team :
# 0
# Empty
# 3 Explosive(s) ! ! ! (HEAT)
# ----------TENETTENET----------
# : maeT eulB
# 5
# TENET
# (EZEERF) ! ! ! (s)evisolpxE 0

# Enter Input (Red, Blue) : AAABBBCDDDEE OOOZZZTENETXXXYYY
# Red Team :
# 15
# EEDZDDCBXBBAYAA
# 0 Explosive(s) ! ! ! (HEAT)
# ----------TENETTENET----------
# : maeT eulB
# 5
# TENET
# (EZEERF) ! ! ! (s)evisolpxE 4

# Enter Input (Red, Blue) : PPPAAAABBBB PPPAAAA
# Red Team :
# 10
# BAAPAAPAPP
# 1 Explosive(s) ! ! ! (HEAT)
# ----------TENETTENET----------
# : maeT eulB
# 1
# A
# (EZEERF) ! ! ! (s)evisolpxE 2
