# Author: Jayesh Sheth / https://github.com/jsheth7/code-poems
#
# Given a list of complete names (first, middle initial (optional) and last names)
# sort the list in ascending alphabetical order by (last name, first name)

# Note: This sorting could have been done via storing the data in a database and using SQL
# to sort the data by last name, first name ASC
# But the point of this file is demonstrate an implementation of such a sorting mechanism in Python

# Sample input:
# ['Caleb C. George', 'Caleb B. George', 'Brittany George', 'Bethany Person', 'Adam Person', 'George Gershwin', 'Alphonso Gershwin', 'Jay Shah', 'Adam Shah', 'Kayla Sheth', 'Jon Kap']

# Sorted output:
#['Brittany George', 'Caleb B. George', 'Caleb C. George', 'Alphonso Gershwin', 'George Gershwin', 'Jon Kap', 'Adam Person', 'Bethany Person', 'Adam Shah', 'Jay Shah', 'Kayla Sheth']


import sorter

names = ['Caleb C. George', 'Caleb B. George', 'Brittany George', 'Bethany Person', 'Adam Person', 'George Gershwin', 'Alphonso Gershwin', 'Jay Shah', 'Adam Shah', 'Kayla Sheth', 'Jon Kap']


sorted_names = sorter.sort_names(names)

print("Original list:")
print(names)

print("")
print("Sorted list:")
print(sorted_names)
