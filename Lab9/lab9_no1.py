def bubble(l):
    lap = 0
    for last in range(len(l)-1, 0, -1):
        temp = None
        swapped = False
        for i in range(last):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True
        if swapped is True:
            lap += 1
            if last == 1:
                lap = 'last'
            print(lap, "step : ", end = "")
            print(l, "move[" + str(temp) + "]")
        else:
            print("last step : ", end = "")
            print(l, "move[" + str(temp) + "]")
            break

inp = [int(e) for e in input("Enter Input : ").split()]
bubble(inp)

# OUTPUT
# Enter Input : 4 3 2 1
# 1 step : [3, 2, 1, 4] move[4]
# 2 step : [2, 1, 3, 4] move[3]
# last step : [1, 2, 3, 4] move[2]

# Enter Input : 3 2 1 5 6 7
# 1 step : [2, 1, 3, 5, 6, 7] move[3]
# 2 step : [1, 2, 3, 5, 6, 7] move[2]
# last step : [1, 2, 3, 5, 6, 7] move[None]

# Enter Input : 1 2 3 4 5
# last step : [1, 2, 3, 4, 5] move[None]
