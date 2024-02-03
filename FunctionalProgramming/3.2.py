#Python supports functional programming features, and one of the key concepts is working with higher-order functions, which can take functions as arguments or return functions.
# Let's start with a simple example. Python has built-in functions like map(), filter(), and reduce(), which are commonly used in functional programming.

# map() applies a given function to all items in an input list and returns an iterator of the results.
# Example: Squaring each element in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

