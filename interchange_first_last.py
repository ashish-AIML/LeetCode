#approach 1
# def swapList(newList):
#     size = len(newList)
#     temp = newList[-1]
#     newList[-1] = newList[0]
#     newList[0] = temp

#     return newList

#approach 2
def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList



#driver code
newList = [12, 34, 56, 23, 23]
print(swapList(newList))