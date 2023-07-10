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
