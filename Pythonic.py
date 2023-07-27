Pythonic code == efficient code
# Print the list created using the Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)

#The Zen of Python, by Tim Peters
import this

# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)]
print(nums_list2)

#enumerate() to get a counter in a loop, display item counts
# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [(i, name) for i, name in enumerate(names, 1)]
print(indexed_names_unpack)

/////
# map() function to apply the str.upper() method to each element in the names object
# Use map to apply str.upper to each element in names
names_map = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = list(names_map)

# Print the list created above
print(names_uppercase)

#Iterating With for Loops in Python
#A for loop in Python uses collection-based iteration. This means that Python assigns the next item from an iterable to the 
#loop variable on every iteration, like in this example:

values = ["a", "b", "c"]

for value in values:
    print(value)


