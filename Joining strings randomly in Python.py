import random, sys
words = ['why', 'who', 'what', 'why', 'when', 'how']

for i in range(100):
    print ''.join(random.choice(words[:randint(1, 4)]))
