#!/usr/bin/python3
''' lockbox module '''


def canUnlockAll(boxes):
    ''' 
        CanUnockAll
        ([boxes]): a list of list
    '''

    # initialize list of unlocked boxes
    unlocked = [False] * len(boxes)
    # set first box oprn
    unlocked[0] = True
    # iterate over boxes
    for index, box in enumerate(boxes):
        # check if box unlocked
        if unlocked[index]:
            # get keys in box
            for index, key in enumerate(box):
                # set box with found key to open
                if key < len(unlocked):
                    unlocked[key] = True
                    # get key at box that has been opened
                    # set boxe with keys to be open
                    for i in boxes[key]:
                        unlocked[i] = True
    return all(unlocked)
