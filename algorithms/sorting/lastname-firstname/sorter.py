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




