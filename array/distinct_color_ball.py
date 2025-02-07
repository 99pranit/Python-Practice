'''
You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored.
For every query in queries that is of the form [x, y], you mark ball x with the color y. 
After each query, you need to find the number of distinct colors among the balls.
'''

def distinctColor(queries):
    freq = {}
    seen = {}
    distinct = 0
    ans = []

    for key , value in queries:
        if key in seen:
            oldval = seen[key]
            freq[oldval] -= 1
            if freq[oldval] == 0:
                distinct -= 1

        seen[key] = value
        if value not in freq or freq[value] == 0:
            distinct += 1

            freq[value] = freq.get(value , 0) + 1
        ans.append(distinct)

    return ans

print(distinctColor([[1,4],[2,5],[1,3],[3,4]]))
