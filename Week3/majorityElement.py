def majorityElement(nums: List[int]) -> int:
    fin = {}
    major = (len(nums) // 2) + 1
    for num in nums:
        if num in fin:
            fin[num] += 1
        else:
            fin[num] = 1
    for i in fin:
        if fin[i] >= major:
            return i