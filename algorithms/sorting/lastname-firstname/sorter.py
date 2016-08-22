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

import re


def extract_name_parts(name):

    """
    Return dict of first and last names, where first includes middle initial
    :param name: e.g. Englebert G. Humperdink
    :return: dict e.g. {'last': 'Humperdink', 'first': 'Englebert G.'}
    """

    regexp1 = re.compile(r"(?P<first>[a-zA-Z]{2,}) ?"
                         r"(?P<middle>[a-zA-Z]\.)? "
                         r"(?P<last>[a-zA-Z]{2,})"
                         )

    result = regexp1.search(name)

    if result is None:
        raise ValueError('Cannot parse full name into parts: ' + name)

    first = result.group('first')

    if result.group('middle') is not None:
        first += ' ' + result.group('middle')

    ret = {'first' : first, 'last': result.group('last')}

    return ret


def create_name_map(names):
    """
    Create dictionary of last name to first names
    :param names:
    :return:
    """

    name_map = {}

    for name in names:

        # Make sure we extract the first name correctly if there is a middle initial
        # e.g. in "Englebert G. Humperdink", the first name would be "Englebert G."
        # and the last would be "Humperdink" (include the first name and middle initial together)

        parts = extract_name_parts(name)

        if parts['last'] in name_map:
            name_map[parts['last']].append(parts['first'])
        else:
            name_map[parts['last']] = [parts['first']]

    return name_map


def sort_names(names):

    """
    Given an unsorted list of full names,
    return a combined sorted list by last name, first name (ascending)
    This is the "main" function
    :param names: unsorted list of full names
    :return: list of sorted full names
    """

    # Create dictionary of last name to first names
    name_map = create_name_map(names)

    # Sort last names
    last_names = name_map.keys()
    last_names.sort()

    sorted_names = []

    for last_name in last_names:
        first_names = name_map[last_name]
        first_names.sort()

        for first_name in first_names:
            sorted_names.append(first_name + ' ' + last_name)

    return sorted_names




