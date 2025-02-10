def cleardigit(s):
    t = ''
    for i in s:
        if not i.isdigit():
            t += i
        else:
            t = t[:-1]
    return t

print(cleardigit('a1b2cd45ef'))