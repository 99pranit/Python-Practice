def skip(ch, s):
    if not s:
        return s
    if s[0:len(ch)] == ch:
        return skip(ch , s[len(ch):])
    else:
        return s[0] + skip(ch , s[1:])
    
print(skip('asd' ,'aasdaf'))