x = input('Enter Input : ').split(',')

ls = list()

for i in x:
    w,f = i.split()
    
    if len(ls) == 0:
        ls.append(i)
    else:
        back = ls[-1:][0]
        #print(back)
        nw,nf = back.split()
        while int(w) > int(nw):
            print(nf)
            ls.pop()
            if len(ls) > 0:
                back = ls[-1:][0]
                nw,nf = back.split()
            else:
                break
        ls.append(i)
    




#OUTPUT

# Enter Input : 1 10,5 20,3 30,3 40,4 50
# 10
# 40
# 30

# Enter Input : 90 8,68 99,44 3,44 102,50 2
# 102
# 3

# weight=[]
# x=input("Enter Input : ").split(",")
# for i in x:
#     while len(weight)>0 and int(weight[-1].split(" ")[0]) < int(i.split(" ")[0]):
#         print(weight[-1].split(" ")[1])
#         weight.pop()
#     weight.append(i)