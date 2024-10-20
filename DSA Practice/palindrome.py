def check_palindrome(str):
    start =  0
    end = len(str) - 1
    while start < end:
        if str[start] == str[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

str = "abcba"
print(check_palindrome(str))