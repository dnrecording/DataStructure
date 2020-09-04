# ############################ วงเล็บ ############################
# openList = ["[", "{", "("]
# closeList = ["]", "}", ")"]
# def Check_match(arg):
#     s = []
#     for i in arg:
#         if i in openList:
#             s.append(i)
#         elif i in closeList:
#             temp = closeList.index(i)
#             if((len(s) > 0) and (openList[temp] == s[len(s)-1])):
#                 s.pop()
#             else:
#                 return "Parentheses : Unmatched ! ! !"
#     if len(s) == 0:
#         return "Parentheses : Matched ! ! !"
#     else:
#         return "Parentheses : Unmatched ! ! !"


# n = input('Enter Input : ')
# print(Check_match(n))


# #OUTPUT

# # Enter Input : ()[]
# # Parentheses : Matched ! ! !

# # Enter Input : [](]
# # Parentheses : Unmatched ! ! !

# ###############################################################

# ############## จานแตก ############## 
# x = input('Enter Input : ').split(',')

# ls = list()

# for i in x:
#     w,f = i.split()
    
#     if len(ls) == 0:
#         ls.append(i)
#     else:
#         back = ls[-1:][0]
#         #print(back)
#         nw,nf = back.split()
#         while int(w) > int(nw):
#             print(nf)
#             ls.pop()
#             if len(ls) > 0:
#                 back = ls[-1:][0]
#                 nw,nf = back.split()
#             else:
#                 break
#         ls.append(i)

# #OUTPUT

# # Enter Input : 1 10,5 20,3 30,3 40,4 50
# # 10
# # 40
# # 30

# # Enter Input : 90 8,68 99,44 3,44 102,50 2
# # 102
# # 3

# ###############################################################

# ############################ คอมโบ ############################ 
# n = input('Enter Input : ').split()

# ls = list()
# countls = list()
# combo = 0

# for i in n:
#     if len(ls) == 0:
#         ls.append(i)
#         countls.append(1)
#     elif ls[-1] == i:
#         if countls[-1] + 1 == 3:
#             combo += 1
#             for j in range(2):
#                 ls.pop()
#                 countls.pop()
#         else:
#             ls.append(i)
#             countls.append(2)
#     else:
#         ls.append(i)
#         countls.append(1)

# print(len(ls))
# ls.reverse()
# for i in range(len(ls)):
#     print(ls[i],end="")

# if len(ls) > 0:
#     if combo > 1:
#         print("\nCombo :", combo, "! ! !")
# else:
#     print("Empty")
#     if combo > 1:
#         print("Combo :", combo, "! ! !")

# # OUTPUT
# # Enter Input : G H H H H P
# # 3
# # PHG

# # Enter Input : L C C X X X C D
# # 2
# # DL
# # Combo : 2 ! ! !

# # Enter Input : C C C
# # 0
# # Empty

# # A C C A A A C A A

# ###############################################################

# ############################ ต้นไม้ ############################
# n = input("Enter Input : ").split(",")
# ls = []

# for i in n:
#     if i.startswith('A') :
#         while len(ls) > 0 and ls[-1] <= int(i.split()[1]):
#             ls.pop()
#         ls.append(int(i.split()[1]))
#     elif i.startswith('B'):
#         print(len(ls))



# # OUTPUT

# # Enter Input : A 4,A 3,B,A 5,A 8,B
# # 2
# # 1

# ###############################################################

# ############################ ต้นไม้หลอน ############################
# n = input("Enter Input : ").split(",")

# ls = []
# lt = []

# for i in n:
#     if i.startswith('A') :
#         while len(ls) > 0 and ls[-1] <= int(i.split()[1]):
#             ls.pop()
#         ls.append(int(i.split()[1]))
#         lt.append(int(i.split()[1]))
#     elif i.startswith('B'):
#         print(len(ls))
#     elif i.startswith('S'):
#         for i,j in enumerate(lt):
#             if j % 2 == 1:
#                 lt[i] += 2
#             else:
#                 lt[i] -= 1
#         ls.clear()
#         for k in lt:
#             while len(ls) > 0 and ls[-1] <= k:
#                 ls.pop()
#             ls.append(k)



# # OUTPUT

# # Enter Input : A 4,A 3,B,A 5,A 8,B
# # 2
# # 1

# ###############################################################