# Simple selection sort, based on first names only

# Sample output:
# Original list:
# ['Caleb C. George', 'Caleb B. George', 'Brittany George', 'Bethany Person', 'Adam Person', 'George Gershwin', 'Alphonso Gershwin', 'Jay Shah', 'Adam Shah', 'Kayla Sheth', 'Jon Kap']
#
# Sorted list (simple):
# ['Adam Person', 'Alphonso Gershwin', 'Adam Shah', 'Brittany George', 'Bethany Person', 'Caleb B. George', 'Caleb C. George', 'George Gershwin', 'Jon Kap', 'Jay Shah', 'Kayla Sheth']

# Ideas for variatons:
# sorting array of numbers vs names
# Run-time in Big O notation (and total number of iterations)

import selsort

names = ['Caleb C. George', 'Caleb B. George', 'Brittany George', 'Bethany Person', 'Adam Person', 'George Gershwin', 'Alphonso Gershwin', 'Jay Shah', 'Adam Shah', 'Kayla Sheth', 'Jon Kap']

print "Original list:"
print (names)

print "Sorted list (simple):"
names = selsort.selection_sort(names)
print (names)


