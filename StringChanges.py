

def StringChanges(s):
    s = list(s)

    while s[0] == 'M':
        del s[0]

    for i in range(len(s)):
        if s[i] == 'M':
            s[i] = s[i-1]

    while s[-1] == 'N':
        del s[-1]

    while 'N' in s:
        x = s.index('N')
        s.pop(x+1)
        s.pop(x)



    return ''.join(s)

    # keep this function call here 
print(StringChanges(input()))
