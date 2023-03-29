def linear_search(list, target):
    """ Return the index position of target if found, else returns None"""

    for i in range (0, len(list)):
        if list[i] == target:
            return i
        return None

    