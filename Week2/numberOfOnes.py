def hammingWeight(n):
    count = 0
    for i in str(n):
        if i == "1":
            count += 1
    return count

print(hammingWeight(-3))