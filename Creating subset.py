#creating a new list with subset of list using index in python

#A list:
a = ['a', 'b', 'c', 3, 4, 'd', 6, 7, 8]
I want a list using a subset of a using a[0:2],a[4], a[6:],

#that is I want a list ['a', 'b', 4, 6, 7, 8]

#Suppose
a = ['a', 'b', 'c', 3, 4, 'd', 6, 7, 8]

#and the list of indexes is stored in
b= [0, 1, 2, 4, 6, 7, 8]

#then a simple one-line solution will be
c = [a[i] for i in b]

#Solution1
Try new_list = a[0:2] + [a[4]] + a[6:].

#Or more generally, something like this:
from itertools import chain
new_list = list(chain(a[0:2], [a[4]], a[6:]))
This works with other sequences as well, and is likely to be faster.

#Or you could do this:
def chain_elements_or_slices(*elements_or_slices):
    new_list = []
    for i in elements_or_slices:
        if isinstance(i, list):
            new_list.extend(i)
        else:
            new_list.append(i)
    return new_list

new_list = chain_elements_or_slices(a[0:2], a[4], a[6:])
#URL:
https://stackoverflow.com/questions/19252301/creating-a-new-list-with-subset-of-list-using-index-in-python
