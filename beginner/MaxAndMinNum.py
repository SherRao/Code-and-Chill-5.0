def getNumbers(arr):
    maxNum, minNum = arr[0], arr[0]
    for num in arr:
        if num > maxNum:
            maxNum = num
        if num < minNum:
            minNum = num
    return maxNum, minNum
