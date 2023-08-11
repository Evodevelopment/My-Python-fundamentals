#Exercise

picture = [
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0],
]

print()
# Iterate over the picture
  # if 0 -> print ''
  # if 1 -> print *

for row in picture:
  for pixel in image:
    if (pixel == 1):
      print ('*' end= '')
    else:
      print(' ', end= '')
  print('')

# cleaning up the code:
  #defining variales to if the code the fill and empty repeats in my code
  
fill = '*'
empty = ''
for row in picture:
  for pixel in row:
    if (pixel == 1):
      print (fill, end= '')
    else:
      print(empty, end= '')
  print('')
