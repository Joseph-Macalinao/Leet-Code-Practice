def divide(dividend, divisor):
    div = 0
    count = 0
    while div <= dividend:
        div += divisor
        count += 1
    return count - 1

print(divide(12, 3))