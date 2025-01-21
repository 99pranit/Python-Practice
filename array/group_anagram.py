"""
Given an integer array nums and an integer k, return the k most 
frequent elements within the array.
"""
def group_anagram(strs):
    freq = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in freq:
            freq[sorted_word] = []
        freq[sorted_word].append(word)

    return list(freq.values())

print(group_anagram(["act","pots","tops","cat","stop","hat"]))