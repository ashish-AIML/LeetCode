
def swapList(newList):
    size = len(newList)
    temp = newList[-1]
    newList[-1] = newList[0]
    newList[0] = temp

    return newList





#driver code
newList = [12, 34, 56, 23, 23]
print(swapList(newList))