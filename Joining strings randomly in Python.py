import random, sys
words = ['why', 'who', 'what', 'why', 'when', 'how']

for i in range(100):
    print ''.join(random.choice(words[:randint(1, 4)]))

# If you don't care which element to be repeated
for i in range(100):
    arr = random.sample(words, random.randint(1,4))
    # select a random element from arr and append to self     
    arr.append(random.choice(words))
    print ''.join(arr)

# if you don't want this operation to be repeated if repetitions are already there,

arr = random.sample(words, random.randint(1,4))
# first check if array contains repetetive elements or not 
# if contains, go and join the list, otherwise select a random element
# from array and add to that array again  
if not [el for el in arr if arr.count(l) > 1]:
    arr.append(random.choice(words))                
print ''.join(arr)


# creating a random 'password'
import os, random, string

length = 13
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

print ''.join(random.choice(chars) for i in range(length))

# Python 3.6+ has a secrets module specifically for this purpose:
import secrets

password_length = 13
print(secrets.token_urlsafe(password_length))
