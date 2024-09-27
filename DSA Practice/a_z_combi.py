import random
import pandas as pd

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Set to store unique combinations
combinations_set = set()

while len(combinations_set) < 10000:
    # Shuffle the alphabet to get a random combination
    shuffled = ''.join(random.sample(alphabet, len(alphabet)))
    combinations_set.add(shuffled)

# Print all unique combinations
df = pd.DataFrame(data= combinations_set , columns= ['Sequence'])
df.to_excel('Sequence.xlsx')
for combination in combinations_set:
    print(combination)
