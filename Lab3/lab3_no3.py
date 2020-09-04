n = input('Enter Input : ').split()

ls = list()
countls = list()
combo = 0

for i in n:
    if len(ls) == 0:
        ls.append(i)
        countls.append(1)
    elif ls[-1] == i:
        if countls[-1] + 1 == 3:
            combo += 1
            for j in range(2):
                ls.pop()
                countls.pop()
        else:
            ls.append(i)
            countls.append(2)
    else:
        ls.append(i)
        countls.append(1)

print(len(ls))
ls.reverse()
for i in range(len(ls)):
    print(ls[i],end="")

if len(ls) > 0:
    if combo > 1:
        print("\nCombo :", combo, "! ! !")
else:
    print("Empty")
    if combo > 1:
        print("Combo :", combo, "! ! !")

# OUTPUT
# Enter Input : G H H H H P
# 3
# PHG

# Enter Input : L C C X X X C D
# 2
# DL
# Combo : 2 ! ! !

# Enter Input : C C C
# 0
# Empty

# A C C A A A C A A