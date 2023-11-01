def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    diction = {}
    for i in nums:
        if i not in diction:
            diction[i] = 1
        elif i in diction:
            diction[i] += 1
    
    for i in diction:
        if diction[i] == 1:
            return i

print(singleNumber([2,2,1]))