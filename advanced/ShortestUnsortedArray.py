def findUnsortedSubarray(nums):
    nums_s = sorted(nums)

    if nums == nums_s:
        return 0

    l, r = 0, -1
    while nums[l] == nums_s[l]:
        l += 1
    while nums[r] == nums_s[r]:
        r -= 1
    return len(nums) - (l + abs(r) - 1)
