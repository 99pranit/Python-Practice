'''
Given two strings s and part, perform the following operation on s 
until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.
'''

def removeOccurance(s , part):
    while True:
        index = s.find(part)
        if index != -1:
            s = s[:index] + s[index+len(part):]
        else:
            break
    return s

print(removeOccurance("daabcbaabcbc" , 'abc'))