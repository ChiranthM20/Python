'''Random Name Selector

Use the random module to pick a winner from a list of names.'''

import random

names = ["Chiranth", "Chiru", "Alice", "Bob", "Ram"]

Winner = random.choice(names)
print("Winner: ", Winner)