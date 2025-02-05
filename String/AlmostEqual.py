'''
You are given two strings s1 and s2 of equal length. A string swap is an 
operation where you choose two indices in a string (not necessarily different)
and swap the characters at these indices.
'''
def almostequal(s1 , s2):
    if s1 == s2:
        return True
    
    diff = [(a , b) for a,b in zip(s1 , s2) if a != b]

    return len(diff) == 2 and diff[0] == diff[1][::-1]

print(almostequal('kurt' , 'krut'))