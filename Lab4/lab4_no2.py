n = input("Enter Input : ").split(',')

esque = []
enque = []

for i in n:
    if i.startswith('EN'):
        enque.append(i.split()[1])
    elif i.startswith('ES'):
        esque.append(i.split()[1])
    elif i.startswith('D'):
        if len(esque) > 0:
            print(esque[0])
            esque.pop(0)
        elif len(esque) < 1 and len(enque) > 0:
            print(enque[0])
            enque.pop(0)
        else:
            print('Empty')

# OUTPUT
# Enter Input : EN 1,EN 2,D,D,D,EN 3,D
# 1
# 2
# Empty
# 3

# Enter Input : EN 1,ES 2,D,D,D,EN 3,D
# 2
# 1
# Empty
# 3

# Enter Input : EN 1,ES 2,ES 99,D,D,D,EN 3,D
# 2
# 99
# 1
# 3

