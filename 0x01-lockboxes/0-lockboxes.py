#!/usr/bin/python3
"""
Contains:
    Functions
    =========
    canUnlockAll - Receives a list of lists representing lockboxes which contain
    keys inside, with the first lockbox (boxes[0]) always unlocked. It returns a boolean
    checking if all lockboxes can be opened
"""
def canUnlockAll(boxes):
    """
    Receives an array of arrays representing lockboxes which contain
    keys (integers) inside. These keys can be used to open a lockbox at their value's index, with the first lockbox (boxes[0]) always unlocked. It returns a boolean
    checking if all lockboxes can be opened

    Args:
        boxes (list): A list of lists each of which representing a lockbox with keys (ints) inside

    Returns:
        bool: True if all lockboxes can be opened, False otherwise
    """
    def remove_index_val(lbox, idx):
        lbox = list(set(lbox))
        if idx in lbox:
            lbox.remove(idx)
        return lbox
    def flatten_concatenation(matrix):
        flat_list = []
        for row in matrix:
            flat_list += row
        return flat_list
    length = len(boxes)
    boxes = [remove_index_val(lbox, idx) for idx, lbox in enumerate(boxes)]
    boxes = flatten_concatenation(boxes)
    boxes = set(boxes)
    rng = set([i for i in range(1, length)])
    return rng.issubset(boxes)
