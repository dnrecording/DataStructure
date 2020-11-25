def alphabet_find(word):
    for i in word:
        if 'a' <= i <= 'z':
            return (ord(i))
    return 0

def alphabet_sort(inp):
    alphabet = []
    word = []
    for i in inp:
        alphabet.append(alphabet_find(i))
        word.append(i)
    for j in range(len(alphabet)):
        minid = j
        for k in range(j+1, len(alphabet)):
            if alphabet[k] < alphabet[minid] and alphabet[k] >= 0:
                minid = k
        alphabet[minid], alphabet[j] = alphabet[j], alphabet[minid]
        word[minid], word[j] = word[j], word[minid]
    return word

inp = input("Enter Input : ").split()
print(*alphabet_sort(inp))

# OUTPUT
# Enter Input : 932c 832u32 2344b
# 2344b 932c 832u32

# Enter Input : 99a 78b c2345 11d
# 99a 78b c2345 11d

# Enter Input : 572z 5y5 304q2
# 304q2 5y5 572z