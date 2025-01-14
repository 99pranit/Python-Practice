
def search(arr , target , index = 0 , answer = None):
    if answer is None:
        answer = []
    if index == len(arr):
        return answer
    elif arr[index] == target:
        answer.append(index + 1)
    return search(arr , target , index + 1, answer)
    
arr = [1,34,34,534,545,646]
target  = 34
print(search(arr , target))