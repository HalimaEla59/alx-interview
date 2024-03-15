#!/usr/bin/python3
"""canUnlockAll method"""


def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.
    """
    if not boxes or type(boxes) is not list:
        return False

    keys = [0]
    for k in keys:
        for key in boxes[k]:
            if key not in keys and key < len(boxes):
                keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False
