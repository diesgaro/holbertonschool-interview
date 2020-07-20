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
        size = len(boxes)
        checklist = [False] * size
        pending = list()

        checklist[0] = True

        for box in boxes:
            if checklist[boxes.index(box)]:
                for key in box:
                    if key < size:
                        checklist[key] = True
                        if key in pending:
                            for value in boxes[key]:
                                if not checklist[value]:
                                    checklist[value] = True
                                    pending.remove(key)
            else:
                pending.append(boxes.index(box))

        for check in checklist:
            if check:
                result = True
            else:
                result = False
                break

    return result
