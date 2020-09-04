n = input("Enter Input : ").split(",")
#print(n)

# s = ' '.join(n)
# x = s.split()
# print(x)

ls = []
lt = []

for i in n:
    if i.startswith('A') :
        while len(ls) > 0 and ls[-1] <= int(i.split()[1]):
            ls.pop()
        ls.append(int(i.split()[1]))
        lt.append(int(i.split()[1]))
    elif i.startswith('B'):
        print(len(ls))
    elif i.startswith('S'):
        for i,j in enumerate(lt):
            if j % 2 == 1:
                lt[i] += 2
            else:
                lt[i] -= 1
        ls.clear()
        #ls = lt.copy()
        for k in lt:
            while len(ls) > 0 and ls[-1] <= k:
                ls.pop()
            ls.append(k)
        #print(ls)



# OUTPUT

# Enter Input : A 4,A 3,B,A 5,A 8,B
# 2
# 1
