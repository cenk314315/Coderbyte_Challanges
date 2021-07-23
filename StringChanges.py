''' Have the function StringChanges(str) take the str parameter being passed, 
which will be a string containing letters from the alphabet, and return a new string based on the following rules. 
Whenever a capital M is encountered, duplicate the previous character (then remove the M), and whenever a capital N is encountered remove 
the next character from the string (then remove the N). All other characters in the string will be lowercase letters. For example: "abcNdgM" should return "abcgg". 
The final string will never be empty. '''

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
