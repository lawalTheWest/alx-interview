#!/usr/bin/python3
'''
    LockBoxes Challenge
'''


def canUnlockAll(boxes):
    '''
        This determines if all the boxes can be opened or not
        Returns:
    '''
    box_length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < box_length:
        used_box = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < box_length and key not in opened_boxes:
                i = key
                break
        if used_box != i:
            continue
        else:
            break

    for i in range(box_length):
        if i not in opened_boxes and i != 0:
            return False
    return True
