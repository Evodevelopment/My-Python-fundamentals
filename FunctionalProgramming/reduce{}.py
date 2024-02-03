# reduce() applies a rolling computation to sequential pairs of values.
from functools import reduce

# Example: Calculating the product of elements in a list
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)
