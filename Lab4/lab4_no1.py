n = input("Enter Input : ").split(',')

que = []

for i in n:
    if i.startswith('E'):
        que.append(i.split()[1])
        print(len(que))
    elif i.startswith('D'):
        if len(que) > 0:
            print(que[0], que.index(que[0]))
            que.pop(0)
        else:
            print('-1')
if len(que) > 0:
    print(' '.join(que))
else:
    print('Empty')

# OUTPUT
# Enter Input : E 10,E 20,E 30,E 40,D,D
# 1
# 2
# 3
# 4
# 10 0
# 20 0
# 30 40

# Enter Input : E 10,E 20,E 30,E 40,D,E 50,E 60,D,D,D,D,D,D
# 1
# 2
# 3
# 4
# 10 0
# 4
# 5
# 20 0
# 30 0
# 40 0
# 50 0
# 60 0
# -1
# Empty
