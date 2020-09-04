openList = ["[", "{", "("]
closeList = ["]", "}", ")"]
def Check_match(arg):
    s = []
    for i in arg:
        if i in openList:
            s.append(i)
            #print(s)
        elif i in closeList:
            temp = closeList.index(i)
            if((len(s) > 0) and (openList[temp] == s[len(s)-1])):
                s.pop()
            else:
                return "Parentheses : Unmatched ! ! !"
    if len(s) == 0:
        return "Parentheses : Matched ! ! !"
    else:
        return "Parentheses : Unmatched ! ! !"


n = input('Enter Input : ')
print(Check_match(n))


#OUTPUT

# Enter Input : ()[]
# Parentheses : Matched ! ! !

# Enter Input : [](]
# Parentheses : Unmatched ! ! !
