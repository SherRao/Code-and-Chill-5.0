def removeDuplicates(arr):
    sortedArr = sorted(arr)

    res = []
    prev = sortedArr[0]
    res.append(prev)

    for _, j in enumerate(sortedArr[1:]):
        val = j

        if prev != val:
            res.append(val)
        else:
            res.append(0)

        prev = val
    return res
