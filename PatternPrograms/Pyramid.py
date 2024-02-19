def print_pyramid(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

# Example usage:
print_pyramid(5)

# In the example where we call print_pyramid(5), rows is 5, so the loop will iterate over the range 0, 1, 2, 3, 4. This means i will take values from 0 to 4.
