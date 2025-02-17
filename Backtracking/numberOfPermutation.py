from itertools import permutations
def countPermutation(s):
    return len(set(p for i in range(1 , len(s)+1) for p in permutations(s,i)))

print(countPermutation("AAB"))