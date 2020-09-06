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


# Main
activity = {"0": "Eat", "1": "Game", "2": "Learn", "3": "Movie"}
place = {"0": "Res.", "1": "ClassR.", "2": "SuperM.", "3": "Home"}

my = Queue()
mydata = Queue()
your = Queue()
yourdata = Queue()

n = input("Enter Input : ").split(",")
score = 0
for i in n:
    a, b = i.split()
    my.enQueue(a)
    your.enQueue(b)

    mac, mpl = a.split(":")
    yac, ypl = b.split(":")
    mydata.enQueue(activity[mac] + ":" + place[mpl])
    yourdata.enQueue(activity[yac] + ":" + place[ypl])
    if mac == yac and mpl != ypl:
        score += 1
    if mac != yac and mpl != ypl:
        score -= 5
    if mpl == ypl and mac != yac:
        score += 2
    if mac == yac and mpl == ypl:
        score += 4

print("My   Queue = ", end="")
print(', '.join(my.items), sep=", ")
print("Your Queue = ", end="")
print(', '.join(your.items), sep=", ")
print("My   Activity:Location = ", end="")
print(', '.join(mydata.items), sep=", ")
print("Your Activity:Location = ", end="")
print(', '.join(yourdata.items), sep=", ")

if(score > 6):
    print("Yes! You're my love! : Score is ", end="")
elif(score >= 0):
    print("Umm.. It's complicated relationship! : Score is ", end="")
else:
    print("No! We're just friends. : Score is ", end="")
print(score, ".", sep="")

####################################################################

# OUTPUT
# Enter Input : 0:0 2:0,1:3 3:3,2:1 2:1
# My   Queue = 0:0, 1:3, 2:1
# Your Queue = 2:0, 3:3, 2:1
# My   Activity:Location = Eat:Res., Game:Home, Learn:ClassR.
# Your Activity:Location = Learn:Res., Movie:Home, Learn:ClassR.
# Yes! You're my love! : Score is 8.

# Enter Input : 2:1 2:1
# My   Queue = 2:1
# Your Queue = 2:1
# My   Activity:Location = Learn:ClassR.
# Your Activity:Location = Learn:ClassR.
# Umm.. It's complicated relationship! : Score is 4.

# Enter Input : 0:1 2:3,3:2 3:2
# My   Queue = 0:1, 3:2
# Your Queue = 2:3, 3:2
# My   Activity:Location = Eat:ClassR., Movie:SuperM.
# Your Activity:Location = Learn:Home, Movie:SuperM.
# No! We're just friends. : Score is -1.

# Enter Input : 3:3 1:3,0:0 1:1,2:2 3:3,0:3 0:1
# My   Queue = 3:3, 0:0, 2:2, 0:3
# Your Queue = 1:3, 1:1, 3:3, 0:1
# My   Activity:Location = Movie:Home, Eat:Res., Learn:SuperM., Eat:Home
# Your Activity:Location = Game:Home, Game:ClassR., Movie:Home, Eat:ClassR.
# No! We're just friends. : Score is -7.
