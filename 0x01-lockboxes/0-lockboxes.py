#!/usr/bin/python3

"""Lokboxes project"""


def canUnlockAll(boxes):
    """
    Determine if all lockboxes in the given list can be unlocked.
    """
    num_boxes = len(boxes)
    unlocked_boxes = set([0])
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key not in unlocked_boxes and key < num_boxes:
                unlocked_boxes.add(key)
                stack.append(key)

    return len(unlocked_boxes) == num_boxes
