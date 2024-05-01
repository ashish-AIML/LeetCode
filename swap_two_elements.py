# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 
def swapList(newList, pos1, pos2):

    newList[pos1], newList[pos2] = newList[pos2], newList[pos1]
    return newList



newList = [1, 2, 3, 4, 5]
pos1 = 1
pos2 = 4
print(swapList(newList, pos1-1, pos2-1))