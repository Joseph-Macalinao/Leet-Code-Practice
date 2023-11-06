def getWinner(arr, k):
    wins = 0
    while wins != k:
        if arr[0] > arr[1]:
            wins += 1
            rem = arr.pop(1)
            arr.append(rem)
        elif arr[1] > arr[0]:
            wins = 1
            rem = arr.pop(0)
            arr.append(rem)
        count += 1
    return arr[0]

print(getWinner([2,1,3,5,4,6,7], 2))