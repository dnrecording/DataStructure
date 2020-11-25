def sort_dontcare(lst):
    for i in range(len(lst)):
        minid = i
        if lst[i] < 0:
            continue
        # print(lst[i], end = "")
        for j in range(i+1, len(lst)):
            if lst[j] < lst[minid] and lst[j] >= 0:
                # print("before",minid)
                minid = j
                # print("after",minid)
        lst[minid], lst[i] = lst[i], lst[minid]
    print(*lst)

inp = [int(e) for e in input("Enter Input : ").split()]
sort_dontcare(inp)

# OUTPUT
# Enter Input : 6 3 -2 5 -8 2 -2
# 2 3 -2 5 -8 6 -2

# Enter Input : 6 5 4 -1 3 0 2 -99 1
# 0 1 2 -1 3 4 5 -99 6