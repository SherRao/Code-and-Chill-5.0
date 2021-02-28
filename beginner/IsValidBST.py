def isValidBST(node, minNum, maxNum):
    if node == None:
        return True
    if node._value < minNum:
        return False
    if node._value > maxNum:
        return False
    return isValidBST(node._left, node._value, maxNum) and isValidBST(node._right, minNum, node._value)
