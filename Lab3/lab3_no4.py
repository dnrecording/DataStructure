n = input("Enter Input : ").split(",")
ls = []

for i in n:
    if i.startswith('A') :
        while len(ls) > 0 and ls[-1] <= int(i.split()[1]):
            ls.pop()
        ls.append(int(i.split()[1]))
    elif i.startswith('B'):
        print(len(ls))



# OUTPUT

# Enter Input : A 4,A 3,B,A 5,A 8,B
# 2
# 1
