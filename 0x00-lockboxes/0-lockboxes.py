#!/usr/bin/python3
'''
    Method:
        canUnlockAll(boxes) - Method that check if all the boxes can be opened.
    Parameters:
        boxes: list of list
'''


def canUnlockAll(boxes):
    result = False
    if boxes:
        index = 0
        size = len(boxes)
        checklist = [False] * size
        pending = set()

        checklist[0] = True

        for box in boxes:
            if checklist[index]:
                for key in box:
                    if key < size:
                        if key in pending:
                            for value in boxes[key]:
                                if value < size:
                                    if not checklist[value]:
                                        checklist[value] = True
                        else:
                            checklist[key] = True
            else:
                pending.add(index)
            index += 1

        for check in checklist:
            if check:
                result = True
            else:
                result = False
                break

    return result
