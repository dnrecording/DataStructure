def insertion_sort(lst, n):
    if n <= 1:
        return

    insertion_sort(lst, n-1)

    last = lst[n-1]
    j = n-2

    # while j >= 0 and lst[j] > last:
    #     lst[j+1] = lst[j]
    #     j = j-1
    j = loop_instead(lst, j, last)
    
    lst[j+1]=last
    # print("n :", n)
    # print("j :", j)
    # print("last :", last)
    if n != len(lst):
        print("insert", last, "at index", j+1, ":", lst[:n], lst[n:])
    else:
        print("insert", last, "at index", j+1, ":", lst)

def loop_instead(lst, j, last): # for shift j to the left
    if j < 0 or lst[j] < last: # j out of length || left less than right
        return j
    
    lst[j+1] = lst[j] # shift
    return loop_instead(lst, j-1, last) # go left

inp = [int(e) for e in input("Enter Input : ").split()]
n = len(inp)
insertion_sort(inp, n)
print("sorted")
print(inp)

# OUTPUT
# Enter Input : 1 2 3 4
# insert 2 at index 1 : [1, 2] [3, 4]
# insert 3 at index 2 : [1, 2, 3] [4]
# insert 4 at index 3 : [1, 2, 3, 4] 
# sorted
# [1, 2, 3, 4]

# Enter Input : 1 3 4 2
# insert 3 at index 1 : [1, 3] [4, 2]
# insert 4 at index 2 : [1, 3, 4] [2]
# insert 2 at index 1 : [1, 2, 3, 4] 
# sorted
# [1, 2, 3, 4]